import re
from pathlib import Path
from typing import List

from pinecone import Pinecone, ServerlessSpec
from .config import get_settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import PyPDFLoader

from .config import get_settings

QA_HEADER_RE = re.compile(
    r"Q\s*&?\s*A\s*;?\s*#\s*\d+",
    re.IGNORECASE
)

def ensure_index():
    s = get_settings()
    pc = Pinecone(api_key=s.pinecone_api_key)

    existing = [i["name"] for i in pc.list_indexes()]

    if s.pinecone_index not in existing:
        pc.create_index(
            name=s.pinecone_index,
            dimension=384,  # ⭐ REQUIRED
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ),
        )

def extract_policies(pdf_path: str) -> List[Document]:
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    full_text = "\n".join(p.page_content for p in pages)

    headers = QA_HEADER_RE.findall(full_text)
    splits = QA_HEADER_RE.split(full_text)

    policies = []

    for i, body in enumerate(splits[1:], start=0):
        header = headers[i]

        # Extract number
        num_match = re.search(r"\d+", header)
        pid = f"Q&A #{num_match.group()}" if num_match else header

        text = f"{header}\n{body.strip()}"

        policies.append(
            Document(
                page_content=text,
                metadata={
                    "policy_id": pid,
                    "source": pdf_path
                }
            )
        )

    return policies

def ingest_folder(data_dir: str):
    s = get_settings()
    ensure_index()
    pc = Pinecone(api_key=s.pinecone_api_key)

    if s.pinecone_index not in [i["name"] for i in pc.list_indexes()]:
        pc.create_index(
            name=s.pinecone_index,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    pdfs = list(Path(data_dir).glob("*.pdf"))
    if not pdfs:
        raise ValueError("No PDF found")

    docs = []
    for pdf in pdfs:
        docs.extend(extract_policies(str(pdf)))

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    PineconeVectorStore.from_documents(
        docs,
        embedding=embeddings,
        index_name=s.pinecone_index,
        namespace=s.namespace
    )

    return {"policies_ingested": len(docs)}
