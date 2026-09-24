# RAG System Architecture & Flow

## System Overview
```
┌─────────────────────────────────────────────────────────────┐
│                     RAG System Architecture                  │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   User/API   │ ──────> │  FastAPI     │ ──────> │   ChromaDB   │
│   Request    │         │  Endpoints   │         │ Vector Store │
└──────────────┘         └──────────────┘         └──────────────┘
                               │                          │
                               │                          │
                               ▼                          ▼
                      ┌──────────────┐         ┌──────────────┐
                      │  LangChain   │ <────── │  OpenAI      │
                      │  RAG Chain   │         │  Embeddings  │
                      └──────────────┘         └──────────────┘
                               │
                               ▼
                      ┌──────────────┐
                      │  OpenAI GPT  │
                      │  (Response)  │
                      └──────────────┘
```

## Document Ingestion Flow
```
┌─────────────────────────────────────────────────────────────┐
│                    Document Processing Pipeline              │
└─────────────────────────────────────────────────────────────┘

Step 1: Upload Document
┌──────────────┐
│ User uploads │ ──> PDF / DOCX / CSV / URL
│   via API    │
└──────────────┘
       │
       ▼
Step 2: Document Loading
┌──────────────┐
│ loaders.py   │ ──> PyPDFLoader / UnstructuredWordDocumentLoader
│              │     WebBaseLoader / CSVLoader
└──────────────┘
       │
       ▼
Step 3: Text Chunking
┌──────────────┐
│ chunking.py  │ ──> RecursiveCharacterTextSplitter
│              │     (1000 chars, 200 overlap)
└──────────────┘
       │
       ▼
Step 4: Generate Embeddings
┌──────────────┐
│ OpenAI       │ ──> text-embedding-3-small
│ Embeddings   │
└──────────────┘
       │
       ▼
Step 5: Store in Vector DB
┌──────────────┐
│ ChromaDB     │ ──> Persistent storage
│ Vector Store │     Similarity search enabled
└──────────────┘
```

## Query Processing Flow
```
┌─────────────────────────────────────────────────────────────┐
│                      Query Flow                              │
└─────────────────────────────────────────────────────────────┘

Step 1: User Query
┌──────────────┐
│ "What is     │
│  this about?"│
└──────────────┘
       │
       ▼
Step 2: Context from Chat History (if available)
┌──────────────┐
│ Session      │ ──> Previous messages
│ History      │
└──────────────┘
       │
       ▼
Step 3: Contextualize Question
┌──────────────┐
│ LangChain    │ ──> Reformulate with context
│ Prompt       │
└──────────────┘
       │
       ▼
Step 4: Generate Query Embedding
┌──────────────┐
│ OpenAI       │ ──> Vector representation
│ Embeddings   │
└──────────────┘
       │
       ▼
Step 5: Similarity Search
┌──────────────┐
│ ChromaDB     │ ──> Find k=5 most similar chunks
│ Retrieval    │
└──────────────┘
       │
       ▼
Step 6: Generate Answer
┌──────────────┐
│ OpenAI GPT-4 │ ──> Answer based on retrieved context
│ + Context    │
└──────────────┘
       │
       ▼
Step 7: Return Response
┌──────────────┐
│ {            │
│  "answer":   │
│  "sources":  │
│ }            │
└──────────────┘
```

## Directory Structure
```
RAG/
│
├── .env                        ← Your API key goes here! ⚠️
├── .env.example                ← Template
│
├── setup_and_run.bat          ← Main setup script ⭐
├── quick_start.bat            ← Fast restart
├── troubleshoot.bat           ← Diagnostic tool
├── test_client.py             ← API test tool
│
├── requirements.txt           ← Python dependencies
├── SETUP_GUIDE.md            ← Complete docs
├── ERROR_FIXES.md            ← Troubleshooting
├── QUICK_REFERENCE.md        ← Quick commands
│
└── rag_system/
    └── app/
        ├── main.py            ← FastAPI application
        │
        ├── api/
        │   └── endpoints.py   ← API routes (/ingest, /query)
        │
        ├── core/
        │   └── config.py      ← Configuration & env vars
        │
        ├── db/
        │   └── vector_store.py ← ChromaDB integration
        │
        ├── ingestion/
        │   ├── loaders.py     ← Document loaders
        │   └── chunking.py    ← Text splitting
        │
        └── services/
            ├── ingest_service.py ← Document processing
            └── rag_service.py    ← RAG chain logic
```

