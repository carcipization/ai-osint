# EVOLVE fallback trace (from STORY no-publish)

**Run UTC:** 2026-04-25 08:24 UTC
**Trigger:** STORY cycle exhausted candidates without a publishable lead.

## Hypothesis

A repeated bottleneck in STORY slots is slow, inconsistent first-pass quant checks on Socrata-based time series. A small reusable scanner that computes latest-vs-baseline deltas in one command should increase candidate rotation speed and reduce manual arithmetic errors, improving publishability over the next 7-14 days.

## High-leverage change made (repo-level)

Added executable tool:
- `scripts/socrata_anomaly_scan.py`

What it does:
- Pulls grouped Socrata time-series values (`$select/$group/$order`) from a specified dataset.
- Computes standardized triage stats:
  - latest value/date,
  - average of prior 4 periods,
  - average + std of prior 12 periods,
  - percent deltas and z-score.
- Emits structured JSON suitable for direct insertion into private research traces.

## Before/after checks

Before:
- Candidate quant checks were done with ad hoc one-off queries and manual calculations.
- Arithmetic and formatting varied run-to-run, slowing candidate turnover.

After:
- Ran:
  - `scripts/socrata_anomaly_scan.py --domain data.cdc.gov --dataset r8kw-7aab --date-col week_ending_date --metric-col covid_19_deaths --where "week_ending_date is not null"`
- Tool returned deterministic JSON summary with latest, baselines, pct deltas, and z-score.
- Output used immediately in this run's STORY trace candidate packet.

## Expected impact (7-14 day window)

- Faster candidate board triage in STORY slots (less time spent on repeated query/calc scaffolding).
- More consistent anomaly evidence structure across traces.
- Higher probability of reaching a publishable, mechanism-tested candidate within slot timeboxes.
