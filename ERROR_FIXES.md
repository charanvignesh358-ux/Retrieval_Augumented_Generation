# 🚀 RAG System - Complete Setup and Error Resolution Guide

## ✅ What I've Fixed and Created for You

### 1. **Created `.env` file** 
   - Your system needs this to store the OpenAI API key
   - Located at: `C:\Users\HP\OneDrive\Desktop\RAG\.env`
   - **ACTION REQUIRED**: You must add your OpenAI API key here!

### 2. **Fixed `run.bat`**
   - Original version didn't change to correct directory
   - Now properly navigates to `rag_system` folder before starting

### 3. **Created `setup_and_run.bat` (⭐ RECOMMENDED)**
   - Complete automated setup script
   - Creates virtual environment
   - Installs all dependencies
   - Starts the server
   - **This is your main entry point!**

### 4. **Created `quick_start.bat`**
   - For subsequent runs after initial setup
   - Faster startup (skips installation)
   - Use this after you've run `setup_and_run.bat` once

### 5. **Created `troubleshoot.bat`**
   - Diagnostic tool to check your setup
   - Identifies missing components
   - Verifies API key configuration

### 6. **Created `test_client.py`**
   - Interactive Python script to test your API
   - Easy way to ingest documents and query
   - User-friendly menu interface

### 7. **Created `SETUP_GUIDE.md`**
   - Comprehensive documentation
   - Common issues and solutions
   - Usage examples and debugging tips

---

## 🎯 Quick Start (3 Steps to Success)

### Step 1: Get Your OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### Step 2: Add API Key to .env File
1. Open `C:\Users\HP\OneDrive\Desktop\RAG\.env` in Notepad
2. Find this line:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Replace `your_openai_api_key_here` with your actual key:
   ```
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   ```
4. Save and close

### Step 3: Run the Setup Script
1. Navigate to `C:\Users\HP\OneDrive\Desktop\RAG`
2. **Double-click `setup_and_run.bat`**
3. Wait for installation (5-10 minutes first time)
4. Server will start automatically

---

## 📋 Common Errors and Solutions

### Error 1: "Python is not recognized"
**Symptom**: When running batch files, you get "Python is not recognized as an internal or external command"

**Solution**:
1. Install Python from https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart your computer
4. Open Command Prompt and type: `python --version`

---

### Error 2: "OPENAI_API_KEY is missing"
**Symptom**: Server starts but crashes with "OPENAI_API_KEY is missing from environment variables"

**Solution**:
1. Make sure you created `.env` file (not `.env.example`)
2. Edit `.env` file with your actual API key
3. No spaces around the `=` sign
4. Key should start with `sk-`
5. Restart the server

---

### Error 3: "Module not found" or Import Errors
**Symptom**: Errors like "ModuleNotFoundError: No module named 'fastapi'" or similar

**Solution**:
```cmd
# Navigate to RAG folder
cd C:\Users\HP\OneDrive\Desktop\RAG

# Activate virtual environment
venv\Scripts\activate

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

---

### Error 4: "uvicorn: command not found"
**Symptom**: Can't start the server, uvicorn not recognized

**Solution**:
Make sure virtual environment is activated:
```cmd
cd C:\Users\HP\OneDrive\Desktop\RAG
venv\Scripts\activate
pip install uvicorn --upgrade
```

---

### Error 5: ChromaDB or SQLite Errors
**Symptom**: Errors mentioning "sqlite3", "chromadb", or "DLL load failed"

**Solution A** - Install Visual C++ Redistributable:
1. Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Install and restart computer

**Solution B** - Reinstall ChromaDB:
```cmd
venv\Scripts\activate
pip uninstall chromadb
pip install chromadb --upgrade
```

---

### Error 6: Port 8000 Already in Use
**Symptom**: "Address already in use" or "Port 8000 is already allocated"

**Solution A** - Kill existing process:
```cmd
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F
```

**Solution B** - Use different port:
Edit `setup_and_run.bat` and change port to 8001:
```batch
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

---

### Error 7: "No module named 'app'"
**Symptom**: Import errors related to 'app' module

**Cause**: Running from wrong directory

**Solution**:
The uvicorn command must be run from the `rag_system` directory. The fixed `setup_and_run.bat` handles this automatically. If running manually:

