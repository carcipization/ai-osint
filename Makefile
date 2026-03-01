PYTHON ?= python3
VENV := .venv

.PHONY: venv build validate clean

venv:
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

build: venv
	./$(VENV)/bin/python scripts/publish.py

validate: venv
	./$(VENV)/bin/python scripts/validate_docs.py

clean:
	rm -rf $(VENV)
