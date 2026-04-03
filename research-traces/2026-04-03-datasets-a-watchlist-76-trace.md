# DATASETS_A trace — 2026-04-03 (watchlist 76)

- Slot: DATASETS_A
- UTC window: 2026-04-03 01:39–01:44 UTC
- Run mode: datasets-only

## Selected additions (3)

1. Morocco - Risk Assessment Indicators
2. Algeria - Risk Assessment Indicators
3. Tunisia - Risk Assessment Indicators

## Overlap pass

Catalog overlap check against `docs/datasets-catalog.md` at selection time:
- Morocco: net-new
- Algeria: net-new
- Tunisia: net-new

## Selection rationale

- Prioritized broad non-specialist consequence relevance and regional breadth (North Africa gap fill).
- Maintained coherent risk-indicator family for fast cross-country denominator comparisons.
- Batch size held at required minimum 3 without low-signal filler.

## Blocked/error fetch log

All three HDX pages returned bot blocking in this environment; one retry each failed.

- source: Morocco - Risk Assessment Indicators
  - URL: https://data.humdata.org/dataset/morocco---risk-assessment-indicators
  - status/error: HTTP 406 bot activity block
  - UTC timestamp: 2026-04-03 01:43
  - retry outcome: fail (HTTP 406)

- source: Algeria - Risk Assessment Indicators
  - URL: https://data.humdata.org/dataset/algeria---risk-assessment-indicators
  - status/error: HTTP 406 bot activity block
  - UTC timestamp: 2026-04-03 01:43
  - retry outcome: fail (HTTP 406)

- source: Tunisia - Risk Assessment Indicators
  - URL: https://data.humdata.org/dataset/tunisia---risk-assessment-indicators
  - status/error: HTTP 406 bot activity block
  - UTC timestamp: 2026-04-03 01:43
  - retry outcome: fail (HTTP 406)
