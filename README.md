# East Dulwich Forum — Modern Rebuild

This repository hosts the full-stack implementation of the modern East Dulwich Forum experience. It contains a Next.js 14 frontend, FastAPI backend, PostgreSQL database schema, infrastructure automation, and supporting documentation.

## Project Layout
- `docs/` — system architecture, ADRs, and design resources.
- `frontend/` — Next.js 14 (App Router) application with TailwindCSS + Shadcn UI.
- `backend/` — FastAPI service with SQLAlchemy, Pydantic, and JWT auth.
- `infrastructure/` — Dockerfiles, docker-compose stack, deployment configs.
- `scripts/` — helper scripts for bootstrapping, migrations, and data seeding.
- `.github/workflows/` — CI/CD pipelines for linting, tests, and build automation.

See `docs/ARCHITECTURE.md` for the confirmed system design, data models, and deployment strategy.

## Deployment configuration

Set the following environment variables before deploying:

| Service | Variable | Description |
| --- | --- | --- |
| Frontend (Vercel) | `NEXT_PUBLIC_API_URL` | Public HTTPS URL to the FastAPI `/api/v1` endpoint. |
| Frontend (Vercel) | `BACKEND_API_URL` | Server-side URL used by Next.js during SSR/server actions. Can point to a private Railway service as long as it is reachable from Vercel. |
| Backend (Railway) | `DATABASE_URL`, `JWT_SECRET`, etc. | See `backend/.env.example` for the complete list. |

> **Reminder:** Production builds now fail fast if either frontend variable references `localhost`. Always provide the public Railway backend URL (e.g., `https://east-dulwich-api.up.railway.app/api/v1`).
