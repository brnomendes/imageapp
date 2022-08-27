all: style test

style:
	python -m isort main.py app/ tests/
	python -m black main.py app/ tests/
	python -m mypy main.py app/ tests/
	python -m xenon main.py app/ --max-absolute B --max-modules C --max-average A
	python -m xenon tests/ --no-assert --max-absolute B --max-modules C --max-average A
	python -m bandit -q -r app/
	python -m bandit -s=B101 -q -r tests/

test:
	python -m pytest
