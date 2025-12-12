.PHONY: run test lint
run:
	uvicorn app.main:app --reload --port 8000
test:
	pytest
lint:
	ruff check app tests
