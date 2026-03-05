PYTHON ?= python3
VENV := .venv

.PHONY: venv build validate bulk-intake clean

venv:
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

build: venv
	./$(VENV)/bin/python scripts/publish.py

validate: venv
	./$(VENV)/bin/python scripts/validate_docs.py

bulk-intake: venv
	./$(VENV)/bin/python scripts/bulk_dataset_intake.py --pages 5 --rows 200 --top 150

clean:
	rm -rf $(VENV)
