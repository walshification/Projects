ENV = $(CURDIR)/env
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python
COVERAGE = $(ENV)/bin/coverage
SNIFFER = $(ENV)/bin/sniffer

make: test

test: $(COVERAGE) lint
	$(COVERAGE) run -m unittest discover ./tests
	$(COVERAGE) report -m

test-watch: $(SNIFFER)
	$(SNIFFER)

htmlcov: $(COVERAGE)
	$(COVERAGE) html

lint: $(COVERAGE)
	$(ENV)/bin/flake8 | > pep8_violations.txt

$(SNIFFER) $(COVERAGE): $(ENV)
	$(PIP) install -Ur requirements.txt
	touch $@

$(ENV):
	virtualenv --python=$(shell which python3) $(ENV)
	$(PIP) install --upgrade pip

distclean:
	rm -rf $(ENV) .coverage htmlcov __pycache__
	find . -iname '*.pyc' -exec rm {} \;

clean:
	rm -rf .coverage htmlcov

PHONY: test distclean clean
