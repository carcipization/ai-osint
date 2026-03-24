# DATASETS_A trace — 2026-03-24 petroleum pass-through stack

UTC window: 2026-03-24 17:39–17:44

## Situational/anomaly sweep

World-state context scanned:
- Ongoing Hormuz disruption volatility and rapid Brent regime shifts in recent runs increased demand for better physical-vs-financial mechanism separation.

Anomaly/coverage gap identified:
- Catalog had strong natural-gas and electricity coverage but incomplete petroleum family coverage at the same granularity (flows + refining + prices + demand in one coherent stack).

## Selection rationale (consequence-first)

Chosen family: EIA petroleum API modules exposed via Data.gov.

Why selected:
1. Broad non-specialist consequence: direct linkage to fuel prices, freight costs, and household affordability.
2. Decision utility: supports practical read-through for transport, procurement, and service operators.
3. Chain completeness: upstream movement + refining + downstream price/consumption in one source family.
4. Reliability: first-party federal statistical infrastructure with clear cadence and metadata.

## Added datasets (6)
1. https://catalog.data.gov/dataset/petroleum-data-application-programming-interface-api
2. https://catalog.data.gov/dataset/petroleum-data-summary-application-programming-interface-api
3. https://catalog.data.gov/dataset/petroleum-data-prices-application-programming-interface-api
4. https://catalog.data.gov/dataset/petroleum-data-refining-and-processing-application-programming-interface-api
5. https://catalog.data.gov/dataset/petroleum-data-imports-exports-and-movements-application-programming-interface-api
6. https://catalog.data.gov/dataset/petroleum-data-consumption-sales-application-programming-interface-api

## Misses / deprioritized
- NOAA SWPC shortlist items were not promoted in this slot due current run’s stronger direct public-cost consequence in fuel-chain monitoring.

## Blocked/error fetch log
- None during this run.

## Outputs
- Updated catalog with 6 additions in Energy, trade, and maritime section.
- Published dataset intel post: `2026-03-24-dataset-intel-petroleum-supply-chain-pass-through-stack-watchlist-52.md`.
