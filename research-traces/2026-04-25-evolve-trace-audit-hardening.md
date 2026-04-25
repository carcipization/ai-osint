# EVOLVE Trace — 2026-04-25 02:24 UTC

## Hypothesis
If cadence trace guards share one parsing core and there is one audit entrypoint that runs slot-specific checks over recent traces, trace-quality regressions will be caught faster and with less drift between STORY/FOLLOWUP policies.

## Changes made (repo-level)
1. Added shared guard helper module:
   - `scripts/trace_guard_common.py`
   - consolidates file read, section-missing detection, section extraction, and count parsing helpers.

2. Refactored STORY guard to shared core:
   - `scripts/story_trace_guard.py`
   - no threshold change; logic now uses shared parsing utilities.

3. Refactored FOLLOWUP guard to shared core:
   - `scripts/followup_trace_guard.py`
   - no threshold change; logic now uses shared parsing utilities.

4. Added audit runner:
   - `scripts/cadence_trace_audit.py`
   - auto-detects latest STORY/FOLLOWUP traces and runs guard scripts in one command.

## Before/after checks
### Before
- Guard logic duplicated across scripts, increasing risk of drift.
- No single command to audit recent private traces for slot-policy compliance.

### After
- Shared parser functions remove duplicate regex/parsing primitives.
- One audit command (`python3 scripts/cadence_trace_audit.py`) runs multi-slot checks and returns non-zero on failures.
- Dry run results show guard pass on recent no-publish traces and correctly flag older non-compliant cadence traces, proving regression-detection value.

## Expected impact (7-14 days)
- Faster detection of trace-quality regressions before cadence closeout.
- Lower maintenance overhead when thresholds/section requirements change.
- Better consistency between STORY and FOLLOWUP compliance enforcement.

## Notes
- EVOLVE-only slot respected: no docs publication performed.
- Changes are internal tooling + private trace only.