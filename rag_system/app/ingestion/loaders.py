from typing import List
import os
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader, WebBaseLoader, CSVLoader, TextLoader,
)
from langchain_core.documents import Document
from app.core.config import settings

_ocr_engine = None
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")


def _ocr_image(img) -> str:
    """OCR a PIL image with RapidOCR (pip-only, no Tesseract install)."""
    global _ocr_engine
    import numpy as np
    if _ocr_engine is None:
        from rapidocr_onnxruntime import RapidOCR
        _ocr_engine = RapidOCR()
    result, _ = _ocr_engine(np.array(img.convert("RGB")))
    return "\n".join(r[1] for r in result) if result else ""


class DocumentLoader:
    """Handles loading of various document types."""

    @staticmethod
    def load_pdf(file_path: str) -> List[Document]:
        """Loads a PDF. Pages with no text layer (scans) are read with OCR."""
        docs = PyPDFLoader(file_path).load()
        if settings.OCR_ENABLED:
            pdf = None
            for d in docs:
                if len(d.page_content.strip()) < 30:
                    import pypdfium2 as pdfium
                    pdf = pdf or pdfium.PdfDocument(file_path)
                    page_no = int(d.metadata.get("page", 0))
                    d.page_content = _ocr_image(pdf[page_no].render(scale=2).to_pil())
        return [d for d in docs if d.page_content.strip()]

    @staticmethod
    def load_image(file_path: str) -> List[Document]:
        """OCR for PNG/JPG scans."""
        if not settings.OCR_ENABLED:
            raise ValueError("OCR is disabled (OCR_ENABLED=false).")
        from PIL import Image
        text = _ocr_image(Image.open(file_path))
        return [Document(page_content=text, metadata={"source": file_path, "page": 0})]

    @staticmethod
    def load_docx(file_path: str) -> List[Document]:
        return Docx2txtLoader(file_path).load()

    @staticmethod
    def load_text(file_path: str) -> List[Document]:
        return TextLoader(file_path, encoding="utf-8", autodetect_encoding=True).load()

    @staticmethod
    def load_csv(file_path: str) -> List[Document]:
        return CSVLoader(file_path).load()

    @staticmethod
    def load_web(url: str) -> List[Document]:
        return WebBaseLoader(url).load()

    @staticmethod
    def load_document(source: str) -> List[Document]:
        """Picks the loader from the file extension or URL."""
        if source.startswith("http://") or source.startswith("https://"):
            return DocumentLoader.load_web(source)

        _, ext = os.path.splitext(source)
        ext = ext.lower()

        if ext == ".pdf":
            return DocumentLoader.load_pdf(source)
        elif ext == ".docx":
            return DocumentLoader.load_docx(source)
        elif ext == ".csv":
            return DocumentLoader.load_csv(source)
        elif ext in (".txt", ".md", ".log"):
            return DocumentLoader.load_text(source)
        elif ext in IMAGE_EXTS:
            return DocumentLoader.load_image(source)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
