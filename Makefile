ENV = $(CURDIR)/env
PYTHON = $(ENV)/bin/python

make: coverage

coverage: deps
	$(ENV)/bin/nose2 --with-coverage

deps: env
	$(ENV)/bin/pip install --upgrade pip
	$(ENV)/bin/pip install -Ur requirements.txt

env:
	virtualenv --python=$(shell which python3.4) $(ENV)
