# EVOLVE trace — 2026-04-30

## Hypothesis
FOLLOWUP quality and auditability will improve if required query-minimum compliance is verified by tooling rather than manual memory.

## Change made (repo-level)
1. Added `scripts/check_followup_trace.py`:
   - verifies `### Bluesky queries (5)` section exists,
   - verifies `### Polymarket queries (3)` section exists,
   - counts numbered query entries and fails if below required minimums.
2. Updated `skills/osint-journalism/SKILL.md` to require running this validator before FOLLOWUP finalize/push.

## Before/after check
- Before: FOLLOWUP query-minimum compliance depended on manual counting; easy to undercount silently.
- After: deterministic pass/fail check catches missing sections and under-minimum query logs.

## Expected impact (7-14 days)
- Fewer non-compliant FOLLOWUP runs.
- Faster reviewer confidence in trace completeness.
- Better consistency when rotating across runs/models.
