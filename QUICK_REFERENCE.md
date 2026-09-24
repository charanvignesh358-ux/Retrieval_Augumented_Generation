# 🚀 RAG System - Quick Reference Card

## 📍 **IMPORTANT: FIRST TIME SETUP**

### Before Running Anything:

1. **Get OpenAI API Key**: https://platform.openai.com/api-keys
2. **Edit `.env` file** in the RAG folder
3. **Replace** `your_openai_api_key_here` with your actual key

---

## ⚡ Quick Commands

### First Time Setup
```
Double-click: setup_and_run.bat
```

### Subsequent Runs  
```
Double-click: quick_start.bat
```

### Troubleshooting
```
Double-click: troubleshoot.bat
```

### Test API
```
1. Run server (setup_and_run.bat)
2. Open new terminal
3. cd C:\Users\HP\OneDrive\Desktop\RAG
4. venv\Scripts\activate
5. python test_client.py
```

---

## 🌐 Important URLs

| URL | Purpose |
|-----|---------|
| http://localhost:8000 | API Base |
| http://localhost:8000/docs | Interactive API Docs (Swagger) |
| http://localhost:8000/redoc | Alternative API Docs |

---

## 🔧 Manual Commands (If scripts don't work)

### Create Virtual Environment
```cmd
cd C:\Users\HP\OneDrive\Desktop\RAG
python -m venv venv
```

### Activate Virtual Environment
```cmd
venv\Scripts\activate
```

### Install Dependencies
```cmd
pip install -r requirements.txt
```

### Start Server
```cmd
cd rag_system
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🐛 Top 5 Common Errors

| Error | Quick Fix |
|-------|-----------|
| "Python not recognized" | Install Python, add to PATH, restart |
| "OPENAI_API_KEY missing" | Edit .env file with your key |
| "Module not found" | `pip install -r requirements.txt` |
| "Port 8000 in use" | Kill process or use port 8001 |
| "No module named 'app'" | Run from `rag_system` directory |

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `.env` | Your API key (you must edit this!) |
| `setup_and_run.bat` | Complete setup + start server |
| `quick_start.bat` | Fast start (after setup) |
| `troubleshoot.bat` | Check your configuration |
| `test_client.py` | Test the API interactively |
| `ERROR_FIXES.md` | Detailed troubleshooting |
| `SETUP_GUIDE.md` | Complete documentation |

---

## ✅ Health Check

Your system is working if:
- ✅ No errors when starting server
- ✅ Can access http://localhost:8000
- ✅ Can see Swagger docs at /docs
- ✅ Can upload files
- ✅ Can query and get answers

---

## 📝 API Examples

### Ingest Document (cURL)
```cmd
curl -X POST "http://localhost:8000/api/v1/ingest" ^
  -F "file=@document.pdf"
```

### Query System (cURL)
```cmd
curl -X POST "http://localhost:8000/api/v1/query" ^
  -H "Content-Type: application/json" ^
  -d "{\"query\":\"What is this about?\",\"session_id\":\"test\"}"
```

### Python Example
```python
import requests

# Ingest
with open("doc.pdf", "rb") as f:
    requests.post("http://localhost:8000/api/v1/ingest", 
                  files={"file": f})

# Query
response = requests.post("http://localhost:8000/api/v1/query",
    json={"query": "Summarize", "session_id": "test"})
print(response.json())
```

---

## 🎯 Workflow

```
1. Edit .env (add API key) ← DO THIS FIRST!
   ↓
2. Run setup_and_run.bat
   ↓
3. Wait for "Application startup complete"
   ↓
4. Open http://localhost:8000/docs
   ↓
5. Upload document via /api/v1/ingest
   ↓
6. Query via /api/v1/query
   ↓
7. Success! 🎉
```

---

## 💡 Pro Tips

- Use same `session_id` for conversational queries
- Start with small documents for testing
- Check logs in terminal for debugging
- Use Swagger UI for easy testing
- Keep server running while testing

---

## 🆘 Need Help?

1. Check `ERROR_FIXES.md` for solutions
2. Run `troubleshoot.bat` to diagnose issues
3. Check server logs in Command Prompt
4. Verify `.env` file has correct API key
5. Make sure virtual environment is activated

---

**Remember**: The server must be running for the API to work!

**Quick Test**: After starting server, visit http://localhost:8000 
If you see "Welcome to the Enterprise RAG System API" → You're good to go! ✅