```cmd
cd C:\Users\HP\OneDrive\Desktop\RAG\rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### Error 8: Pydantic Validation Errors
**Symptom**: Errors mentioning "pydantic" or "BaseSettings"

**Solution**:
```cmd
venv\Scripts\activate
pip install pydantic pydantic-settings --upgrade
```

---

### Error 9: LangChain Import Errors
**Symptom**: "No module named 'langchain_openai'" or similar

**Solution**:
```cmd
venv\Scripts\activate
pip install langchain langchain-openai langchain-community --upgrade
```

---

## 🧪 Testing Your Setup

### Method 1: Using Troubleshoot Script
```cmd
# Double-click troubleshoot.bat
# It will check everything and tell you what's wrong
```

### Method 2: Using Web Browser
1. Start the server with `setup_and_run.bat`
2. Open browser and go to: http://localhost:8000/docs
3. You should see interactive API documentation
4. Try the endpoints directly in the browser

### Method 3: Using Test Client
```cmd
# After server is running, open a new Command Prompt
cd C:\Users\HP\OneDrive\Desktop\RAG
venv\Scripts\activate
python test_client.py
```

---

## 📝 Full Manual Setup (If Scripts Fail)

Sometimes batch scripts don't work due to permission issues. Here's the manual method:

### 1. Open Command Prompt as Administrator
Right-click Command Prompt → "Run as administrator"

### 2. Navigate to Project
```cmd
cd C:\Users\HP\OneDrive\Desktop\RAG
```

### 3. Create Virtual Environment
```cmd
python -m venv venv
```

### 4. Activate Virtual Environment
```cmd
venv\Scripts\activate
```
You should see `(venv)` at the start of your command prompt.

### 5. Upgrade pip
```cmd
python -m pip install --upgrade pip
```

### 6. Install Dependencies
```cmd
pip install -r requirements.txt
```
This will take 5-10 minutes. Wait for it to complete.

### 7. Configure .env File
```cmd
# Copy template
copy .env.example .env

# Edit with Notepad
notepad .env
```
Add your OpenAI API key, save and close.

### 8. Start Server
```cmd
cd rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 9. Access API
Open browser: http://localhost:8000/docs

---

## 🎮 Using the System

### Upload a Document
1. Go to http://localhost:8000/docs
2. Find `/api/v1/ingest` endpoint
3. Click "Try it out"
4. Click "Choose File" and select a PDF or DOCX
5. Click "Execute"
6. Wait for "Ingestion complete" message

### Query the System
1. Find `/api/v1/query` endpoint
2. Click "Try it out"
3. Enter query in JSON format:
```json
{
  "query": "What is the main topic of the document?",
  "session_id": "my_session"
}
```
4. Click "Execute"
5. See the answer and sources

---

## 🔍 Verification Checklist

Use this checklist to ensure everything is working:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created (`venv` folder exists)
- [ ] `.env` file created with valid OpenAI API key
- [ ] All dependencies installed (no errors during `pip install`)
- [ ] Server starts without errors
- [ ] Can access http://localhost:8000 in browser
- [ ] Can access http://localhost:8000/docs (Swagger UI)
- [ ] Can upload a document successfully
- [ ] Can query and get responses

---

## 📞 Still Having Issues?

### Diagnostic Commands

Run these in Command Prompt to gather information:

```cmd
# Check Python version
python --version

# Check pip version
python -m pip --version

# Check if virtual environment exists
dir venv

# Check if .env file exists
dir .env

# Check installed packages
venv\Scripts\activate
pip list

# Test Python imports
python -c "import fastapi; print('FastAPI OK')"
python -c "import langchain; print('LangChain OK')"
python -c "import chromadb; print('ChromaDB OK')"
```

### Log Files
If server crashes, check the error messages in the Command Prompt window. Copy the full error and search for it in the SETUP_GUIDE.md file.

---

## 🎯 Success Indicators

You'll know everything is working when:
1. ✅ Server starts with message: "Application startup complete"
2. ✅ You can see "Welcome to the Enterprise RAG System API" at http://localhost:8000
3. ✅ Swagger docs load at http://localhost:8000/docs
4. ✅ You can upload a file and see "Ingestion complete"
5. ✅ You can query and get answers with sources

---

## 📚 Additional Resources

- **OpenAI API Docs**: https://platform.openai.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **LangChain Docs**: https://python.langchain.com/
- **ChromaDB Docs**: https://docs.trychroma.com/

---

## 🔐 Security Reminders

- ⚠️ Never share your OpenAI API key
- ⚠️ Don't commit `.env` file to Git
- ⚠️ Keep your API key secure
- ⚠️ Monitor your OpenAI usage to avoid unexpected charges

---

## 🎉 Next Steps After Setup

Once everything is working:
1. Test with a sample PDF document
2. Try different types of queries
3. Experiment with conversational queries (same session_id)
4. Check the API logs to see how it processes documents
5. Read the full code to understand the architecture

Good luck! 🚀
