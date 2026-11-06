PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.PHONY: bootstrap check test verify

bootstrap:
	python3 -m venv .venv
	@test -f .env || cp .env.example .env

check:
	$(PYTHON) scripts/check_repository.py

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

verify: check test
