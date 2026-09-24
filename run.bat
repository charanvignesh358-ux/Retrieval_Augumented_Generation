@echo off
cd /d "%~dp0"
echo Starting Enterprise RAG System (Groq)...
if not exist venv (
  python -m venv venv
)
call venv\Scripts\activate
pip install -q -r requirements.txt
cd rag_system
start "" http://127.0.0.1:8000/docs
uvicorn app.main:app --host 127.0.0.1 --port 8000
pause
