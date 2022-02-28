install:
	pip install -r requirements.txt
	conda install --channel conda-forge pygraphviz

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
	python -m src.build

demo:
	streamlit run demonstrator/__main__.py

requests:
	python -m src.requests
	
checker:
	python -m src.checker
	
reasoner:
	python -m src.reasoner
