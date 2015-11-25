ENV = $(CURDIR)/env
PYTHON = $(ENV)/bin/python

make: test

test: deps
	$(ENV)/bin/coverage run --source projects -m py.test
	$(ENV)/bin/coverage report

deps: env
	$(ENV)/bin/pip install --upgrade pip
	$(ENV)/bin/pip install -Ur requirements.txt

env:
	virtualenv --python=$(shell which python3.4) $(ENV)

clean:
	rm -rf $(ENV)
	find . -iname '*.pyc' -exec rm {} \;
