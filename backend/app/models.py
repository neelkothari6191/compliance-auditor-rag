from pydantic import BaseModel

class IngestRequest(BaseModel):
    data_dir: str = "./data"

class QueryRequest(BaseModel):
    question: str
