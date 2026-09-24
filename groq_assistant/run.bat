@echo off
cd /d "%~dp0"
if not exist .env (
  copy .env.example .env >nul
  echo Created .env. Fill in GROQ_API_KEY and the passwords in APP_USERS, save, close Notepad.
  notepad .env
  pause
)
if not exist venv (
  python -m venv venv
)
call venv\Scripts\activate
pip install -q -r requirements.txt
start "" http://localhost:8000
uvicorn app:app --host 127.0.0.1 --port 8000
pause
