.PHONY: format dev start
	
format:
	uv run ruff check --select I --fix .
	uv run ruff format .

dev:
	uv run fastapi dev src/contextcraft/main.py

start:
	PYTHONPATH=src uv run uvicorn contextcraft.main:app --host 0.0.0.0 --port 8000

