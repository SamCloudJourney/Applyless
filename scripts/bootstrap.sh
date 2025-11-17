#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e backend[dev]
cd backend && alembic upgrade head
