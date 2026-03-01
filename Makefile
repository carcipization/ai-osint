PYTHON ?= python3
VENV := .venv

.PHONY: venv build validate clean oneoff-story oneoff-datasets

venv:
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

build: venv
	./$(VENV)/bin/python scripts/publish.py

validate: venv
	./$(VENV)/bin/python scripts/validate_docs.py

clean:
	rm -rf $(VENV)

oneoff-story:
	scripts/run_oneoff_slot.py STORY

oneoff-datasets:
	scripts/run_oneoff_slot.py DATASETS
