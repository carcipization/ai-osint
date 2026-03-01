# AGENTS.md (ai-osint)

This repo uses a code-first control plane.

## Rules

1. Prefer `scripts/osintctl_cli.py` commands over editing cron prompts manually.
2. Keep prompt text in `osintctl/prompts.py`.
3. Keep cadence/state logic in `osintctl/state.py`.
4. Keep operational state under `state/`.
5. One-off runs must be out-of-cadence and must not mutate cadence state.

## Common workflows

- Show state: `python3 scripts/osintctl_cli.py state show`
- Queue one-off story: `python3 scripts/osintctl_cli.py enqueue-oneoff STORY`
- Sync cadence cron prompt: `python3 scripts/osintctl_cli.py sync-cadence-cron`

## Quality gates

- `make validate`
- `make test`

When changing cadence/prompt behavior, update tests and README in the same commit.
