from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
import os
import shutil
import tempfile

from app.core.security import authenticate, current_user, admin_only
from app.db.vector_store import VectorStore
from app.services.ingest_service import IngestionService
from app.services.rag_service import RAGChain

router = APIRouter()

# One shared vector store (loads the embedding model once)
_vector_store = VectorStore()
ingest_service = IngestionService(_vector_store)
rag_chain = RAGChain(_vector_store)


class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = "default_session"


class QueryResponse(BaseModel):
    answer: str
    sources: List[dict]


@router.post("/login", summary="Log in (returns a token)")
def login(form: OAuth2PasswordRequestForm = Depends()):
    return authenticate(form.username, form.password)


@router.post("/ingest", summary="Upload and ingest a file (admin only)")
def ingest_file(file: UploadFile = File(...), user: dict = Depends(admin_only)):
    """Accepts PDF (scanned PDFs use OCR), DOCX, CSV, TXT, MD, PNG, JPG."""
    original = os.path.basename(file.filename or "upload")
    suffix = os.path.splitext(original)[1]
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        chunks = ingest_service.ingest_file(tmp_path, display_name=original)
        return {"message": f"{original} indexed.", "chunks": chunks}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


@router.post("/query", response_model=QueryResponse, summary="Ask a question")
def query_rag(request: QueryRequest, user: dict = Depends(current_user)):
    try:
        # History is kept per user so people never see each other's chats
        result = rag_chain.run(request.query, session_id=f"{user['u']}:{request.session_id}")
        return QueryResponse(answer=result["answer"], sources=result["source_documents"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sources", summary="List indexed files")
def list_sources(user: dict = Depends(current_user)):
    return [{"source": k, "chunks": v} for k, v in sorted(_vector_store.list_sources().items())]


@router.delete("/sources/{name}", summary="Remove a file from the index (admin only)")
def delete_source(name: str, user: dict = Depends(admin_only)):
    _vector_store.delete_source(name)
    return {"deleted": name}
