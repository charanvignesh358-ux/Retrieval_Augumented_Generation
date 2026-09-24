# RAG System - Complete Setup Guide

## 🚀 Quick Start (Recommended)

### Step 1: Get Your OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key (it will look like: `sk-proj-...`)

### Step 2: Run Setup Script
1. **Double-click `setup_and_run.bat`**
2. The script will:
   - Check Python installation
   - Create virtual environment
   - Install all dependencies
   - Start the API server

### Step 3: Configure API Key
When prompted, or after first run:
1. Open the `.env` file in the RAG folder
2. Replace `your_openai_api_key_here` with your actual API key
3. Save the file

### Step 4: Access the API
- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc

---

## 📋 Manual Setup (If scripts don't work)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key

### Step-by-Step Manual Installation

#### 1. Open Command Prompt
```cmd
cd C:\Users\HP\OneDrive\Desktop\RAG
```

#### 2. Create Virtual Environment
```cmd
python -m venv venv
```

#### 3. Activate Virtual Environment
```cmd
venv\Scripts\activate
```
You should see `(venv)` at the start of your command line.

#### 4. Upgrade pip
```cmd
python -m pip install --upgrade pip
```

#### 5. Install Dependencies
```cmd
pip install -r requirements.txt
```

This will install all required packages. This may take a few minutes.

#### 6. Configure Environment Variables
1. Copy `.env.example` to `.env`:
   ```cmd
   copy .env.example .env
   ```

2. Edit `.env` file with Notepad:
   ```cmd
   notepad .env
   ```

3. Replace `your_openai_api_key_here` with your actual OpenAI API key
4. Save and close

#### 7. Run the Application
```cmd
cd rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🔧 Common Issues and Solutions

### Issue 1: "Python is not recognized"
**Solution**: 
- Install Python from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart Command Prompt after installation

### Issue 2: "pip is not recognized"
**Solution**:
```cmd
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Issue 3: "OPENAI_API_KEY is missing"
**Solution**:
- Make sure you created the `.env` file from `.env.example`
- Verify your API key is correctly entered (no extra spaces)
- The key should start with `sk-`

### Issue 4: "Module not found" errors
**Solution**:
```cmd
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue 5: ChromaDB/SQLite errors
**Solution**:
```cmd
# Install Microsoft Visual C++ Redistributable
# Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe

# Or try installing chromadb separately:
pip install chromadb --upgrade
```

### Issue 6: Port 8000 already in use
**Solution**:
```cmd
# Use a different port
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

### Issue 7: Import errors with pydantic
**Solution**:
```cmd
pip install pydantic-settings pydantic --upgrade
```

---

## 📝 Testing the API

### Using Interactive Docs (Easiest)
1. Go to http://localhost:8000/docs
2. Try the endpoints directly in the browser

### Using cURL (Command Line)

#### 1. Test Root Endpoint
```cmd
curl http://localhost:8000/
```

Expected Response:
```json
{"message": "Welcome to the Enterprise RAG System API"}
```

#### 2. Ingest a Document
```cmd
curl -X POST "http://localhost:8000/api/v1/ingest" ^
  -H "accept: application/json" ^
  -H "Content-Type: multipart/form-data" ^
  -F "file=@path/to/your/document.pdf"
```

#### 3. Query the System
```cmd
curl -X POST "http://localhost:8000/api/v1/query" ^
  -H "accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "{\"query\":\"What is this document about?\",\"session_id\":\"test_session\"}"
```

### Using Python requests

Create a file `test_api.py`:
```python
import requests
import json

BASE_URL = "http://localhost:8000"

# Test root endpoint
response = requests.get(f"{BASE_URL}/")
print("Root:", response.json())

# Ingest a document
with open("sample.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(f"{BASE_URL}/api/v1/ingest", files=files)
    print("Ingest:", response.json())

# Query the system
query_data = {
    "query": "What is this document about?",
    "session_id": "test_session"
}
response = requests.post(f"{BASE_URL}/api/v1/query", json=query_data)
print("Query:", response.json())
```

Run it:
```cmd
python test_api.py
```

---

## 📂 Project Structure

```
RAG/
├── rag_system/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints.py      # API routes
│   │   ├── core/
│   │   │   └── config.py         # Configuration
│   │   ├── db/
│   │   │   └── vector_store.py   # ChromaDB integration
│   │   ├── ingestion/
│   │   │   ├── loaders.py        # Document loaders
│   │   │   └── chunking.py       # Text chunking
│   │   ├── services/
│   │   │   ├── ingest_service.py # Ingestion logic
│   │   │   └── rag_service.py    # RAG chain logic
│   │   └── main.py               # FastAPI app
│   └── tests/
│       └── test_api.py           # API tests
├── .env                          # Environment variables (you create this)
├── .env.example                  # Environment template
├── requirements.txt              # Python dependencies
├── setup_and_run.bat            # Automated setup (NEW)
├── quick_start.bat              # Quick start script (NEW)
└── README.md                     # Documentation
```

---

## 🎯 Usage Examples

### Supported File Types
- PDF documents (`.pdf`)
- Word documents (`.docx`)
- CSV files (`.csv`)
- Web URLs (starting with http:// or https://)

### Example Workflow

1. **Start the Server**
   ```cmd
   setup_and_run.bat
   ```

2. **Upload Documents** (via Swagger UI at http://localhost:8000/docs)
   - Click on `/api/v1/ingest` endpoint
   - Click "Try it out"
   - Upload a PDF or DOCX file
   - Click "Execute"

3. **Query Your Documents**
   - Click on `/api/v1/query` endpoint
   - Click "Try it out"
   - Enter your query in JSON format:
     ```json
     {
       "query": "What are the main points in the document?",
       "session_id": "my_session"
     }
     ```
   - Click "Execute"

---

## 🛠️ Advanced Configuration

### Changing Embedding Model
Edit `.env`:
```
EMBEDDING_MODEL=text-embedding-3-large
# Options: text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002
```

### Changing ChromaDB Location
Edit `.env`:
```
CHROMA_DB_DIR=D:/my_chroma_database
```

### Adjusting Chunk Size
Edit `rag_system/app/ingestion/chunking.py`:
```python
def __init__(self, chunk_size: int = 1500, chunk_overlap: int = 300):
```

---

## 🐛 Debugging

### Enable Verbose Logging
Add to `rag_system/app/main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Installed Packages
```cmd
venv\Scripts\activate
pip list
```

### Verify Environment Variables
```cmd
venv\Scripts\activate
python -c "from app.core.config import settings; print(f'API Key Set: {bool(settings.OPENAI_API_KEY)}')"
```

---

## 📞 Support

If you encounter issues:
1. Check this guide's "Common Issues" section
2. Verify your OpenAI API key is valid
3. Make sure virtual environment is activated
4. Check logs in the terminal for specific error messages

---

## 🔒 Security Notes

- Never commit `.env` file to Git (it's in `.gitignore`)
- Keep your OpenAI API key secret
- Don't share your API key in screenshots or logs
- Regenerate your API key if accidentally exposed

---

## 📊 Next Steps

After successful setup:
1. Test with a sample document
2. Experiment with different query types
3. Try conversational queries (using same `session_id`)
4. Explore the advanced retrieval features
5. Consider deploying with Docker for production use

Happy querying! 🎉
