# ai-osint

Public GitHub Pages site for publishing AI-assisted OSINT stories.

## Architecture (post-refactor)

Core control logic now lives in Python code (not giant inline cron prompts):

- `osintctl/state.py` — cadence state + rotation logic
- `osintctl/prompts.py` — prompt templates (cadence + one-off)
- `scripts/osintctl_cli.py` — CLI entrypoint used by humans + cron wiring
- `state/` — all operational state in one easy-to-scan tree

Publishing remains:
- `scripts/publish.py` (render docs + index/latest pointers)
- `scripts/validate_docs.py` (basic quality checks)

## State tree

```text
state/
  cadence/
    current_slot.txt
  followup/
    checkpoint_state.json
```

`state/cadence/current_slot.txt` is the source of truth for rotation.
Legacy `.cron_checkpoint_mode.txt` is still synchronized for compatibility.

## CLI usage

```bash
# Show cadence state
python3 scripts/osintctl_cli.py state show

# Set/advance slot
python3 scripts/osintctl_cli.py state set-slot STORY_A
python3 scripts/osintctl_cli.py state advance

# Print prompts generated from code
python3 scripts/osintctl_cli.py prompt cadence
python3 scripts/osintctl_cli.py prompt oneoff --slot STORY

# Queue one-off jobs (out-of-cadence)
python3 scripts/osintctl_cli.py enqueue-oneoff STORY
python3 scripts/osintctl_cli.py enqueue-oneoff DATASETS

# Update the main cadence cron message from generated prompt
python3 scripts/osintctl_cli.py sync-cadence-cron
```

## Make targets

```bash
make build
make validate
make test
make oneoff-story
make oneoff-datasets
make cadence-prompt
make sync-cadence-cron
```

## Tests

Basic harness (stdlib `unittest`):
- `tests/test_state.py`
- `tests/test_prompts.py`
- `tests/test_cli_smoke.py`

Run:

```bash
make test
```

## Published site (GitHub Pages)

- Pages root: `docs/`
- Latest pointers: `docs/latest.md` + `docs/latest.html`
- Index: `docs/index.html`
