install:
	poetry install

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

coverage:
	poetry run coverage run --omit '.venv/*' -m pytest && poetry run coverage report -m
