PYTHON ?= python3
VENV := .venv

.PHONY: venv build validate test clean oneoff-story oneoff-datasets cadence-prompt sync-cadence-cron

venv:
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

build: venv
	./$(VENV)/bin/python scripts/publish.py

validate: venv
	./$(VENV)/bin/python scripts/validate_docs.py

clean:
	rm -rf $(VENV)

test:
	PYTHONPATH=. $(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

oneoff-story:
	python3 scripts/osintctl_cli.py enqueue-oneoff STORY

oneoff-datasets:
	python3 scripts/osintctl_cli.py enqueue-oneoff DATASETS

cadence-prompt:
	python3 scripts/osintctl_cli.py prompt cadence

sync-cadence-cron:
	python3 scripts/osintctl_cli.py sync-cadence-cron
