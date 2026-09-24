@echo off
echo ========================================
echo RAG System - Setup and Run Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Checking Python installation...
python --version
echo.

REM Check if .env file exists
if not exist ".env" (
    echo [2/5] Creating .env file from template...
    copy .env.example .env
    echo.
    echo WARNING: Please edit .env file and add your OpenAI API key!
    echo Open .env file and replace 'your_openai_api_key_here' with your actual API key
    echo.
    pause
) else (
    echo [2/5] .env file already exists
)
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [3/5] Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully!
) else (
    echo [3/5] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [4/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install/upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install requirements
echo [5/5] Installing dependencies...
pip install -r requirements.txt
echo.

echo ========================================
echo Setup complete!
echo ========================================
echo.
echo Starting RAG System API...
echo API will be available at: http://localhost:8000
echo Interactive docs at: http://localhost:8000/docs
echo.

REM Change to rag_system directory and run uvicorn
cd rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
