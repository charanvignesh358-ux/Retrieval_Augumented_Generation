@echo off
echo ========================================
echo Quick Start - RAG System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup_and_run.bat first
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please run setup_and_run.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

echo Starting RAG System API...
echo API available at: http://localhost:8000
echo Interactive docs at: http://localhost:8000/docs
echo.

REM Change to rag_system directory and run uvicorn
cd rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
