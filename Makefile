VENV=.venv

PYTHON_BIN=python3
PIP_BIN=$(VENV)/bin/pip

all: install

$(VENV): $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || $(PYTHON_BIN) -m venv $(VENV)
	$(PIP_BIN) install -r $<
	touch $@

install: $(VENV)

runserver: DEV_HOST=$(shell grep DEV_HOST= .env | sed -e 's/DEV_HOST=//')
runserver: DEV_PORT=$(shell grep DEV_PORT= .env | sed -e 's/DEV_PORT=//')
runserver: install
	$(VENV)/bin/python3 manage.py runserver $(DEV_HOST):$(DEV_PORT)

run: runserver

help:
	@echo '====================================================' && sleep 0.01
	@cat README.md
	@echo '====================================================' && sleep 0.01

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
