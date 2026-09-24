# Retrieval-Augmented Generation (RAG) Assistant

A local document Q&A web app built for PDF and text-based knowledge retrieval using FastAPI, Groq, and ChromaDB. It lets users upload documents, ask questions in natural language, and receive grounded answers generated from the uploaded content.

## Features

- PDF, DOCX, TXT, and image-based document ingestion
- Local vector search with ChromaDB
- Groq-powered answer generation grounded in retrieved context
- Browser-based chat interface
- Optional graph-style relationship extraction for document insights
- Simple authentication and local deployment setup

## Tech Stack

- Python
- FastAPI
- ChromaDB
- Groq API
- pypdf / python-docx / OCR support
- HTML + JavaScript frontend

## Project Structure

- groq_assistant/ — main web application and UI
- rag_system/ — backend RAG components
- requirements.txt — Python dependencies
- .env.example — sample environment variables

## Quick Start

1. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables

   Copy the sample file and update it with your keys:

   ```bash
   copy .env.example .env
   ```

   Then set values such as:
   - GROQ_API_KEY
   - APP_USERS
   - SECRET_KEY

4. Start the app

   ```bash
   cd groq_assistant
   python app.py
   ```

5. Open the app in a browser

   ```text
   http://127.0.0.1:8000/
   ```

## Default Login

The app includes a local login system. Example credentials:

- admin / admin123
- staff / staff123

You can change these in the environment configuration.

## Supported Files

- PDF
- DOCX
- TXT
- JPG / PNG images

## Notes

- This project is designed for local use and experimentation.
- It is best suited for personal, academic, or prototype deployment.
- For production use, add proper secrets management, HTTPS, and user-level access control.

## License

This project is intended for educational and demonstration purposes.

## Contact

For project questions, custom enhancements, or deployment help, please reach out through the repository issues or project maintainer contact.

