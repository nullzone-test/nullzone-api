.PHONY: setup run test lint

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/uvicorn main:app --reload

test:
	.venv/bin/pytest tests/ -v

lint:
	.venv/bin/ruff check .
