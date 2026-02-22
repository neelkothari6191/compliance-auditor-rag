import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    openai_api_key: str
    pinecone_api_key: str
    pinecone_index: str
    namespace: str = "default"
    embed_model: str = "text-embedding-3-small"
    chat_model: str = "gpt-4o-mini"

def get_settings():
    return Settings(
        openai_api_key=os.environ["OPENAI_API_KEY"],
        pinecone_api_key=os.environ["PINECONE_API_KEY"],
        pinecone_index=os.environ["PINECONE_INDEX"],
    )