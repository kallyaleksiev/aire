# Makefile

.PHONY: format lint type-check test all

DIR_SRC := ./src

format:
	isort $(DIR_SRC)
	black $(DIR_SRC)

format-check:
	isort --check-only $(DIR_SRC)
	black --check $(DIR_SRC)

lint:
	flake8 $(DIR_SRC)

type-check:
	mypy $(DIR_SRC)

check: format-check type-check lint

test:
	pytest tests