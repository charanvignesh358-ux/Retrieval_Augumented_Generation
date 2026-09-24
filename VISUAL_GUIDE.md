# 🎯 VISUAL STEP-BY-STEP GUIDE

## 📋 Complete Checklist

```
□ Step 1: Get OpenAI API Key
□ Step 2: Add Key to .env File
□ Step 3: Run setup_and_run.bat
□ Step 4: Wait for Installation
□ Step 5: Server Starts
□ Step 6: Test in Browser
□ Step 7: Upload Document
□ Step 8: Query System
```

---

## 🔑 STEP 1: Get OpenAI API Key (5 minutes)

```
1. Open browser
   ↓
2. Go to: https://platform.openai.com/api-keys
   ↓
3. Sign in (or create account)
   ↓
4. Click: "Create new secret key"
   ↓
5. Name it: "RAG System"
   ↓
6. Click: "Create secret key"
   ↓
7. COPY THE KEY (starts with sk-)
   ↓
   Example: sk-proj-abc123...
   
⚠️  IMPORTANT: Save it now! You can't see it again!
```

---

## 📝 STEP 2: Add Key to .env File (2 minutes)

```
1. Navigate to:
   C:\Users\HP\OneDrive\Desktop\RAG
   
2. Find file: .env
   
3. Right-click → Open with → Notepad
   
4. You'll see:
   ┌─────────────────────────────────────────┐
   │ OPENAI_API_KEY=your_openai_api_key_here │
   │ CHROMA_DB_DIR=./chroma_db               │
   │ EMBEDDING_MODEL=text-embedding-3-small  │
   └─────────────────────────────────────────┘
   
5. Replace ONLY: your_openai_api_key_here
   
6. After editing:
   ┌─────────────────────────────────────────┐
   │ OPENAI_API_KEY=sk-proj-abc123xyz...     │
   │ CHROMA_DB_DIR=./chroma_db               │
   │ EMBEDDING_MODEL=text-embedding-3-small  │
   └─────────────────────────────────────────┘
   
7. Save and Close (Ctrl+S, then close Notepad)

✅ Done!
```

---

## 🚀 STEP 3: Run Setup Script (1 minute)

```
1. Open folder:
   C:\Users\HP\OneDrive\Desktop\RAG
   
2. Find file: setup_and_run.bat
   
3. Double-click it
   
4. You'll see a black window (Command Prompt) open:
   
   ┌─────────────────────────────────────────┐
   │ RAG System - Setup and Run Script       │
   │ ========================================│
   │                                         │
   │ [1/5] Checking Python installation...  │
   │ Python 3.x.x                            │
   └─────────────────────────────────────────┘
   
⚠️  Don't close this window!
```

---

## ⏳ STEP 4: Wait for Installation (5-10 minutes)

```
What you'll see:

┌─────────────────────────────────────────┐
│ [2/5] Creating .env file...             │
│ [3/5] Creating virtual environment...   │
│ [4/5] Activating virtual environment... │
│ [5/5] Installing dependencies...        │
│                                         │
│ Collecting langchain...                 │
│ Collecting fastapi...                   │
│ Collecting chromadb...                  │
│ ... (many lines) ...                    │
│ Successfully installed xxx packages     │
└─────────────────────────────────────────┘

☕ This is a good time for coffee!

Common packages being installed:
- langchain (30+ sub-packages)
- fastapi (web framework)
- chromadb (vector database)
- openai (API client)
- uvicorn (server)
- And 50+ more dependencies
```

---

## ✅ STEP 5: Server Starts (Automatic)

```
When installation completes, you'll see:

┌─────────────────────────────────────────┐
│ Setup complete!                         │
│ ========================================│
│ Starting RAG System API...              │
│ API will be available at:               │
│   http://localhost:8000                 │
│ Interactive docs at:                    │
│   http://localhost:8000/docs            │
│                                         │
│ INFO: Started server process [12345]   │
│ INFO: Waiting for application startup. │
│ INFO: Application startup complete.    │
│ INFO: Uvicorn running on               │
│       http://0.0.0.0:8000              │
└─────────────────────────────────────────┘

✅ Success! Server is running!
⚠️  Keep this window open!
```

---

## 🌐 STEP 6: Test in Browser (1 minute)

```
1. Open your web browser (Chrome, Firefox, Edge)

2. Go to: http://localhost:8000

3. You should see:
   ┌─────────────────────────────────────────┐
   │ {"message": "Welcome to the Enterprise  │
   │  RAG System API"}                       │
   └─────────────────────────────────────────┘
   
   ✅ If you see this → Server is working!
   ❌ If page doesn't load → Check Step 5

4. Now go to: http://localhost:8000/docs

5. You should see:
   ┌─────────────────────────────────────────┐
   │ Enterprise RAG System API               │
   │ API for ingesting documents and         │
   │ querying knowledge base.                │
   │                                         │
   │ Version: 1.0.0                          │
   │                                         │
   │ Endpoints:                              │
   │ GET  /                                  │
   │ POST /api/v1/ingest                     │
   │ POST /api/v1/query                      │
   └─────────────────────────────────────────┘
   
   ✅ If you see this → System is ready!
```

---

## 📤 STEP 7: Upload Document (2 minutes)

