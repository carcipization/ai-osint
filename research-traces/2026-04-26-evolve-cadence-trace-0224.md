# EVOLVE cadence trace

**Run UTC:** 2026-04-26 02:24 UTC
**Slot:** EVOLVE
**Publication:** none (EVOLVE run; docs publication disabled)

## Hypothesis

A frequent root cause of STORY no-publish cycles is uneven private-trace structure: candidate packets, claim-evidence mapping, and corroboration-independence checks are often assembled manually and inconsistently under time pressure. A deterministic scaffold should improve both speed and evidence discipline, increasing publishable-story hit rate over the next 7-14 days.

## High-leverage change made (repo-level)

Added executable tool:
- `scripts/story_trace_scaffold.py`

What it does:
- Generates a standardized STORY trace template aligned with SKILL-required workflow:
  - first-principles frame,
  - dual-trigger candidate board,
  - per-candidate 4-item packet + gate outcomes,
  - claim-evidence matrix,
  - corroboration independence ledger,
  - explicit disconfirmation block,
  - 72h overlap check,
  - publish/no-publish decision block.
- Supports configurable candidate count (`--candidates`) and output path.

## Before/after checks

Before:
- STORY trace quality varied by run; mandatory fields could be omitted or inconsistently formatted.
- Candidate rotation consumed extra time due to repeated manual section assembly.

After:
- Ran validation sample:
  - `scripts/story_trace_scaffold.py --out /tmp/story_scaffold_demo.md --run-label evolve-2026-04-26 --slot STORY --candidates 5`
- Verified generated scaffold includes all required packet/gate and evidence-ledger sections in one repeatable format.

## Expected impact (7-14 day window)

- Faster candidate-board execution in STORY slots (less manual scaffolding overhead).
- Better compliance with mechanism/importance and independence checks.
- Higher probability of reaching defensible publish decisions within slot timeboxes.
