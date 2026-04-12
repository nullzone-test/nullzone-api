# nullzone-api

Internal API service for Nullzone platform.

## Stack
- Python 3.11+
- FastAPI
- PostgreSQL
- Redis

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment Variables

Copy `.env.example` to `.env` and fill in values.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| GET | /api/v1/users | List users |
| POST | /api/v1/users | Create user |
| GET | /api/v1/orders | List orders |

## CI

Runs on GitHub Actions. See `.github/workflows/ci.yml`.
