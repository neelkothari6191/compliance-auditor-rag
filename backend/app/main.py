from fastapi import FastAPI
from .models import IngestRequest, QueryRequest
from .ingest import ingest_folder
from .rag_pipeline import run_rag
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Compliance Auditor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ingest")
def ingest(req: IngestRequest):
    return ingest_folder(req.data_dir)

@app.post("/query")
def query(req: QueryRequest):
    return run_rag(req.question)
