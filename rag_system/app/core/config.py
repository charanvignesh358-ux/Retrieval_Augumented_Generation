import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()  # finds RAG\.env by walking up from this file


class Settings(BaseSettings):
    # LLM (free): https://console.groq.com/keys
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # Embeddings run locally (free). Groq has no embedding API.
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHROMA_DB_DIR: str = "./chroma_db"

    # Login: "user:password:role,user2:password2:role" (roles: admin | user)
    APP_USERS: str = ""
    SECRET_KEY: str = ""
    TOKEN_HOURS: int = 8

    OCR_ENABLED: bool = True

    class Config:
        env_file = ".env"
        extra = "ignore"  # old OPENAI_* lines in .env will not crash startup


settings = Settings()
