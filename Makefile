PYTHON ?= python3
VENV := .venv

.PHONY: venv build clean

venv:
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

build: venv
	./$(VENV)/bin/python scripts/publish.py

clean:
	rm -rf $(VENV)
