lint:
	uv run ruff check

install:
	uv sync

test:
	uv run pytest

coverage:
	uv run pytest --cov --cov-report=xml