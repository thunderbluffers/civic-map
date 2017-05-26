VENV=.venv

PYTHON_BIN=python3
PIP_BIN=$(VENV)/bin/pip

DJANGO_MANAGE_BIN=$(VENV)/bin/python manage.py

all: install

$(VENV): $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || $(PYTHON_BIN) -m venv $(VENV)
	$(PIP_BIN) install -r $<
	touch $@

django-migrate:
	yes | $(DJANGO_MANAGE_BIN) migrate

install: $(VENV) django-migrate

runserver: DEV_ADDR=$(shell grep DEV_ADDR= .env | sed -e 's/DEV_ADDR=//')
runserver: install
	$(VENV)/bin/python3 manage.py runserver $(DEV_ADDR)

run: runserver

help:
	@echo '====================================================' && sleep 0.01
	@cat README.md
	@echo '====================================================' && sleep 0.01

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
