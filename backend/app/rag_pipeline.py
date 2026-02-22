from pinecone import Pinecone
from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

from .config import get_settings

SIMILARITY_THRESHOLD = 0.75


def build_vectorstore():
    s = get_settings()

    pc = Pinecone(api_key=s.pinecone_api_key)
    index = pc.Index(s.pinecone_index)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    return PineconeVectorStore(
        index=index,
        embedding=embeddings,
        namespace=s.namespace
    )


def run_rag(question: str):
    s = get_settings()

    vs = build_vectorstore()
    docs_scores = vs.similarity_search_with_score(question, k=3)

    docs = [d for d, _ in docs_scores]
    best_score = max([score for _, score in docs_scores], default=0)

    llm = ChatOllama(
    model="llama3",
    temperature=0
)

    if best_score >= SIMILARITY_THRESHOLD and docs:
        context = "\n\n".join(
            f"[{d.metadata.get('policy_id')} | Page {d.metadata.get('page')}]\n{d.page_content}"
            for d in docs
        )

        prompt = f"""
Answer ONLY using these policies:

{context}

Question: {question}
"""
        answer = llm.invoke(prompt).content
        source = "policy"

    else:
        prompt = f"Answer using general knowledge: {question}"
        answer = llm.invoke(prompt).content
        source = "general"

    return {"source": source, "similarity": best_score, "answer": answer}
