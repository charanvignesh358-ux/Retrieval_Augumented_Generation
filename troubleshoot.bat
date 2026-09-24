@echo off
echo ========================================
echo RAG System - Troubleshooting Script
echo ========================================
echo.

echo [Checking Python Installation]
python --version
if errorlevel 1 (
    echo ❌ Python is NOT installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
) else (
    echo ✅ Python is installed
)
echo.

echo [Checking pip]
python -m pip --version
if errorlevel 1 (
    echo ❌ pip is NOT working
) else (
    echo ✅ pip is working
)
echo.

echo [Checking Virtual Environment]
if exist "venv" (
    echo ✅ Virtual environment exists
) else (
    echo ❌ Virtual environment NOT found
    echo Run setup_and_run.bat to create it
)
echo.

echo [Checking .env file]
if exist ".env" (
    echo ✅ .env file exists
    echo.
    echo Checking if API key is set...
    findstr /C:"sk-" .env >nul
    if errorlevel 1 (
        echo ❌ OpenAI API key might not be set correctly
        echo Please edit .env file and add your API key
    ) else (
        echo ✅ API key appears to be set
    )
) else (
    echo ❌ .env file NOT found
    echo Run setup_and_run.bat to create it
)
echo.

echo [Checking Directory Structure]
if exist "rag_system\app\main.py" (
    echo ✅ Main application file found
) else (
    echo ❌ Main application file NOT found
)
echo.

echo [Checking if port 8000 is in use]
netstat -ano | findstr :8000 >nul
if errorlevel 1 (
    echo ✅ Port 8000 is available
) else (
    echo ⚠️  Port 8000 is already in use
    echo You may need to stop the existing process or use a different port
)
echo.

echo [Attempting to activate venv and check packages]
if exist "venv" (
    call venv\Scripts\activate.bat
    echo.
    echo Checking key packages...
    python -c "import fastapi; print('✅ FastAPI:', fastapi.__version__)" 2>nul || echo ❌ FastAPI not installed
    python -c "import langchain; print('✅ LangChain:', langchain.__version__)" 2>nul || echo ❌ LangChain not installed
    python -c "import chromadb; print('✅ ChromaDB:', chromadb.__version__)" 2>nul || echo ❌ ChromaDB not installed
    python -c "import openai; print('✅ OpenAI:', openai.__version__)" 2>nul || echo ❌ OpenAI not installed
)
echo.

echo ========================================
echo Troubleshooting Complete
echo ========================================
echo.
echo If you see any ❌ errors above, please:
echo 1. Run setup_and_run.bat to fix setup issues
echo 2. Edit .env file to add your OpenAI API key
echo 3. Check the SETUP_GUIDE.md for detailed solutions
echo.

pause