```
On the Swagger UI page (http://localhost:8000/docs):

1. Find: POST /api/v1/ingest
   
2. Click the endpoint to expand it
   
3. Click: "Try it out" button
   
4. You'll see a file upload section:
   ┌─────────────────────────────────────────┐
   │ file * (required)                       │
   │ ┌─────────────────┐                     │
   │ │ Choose File     │                     │
   │ └─────────────────┘                     │
   └─────────────────────────────────────────┘
   
5. Click "Choose File"
   
6. Select a PDF, DOCX, or CSV file from your computer
   
7. Click: "Execute" button
   
8. Wait a moment...
   
9. You'll see response:
   ┌─────────────────────────────────────────┐
   │ Response body:                          │
   │ {                                       │
   │   "message": "File uploaded and         │
   │    ingestion started."                  │
   │ }                                       │
   └─────────────────────────────────────────┘
   
10. Check the Command Prompt window:
    ┌─────────────────────────────────────────┐
    │ Starting ingestion for: temp_file.pdf   │
    │ Loaded 5 documents.                     │
    │ Split into 23 chunks.                   │
    │ Added 23 chunks to vector store.        │
    │ Ingestion complete.                     │
    └─────────────────────────────────────────┘

✅ Document uploaded and processed!
```

---

## 💬 STEP 8: Query System (2 minutes)

```
Still on the Swagger UI page:

1. Find: POST /api/v1/query
   
2. Click the endpoint to expand it
   
3. Click: "Try it out" button
   
4. You'll see request body:
   ┌─────────────────────────────────────────┐
   │ {                                       │
   │   "query": "string",                    │
   │   "session_id": "default_session"       │
   │ }                                       │
   └─────────────────────────────────────────┘
   
5. Replace "string" with your question:
   ┌─────────────────────────────────────────┐
   │ {                                       │
   │   "query": "What is this document       │
   │            about?",                     │
   │   "session_id": "my_session"            │
   │ }                                       │
   └─────────────────────────────────────────┘
   
6. Click: "Execute" button
   
7. Wait 3-5 seconds...
   
8. You'll see response:
   ┌─────────────────────────────────────────┐
   │ Response body:                          │
   │ {                                       │
   │   "answer": "The document discusses...",│
   │   "sources": [                          │
   │     {                                   │
   │       "source": "temp_file.pdf",        │
   │       "page": 1                         │
   │     },                                  │
   │     ...                                 │
   │   ]                                     │
   │ }                                       │
   └─────────────────────────────────────────┘

✅ System is working! You got an answer!

Try more questions:
- "Summarize the main points"
- "What are the key findings?"
- "Tell me more about [specific topic]"
```

---

## 🎉 SUCCESS! What Now?

```
✅ You've successfully:
   □ Set up the RAG system
   □ Started the server
   □ Uploaded a document
   □ Queried and got answers

📚 Next Steps:
   □ Try different documents
   □ Ask follow-up questions (same session_id)
   □ Experiment with queries
   □ Read ARCHITECTURE.md to understand how it works
   
🔧 For next time:
   □ Just run quick_start.bat
   □ No need for full setup again
```

---

## ❌ If Something Went Wrong

### Problem: Python not found
```
Solution:
1. Install Python from python.org
2. Check "Add Python to PATH" during install
3. Restart computer
4. Try again
```

### Problem: API key error
```
Solution:
1. Check .env file
2. Make sure key starts with "sk-"
3. No spaces around the = sign
4. Save the file properly
```

### Problem: Module not found
```
Solution:
1. Open Command Prompt
2. cd C:\Users\HP\OneDrive\Desktop\RAG
3. venv\Scripts\activate
4. pip install -r requirements.txt --force-reinstall
```

### Problem: Port 8000 in use
```
Solution:
1. Close any other servers
2. Or open run script in Notepad
3. Change 8000 to 8001
4. Save and run again
```

### Problem: Nothing works
```
Solution:
1. Run troubleshoot.bat
2. Check what's marked with ❌
3. Look up error in ERROR_FIXES.md
4. Follow the solution
```

---

## 📞 Quick Help Reference

```
File to Check               When to Use It
────────────────────────────────────────────────
QUICK_REFERENCE.md          Need commands fast
ERROR_FIXES.md              Got an error
SETUP_GUIDE.md              Detailed instructions
ARCHITECTURE.md             Want to understand system
troubleshoot.bat            Diagnose problems
test_client.py              Test with Python
```

---

## 💡 Pro Tips

```
✅ DO:
- Keep Command Prompt window open while using API
- Use same session_id for conversation
- Start with small test documents
- Check logs in Command Prompt for errors
- Use Swagger UI for easy testing

❌ DON'T:
- Close Command Prompt window when server is running
- Share your API key
- Commit .env file to Git
- Upload huge files for first test
- Forget to activate venv for manual commands
```

---

## 🏁 Final Checklist

```
Before asking for help, verify:
□ Python is installed (python --version)
□ .env file exists and has your API key
□ Virtual environment created (venv folder exists)
□ Packages installed (no errors in setup)
□ Server started (saw "Application startup complete")
□ Can access http://localhost:8000
□ Can see docs at http://localhost:8000/docs
□ Tried troubleshoot.bat

If all ✅ but still issues:
→ Check ERROR_FIXES.md for your specific error
```

---

## 🎊 Congratulations!

```
You now have a working RAG system!

What you can do:
✓ Upload documents (PDF, DOCX, CSV)
✓ Ask questions about them
✓ Get AI-generated answers
✓ Have conversations (with memory)
✓ Build a knowledge base

What you learned:
✓ How to set up a Python project
✓ How to use virtual environments
✓ How to configure environment variables
✓ How to run a FastAPI server
✓ How to use REST APIs

Keep exploring! 🚀
```

---

**Remember**: The server must stay running to use the API!

**Quick restart**: Just run `quick_start.bat` next time!

**Need help**: Check the documentation files in your RAG folder!
