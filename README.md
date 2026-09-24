# Retrieval-Augmented Generation (RAG) Assistant

<div align="center">
  <img src="docs/assets/project-banner.svg" alt="RAG Document Assistant banner" width="100%" />
</div>

<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-Advanced-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  </a>
  <a href="https://groq.com/">
    <img alt="Groq" src="https://img.shields.io/badge/Groq-AI%20Inference-FB7C0F?style=for-the-badge" />
  </a>
  <a href="https://www.trychroma.com/">
    <img alt="ChromaDB" src="https://img.shields.io/badge/ChromaDB-Vector%20Search-8B5CF6?style=for-the-badge" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  </a>
</p>

A local AI document assistant for asking questions from PDFs, text files, and uploaded knowledge sources. The application combines retrieval-augmented generation, semantic search, and a simple browser interface to make document Q&A fast and usable.

## Overview

This project was built to help users:

- upload important documents
- search within them using embeddings
- ask natural-language questions
- receive responses grounded in the source content
- use the system locally without needing a heavy enterprise stack

## Tech stack

- Python
- FastAPI
- Groq LLM APIs
- ChromaDB for vector search
- OCR support for scanned PDFs and images
- HTML + JavaScript frontend

## Key features

- PDF, DOCX, TXT, and image ingestion
- Local semantic retrieval with embeddings
- Groq-powered answer generation grounded in context
- Login and user access flow
- Document upload and chat workflow in the browser
- Graph-style relationship extraction support for richer document understanding

## Demo preview

### Login screen

<img src="docs/assets/login-screen.svg" alt="Login screen preview" width="80%" />

### Chat workflow

<img src="docs/assets/chat-screen.svg" alt="Chat preview" width="80%" />

## Quick start

### 1. Clone and set up the environment

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure your environment

```bash
copy .env.example .env
```

Update the values inside `.env` with your keys and app settings, including:

- GROQ_API_KEY
- APP_USERS
- SECRET_KEY

### 3. Run the application

```bash
cd groq_assistant
python app.py
```

Then open:

```text
http://127.0.0.1:8000/
```

## Example credentials

The app includes local sample credentials such as:

- admin / admin123
- staff / staff123

## Project structure

```text
RAG/
├── groq_assistant/        # main app + frontend
├── rag_system/            # backend RAG logic
├── docs/assets/           # banner and UI screenshots
├── .env.example           # environment template
├── .gitignore             # repo hygiene rules
├── requirements.txt       # Python dependencies
├── README.md              # portfolio-style landing page
├── Dockerfile             # optional container setup
├── run.bat                # Windows launcher
└── app.py                 # entry point for local app
```

## Use cases

- research document Q&A
- internal knowledge assistant
- PDF-based support chatbot
- prototype enterprise RAG workflows

## Notes

- This project is optimized for local usage and demos.
- For production deployment, add HTTPS, a proper auth layer, secrets management, and user-level access control.

## License

This project is intended for educational, prototype, and portfolio use.

## Contact

For questions, feature requests, or collaboration opportunities, open an issue in the repository.

