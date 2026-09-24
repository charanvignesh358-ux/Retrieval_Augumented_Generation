# RAG Document Assistant (Groq, free)

Runs alongside your existing `rag_system` folder; nothing there was changed.

## Run
1. Get a free key: https://console.groq.com/keys
2. Double-click `run.bat`. First run creates `.env` and opens it. Set:
   - `GROQ_API_KEY`
   - passwords in `APP_USERS` (format `user:password:role`). The app will not start while `change_me` is left in.
   - `SECRET_KEY` (any long random text)
3. Save, close Notepad, press a key. Browser opens at http://localhost:8000. Log in.

The first run installs packages (a few minutes). The first upload downloads the local embedding model (~80 MB); the first scanned page downloads nothing extra (OCR models ship with the package).

## Roles
- `admin`: upload, delete documents, view `/api/logs`, ask questions
- `user`: ask questions only

## OCR
Scanned PDF pages (pages with almost no text layer) and PNG/JPG images are read automatically with RapidOCR. Set `OCR_ENABLED=false` to turn it off. OCR is slower: expect a few seconds per page on CPU.

## How it works
- Ingest: parse (pypdf / python-docx / OCR) -> chunk (350 words, 60 overlap) -> embed locally (Chroma MiniLM) -> ChromaDB (`chroma_db/`).
- Query: embed question -> top 5 chunks -> Groq `llama-3.3-70b-versatile` answers only from that context, with citations.
- Every login, upload, query and delete is written to `audit.log` with the username.

## Security notes
- Login uses signed tokens that expire after `TOKEN_HOURS`, and locks a username for 5 minutes after 5 wrong passwords.
- Passwords live in plain text in `.env`; keep that file private. Passwords cannot contain `:` or `,`.
- It listens on 127.0.0.1 only. To share on a network, put it behind HTTPS (e.g. Caddy or nginx) first; plain HTTP would expose passwords.
- All logged-in users can query every document; there is no per-document permission yet.
