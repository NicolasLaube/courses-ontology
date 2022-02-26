install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

lint:
	python -m pylint src tests
	python -m mypy src tests
	python -m flake8 src tests

test:
	pytest
tests: test

build:
	python -m src.construction

demo:
	streamlit run demonstrator/__main__.py
