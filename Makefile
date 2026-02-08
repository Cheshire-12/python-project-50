make lint:
	uv run ruff check

make install:
	uv sync

make test:
	uv run pytest

make coverage:
	uv run pytest --cov --cov-report=xml