from typing import List
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from app.core.config import settings


class VectorStore:
    def __init__(self):
        # Local, free embeddings (downloaded once, ~80 MB). No OpenAI key needed.
        self.embedding_function = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

        self.db = Chroma(
            persist_directory=settings.CHROMA_DB_DIR,
            embedding_function=self.embedding_function,
        )

    def add_documents(self, documents: List[Document]):
        """Adds documents to the vector store."""
        if not documents:
            return
        self.db.add_documents(documents)
        print(f"Added {len(documents)} chunks to vector store.")

    def delete_source(self, source: str):
        """Removes every chunk that came from one file (used before re-uploading it)."""
        self.db.delete(where={"source": source})

    def list_sources(self) -> dict:
        """Returns {file name: number of chunks}."""
        counts: dict = {}
        for m in self.db.get(include=["metadatas"])["metadatas"]:
            name = (m or {}).get("source", "unknown")
            counts[name] = counts.get(name, 0) + 1
        return counts

    def similarity_search(self, query: str, k: int = 5) -> List[Document]:
        return self.db.similarity_search(query, k=k)

    def as_retriever(self, search_kwargs: dict = {"k": 5}):
        return self.db.as_retriever(search_kwargs=search_kwargs)
