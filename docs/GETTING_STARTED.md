# Getting Started

## Requirements
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+

## Environment bootstrap
```bash
cp .env.example .env
nano .env # update BACKEND_API_URL and NEXT_PUBLIC_API_URL once
```
> The same values are consumed by both the frontend (browser + SSR) and backend Docker Compose targets, so configuring them once prevents drift.

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
cp .env.example .env
nano .env # update BACKEND_API_URL/NEXT_PUBLIC_API_URL to your FastAPI URL
npm install
npm run dev
```

### Required environment variables

| Name | Purpose | Example |
| --- | --- | --- |
| `BACKEND_API_URL` | Server-side API base URL for Next.js server actions and SSR | `https://api.your-domain.com/api/v1` |
| `NEXT_PUBLIC_API_URL` | Browser-accessible API base URL | `https://api.your-domain.com/api/v1` |
| `NEXT_PUBLIC_MAPBOX_TOKEN` | Mapbox access token for the community map | `pk.test-token` |

> **Tip:** Production builds fail fast if these values still point to `localhost`. Configure them with the public Railway backend URL before deploying on Vercel.

## Docker Compose
```bash
cd infrastructure
docker compose up --build
```
