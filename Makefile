install:
	poetry install

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
