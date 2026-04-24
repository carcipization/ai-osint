# EVOLVE fallback trace (from FOLLOWUP no-publish)

**Run UTC:** 2026-04-24 02:24 UTC
**Trigger:** FOLLOWUP cycle found no materially conclusion-changing update.

## Hypothesis

A recurring root-cause failure mode in follow-up cycles is URL churn on primary sources (notably CDC and ENTSO-E), causing avoidable 404 retries and inconsistent trace quality. A reusable probe tool that automates canonical fallback checks should improve verification speed and consistency across the next 7-14 days.

## High-leverage change made (repo-level)

Added executable tool:
- `scripts/followup_probe.py`

What it does:
- Probes one or more source URLs.
- Captures initial status, UTC timestamp, and final URL.
- Automatically applies known canonical replacements for recurring churny paths (CDC dashboard legacy path; ENTSO-E short report slug).
- Emits structured JSON for direct insertion into research traces.

## Before/after checks

Before:
- Canonical recovery from 404s was manual and ad hoc per run.
- Trace logging format for retries varied run-to-run.

After:
- Ran `scripts/followup_probe.py` on three representative URLs and captured deterministic output (`/tmp/followup_probe_run.json`).
- Verification sample showed:
  - CDC legacy URL: initial HTTP 404 -> canonical retry HTTP 200.
  - ENTSO-E short slug: initial HTTP 404 -> canonical retry HTTP 200.
  - FAO URL: initial HTTP 200 (no retry needed).

## Expected impact (7-14 day window)

- Faster follow-up source validation under slot timeboxes.
- More consistent blocked/error and retry evidence in private traces.
- Higher probability of completing stronger evidence packs when updates are actually present.