## API Endpoints
```
┌─────────────────────────────────────────────────────────────┐
│                        API Overview                          │
└─────────────────────────────────────────────────────────────┘

GET  /                   ← Health check
     Returns: {"message": "Welcome to the Enterprise RAG System API"}

POST /api/v1/ingest      ← Upload documents
     Input:  multipart/form-data (file)
     Output: {"message": "File uploaded and ingestion started"}
     
POST /api/v1/query       ← Ask questions
     Input:  {
               "query": "What is X?",
               "session_id": "my_session"
             }
     Output: {
               "answer": "...",
               "sources": [...]
             }

GET  /docs              ← Interactive API documentation (Swagger UI)
GET  /redoc             ← Alternative API documentation
```

## Component Interactions
```
┌─────────────────────────────────────────────────────────────┐
│                   Component Dependency Map                   │
└─────────────────────────────────────────────────────────────┘

main.py
  └── endpoints.py
       ├── ingest_service.py
       │    ├── loaders.py (DocumentLoader)
       │    ├── chunking.py (TextChunker)
       │    └── vector_store.py (VectorStore)
       │         └── OpenAI Embeddings
       │
       └── rag_service.py (RAGChain)
            ├── vector_store.py (VectorStore)
            ├── OpenAI ChatGPT
            └── LangChain
                 ├── History-Aware Retriever
                 ├── Retrieval Chain
                 └── Message History
```

## Data Flow - Complete Cycle
```
1. User uploads document.pdf
   ↓
2. API receives file → saves temporarily
   ↓
3. DocumentLoader detects PDF → uses PyPDFLoader
   ↓
4. Extracts text → creates Document objects
   ↓
5. TextChunker splits into 1000-char chunks (200 overlap)
   ↓
6. For each chunk:
   - Generate embedding via OpenAI API
   - Store in ChromaDB with metadata
   ↓
7. User sends query: "Summarize the document"
   ↓
8. System:
   - Checks session history (if any)
   - Reformulates query with context
   - Generates query embedding
   ↓
9. ChromaDB:
   - Performs similarity search
   - Returns top 5 relevant chunks
   ↓
10. LangChain:
    - Combines query + retrieved chunks
    - Sends to GPT-4
    ↓
11. GPT-4:
    - Generates answer based on context
    - Returns structured response
    ↓
12. API returns:
    {
      "answer": "The document discusses...",
      "sources": [{metadata}, {metadata}, ...]
    }
```

## Tech Stack Summary
```
┌────────────────────────────────────────────────┐
│ Component      │ Technology                    │
├────────────────┼───────────────────────────────┤
│ Web Framework  │ FastAPI                       │
│ API Server     │ Uvicorn                       │
│ Vector DB      │ ChromaDB                      │
│ LLM            │ OpenAI GPT-4                  │
│ Embeddings     │ OpenAI text-embedding-3-small │
│ Orchestration  │ LangChain                     │
│ Doc Loading    │ PyPDF, Unstructured          │
│ Text Splitting │ RecursiveCharacterTextSplitter│
└────────────────┴───────────────────────────────┘
```

## Memory & Session Management
```
Session Handling:
┌──────────────────────────────────────────┐
│ User Session ID: "my_session"            │
├──────────────────────────────────────────┤
│                                          │
│ Message History:                         │
│ ┌────────────────────────────────────┐  │
│ │ User: "What is X?"                 │  │
│ │ AI: "X is..."                      │  │
│ │ User: "Tell me more"               │  │
│ │ AI: "X also includes..."           │  │
│ └────────────────────────────────────┘  │
│                                          │
│ Context: Maintains conversation history  │
│          for follow-up questions         │
└──────────────────────────────────────────┘
```

## Scalability Considerations
```
Current Setup (Development):
- In-memory session storage
- Local ChromaDB
- Single process

Production Improvements:
- Redis for session management
- Persistent ChromaDB on disk/cloud
- Celery for async ingestion
- Load balancing with multiple workers
- Separate ingestion and query services
```
