# 🚀 NexusAI — AI-Powered Business Growth Platform

Turn customer conversations into business growth. NexusAI lets businesses upload their knowledge, launch a personalized AI chatbot, capture leads, and discover growth opportunities — all from one platform.

---

## ✨ Features

| Feature | Status |
|---|---|
| RAG chatbot (Gemini + ChromaDB) | ✅ Complete |
| PDF, DOCX, TXT upload | ✅ Complete |
| Paste FAQ / text directly | ✅ Complete |
| Source attribution in answers | ✅ Complete |
| Honest fallback for unknown questions | ✅ Complete |
| Lead capture (quote, demo, booking, contact) | ✅ Complete |
| Lead management dashboard | ✅ Complete |
| Conversation history | ✅ Complete |
| Real analytics (no fabricated stats) | ✅ Complete |
| AI Growth Insights | ✅ Complete |
| Business onboarding wizard | ✅ Complete |
| Chatbot customization (name, color, tone, CTAs) | ✅ Complete |
| Public shareable chatbot link | ✅ Complete |
| Embeddable iframe code | ✅ Complete |
| Multi-tenant data isolation | ✅ Complete |
| JWT authentication | ✅ Complete |
| Prompt injection protection | ✅ Complete |

---

## 🏗️ Architecture

```
kits/
├── backend/                  # FastAPI backend
│   ├── main.py               # App entry point
│   ├── config.py             # Settings (pydantic-settings)
│   ├── database.py           # SQLAlchemy async models
│   ├── auth.py               # JWT utilities
│   ├── routers/              # API route handlers
│   │   ├── auth_router.py
│   │   ├── businesses_router.py
│   │   ├── documents_router.py
│   │   ├── chat_router.py
│   │   ├── leads_router.py
│   │   └── analytics_router.py
│   └── services/             # Business logic
│       ├── rag_service.py    # Document processing + ChromaDB
│       ├── chat_service.py   # Gemini RAG + prompt safety
│       └── analytics_service.py
├── frontend/                 # Streamlit frontend
│   ├── app.py                # Landing page + auth
│   ├── pages/
│   │   ├── 1_Dashboard.py    # Business overview + onboarding
│   │   ├── 2_Knowledge_Base.py
│   │   ├── 3_Chatbot.py      # Owner preview + public customer chat
│   │   ├── 4_Leads.py        # Lead management
│   │   ├── 5_Analytics.py    # Charts + AI insights
│   │   └── 6_Settings.py     # Full configuration
│   └── utils/
│       ├── api_client.py     # FastAPI calls
│       └── helpers.py        # CSS, nav, auth guards
├── .env.example
├── run.py                    # One-command startup
└── README.md
```

**Stack:**
- **AI:** Google Gemini 1.5 Flash (answers) + text-embedding-004 (embeddings)
- **Vector DB:** ChromaDB (persistent, local)
- **Backend:** FastAPI + SQLAlchemy async + SQLite
- **Frontend:** Streamlit (multi-page)
- **Auth:** JWT (python-jose + passlib)

---

## ⚡ Quick Start

### 1. Get a Gemini API Key (free)
Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and create a free API key.

### 2. Set up environment
```bash
cd kits
copy .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### 3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Run the platform
```bash
python run.py
```

This starts:
- **Frontend** → http://localhost:8501
- **Backend**  → http://localhost:8000
- **API docs** → http://localhost:8000/docs

---

## 🔒 Security Notes

- All document content is treated as **reference data only** — it cannot override system rules
- Each business's ChromaDB collection is **strictly namespaced** — cross-tenant access is impossible
- Uploaded documents are validated for type and size before processing
- Prompt injection attempts are filtered before reaching Gemini
- Passwords are bcrypt-hashed; tokens are JWT with configurable expiry
- **Never commit `.env` to version control**

---

## 📋 API Endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/register` | Public | Create account |
| POST | `/api/auth/login` | Public | Get JWT token |
| GET | `/api/auth/me` | Bearer | Current user |
| GET/POST | `/api/businesses` | Bearer | List/create businesses |
| GET/PUT | `/api/businesses/{id}` | Bearer | Get/update business |
| GET | `/api/businesses/public/{slug}` | Public | Public chatbot config |
| POST | `/api/documents/{biz_id}/upload` | Bearer | Upload file |
| POST | `/api/documents/{biz_id}/paste-text` | Bearer | Paste text |
| GET/DELETE | `/api/documents/{biz_id}` | Bearer | List/delete docs |
| POST | `/api/chat` | Public | Send chat message |
| GET | `/api/chat/conversations/{biz_id}` | Public | List conversations |
| POST | `/api/leads` | Public | Capture lead |
| GET | `/api/leads/{biz_id}` | Bearer | List leads |
| PATCH | `/api/leads/{biz_id}/{lead_id}` | Bearer | Update lead status |
| GET | `/api/analytics/{biz_id}` | Bearer | Analytics summary |
| GET | `/api/analytics/{biz_id}/insights` | Bearer | AI growth insights |

---

## 🚀 Deployment

For production deployment:

1. Set a strong `SECRET_KEY` in `.env`
2. Replace SQLite with PostgreSQL: `DATABASE_URL=postgresql+asyncpg://user:pass@host/db`
3. Deploy ChromaDB to a persistent volume
4. Restrict CORS origins in `backend/main.py`
5. Use a reverse proxy (nginx) in front of both services
6. Set `GEMINI_API_KEY` as an environment secret in your hosting provider

---

## 📝 License

MIT — use freely for commercial and personal projects.
