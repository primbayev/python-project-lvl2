install:
	poetry install

lint:
	poetry run flake8 gendiff

pytest_with_coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
