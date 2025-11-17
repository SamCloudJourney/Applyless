# Getting Started

## Requirements
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+

## Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Frontend
```bash
cd frontend
npm install
npm run dev
```

## Docker Compose
```bash
cd infrastructure
docker compose up --build
```
