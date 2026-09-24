from typing import Optional
import os
from app.ingestion.loaders import DocumentLoader
from app.ingestion.chunking import TextChunker
from app.db.vector_store import VectorStore


class IngestionService:
    def __init__(self, vector_store: Optional[VectorStore] = None):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store = vector_store or VectorStore()

    def ingest_file(self, file_path: str, display_name: Optional[str] = None) -> int:
        """
        Orchestrates ingestion for a single file. Returns the number of chunks stored.
        display_name is the original file name shown in citations.
        """
        name = display_name or os.path.basename(file_path)
        print(f"Starting ingestion for: {name}")

        # 1. Load (with OCR for scanned pages)
        documents = self.loader.load_document(file_path)
        print(f"Loaded {len(documents)} documents.")

        # 2. Split
        chunks = self.chunker.split_documents(documents)
        if not chunks:
            raise ValueError("No readable text found in this file.")
        print(f"Split into {len(chunks)} chunks.")

        # 3. Tag every chunk with a clean source name and 1-based page number
        for c in chunks:
            page = c.metadata.get("page")
            c.metadata["source"] = name
            c.metadata["page"] = (int(page) + 1) if isinstance(page, int) else 1

        # 4. Replace older version of the same file, then store
        self.vector_store.delete_source(name)
        self.vector_store.add_documents(chunks)
        print("Ingestion complete.")
        return len(chunks)

    def ingest_directory(self, directory_path: str):
        """Ingests all supported files in a directory."""
        supported_extensions = ['.pdf', '.docx', '.csv', '.txt', '.md', '.png', '.jpg', '.jpeg']
        for root, _, files in os.walk(directory_path):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in supported_extensions:
                    full_path = os.path.join(root, file)
                    try:
                        self.ingest_file(full_path)
                    except Exception as e:
                        print(f"Failed to ingest {full_path}: {e}")
