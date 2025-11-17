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
