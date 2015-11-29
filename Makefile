ENV = $(CURDIR)/env
PYTHON = $(ENV)/bin/python
COVERAGE = $(ENV)/bin/coverage

make: test

test: deps
	$(COVERAGE) run --source lib -m py.test
	$(COVERAGE) report -m

deps: env
	$(ENV)/bin/pip install --upgrade pip
	$(ENV)/bin/pip install -Ur requirements.txt

env:
	virtualenv --python=$(shell which python3.4) $(ENV)

clean:
	rm -rf $(ENV)
	find . -iname '*.pyc' -exec rm {} \;
