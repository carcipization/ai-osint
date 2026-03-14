# Datasets: EIA Weekly Petroleum Status Report adds fast fuel-supply stress context

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-eia-weekly-petroleum-status-report.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-eia-weekly-petroleum-status-report.md)

**Dateline:** 2026-03-14 09:01 UTC

## Story

Initial lead: [EIA Weekly Petroleum Status Report release page](https://www.eia.gov/petroleum/supply/weekly/).

Fuel inventories and refinery throughput are broad public-interest signals because they can quickly affect transport costs, household budgets, and freight reliability. In this STORY_C run, no event-style candidate cleared the full novelty-and-importance bar without duplicating very recent publications, so we executed mandatory fallback and added the **U.S. EIA Weekly Petroleum Status Report (WPSR)** as a high-utility operational dataset.

WPSR matters because it provides a recurring official snapshot of U.S. crude and product inventories, refinery activity, and implied supply-demand pressure in one place. That gives reporters and non-specialist decision-makers a reproducible way to distinguish routine weekly noise from developing supply stress.

Practical decision use: local planners, businesses, and households can use WPSR trend direction (with multi-week context) to anticipate whether fuel-cost pressure is likely to ease or tighten before it fully shows up in retail prices.

## Appendix: Method

- Ran STORY_C broad sweep with world-state and anomaly triggers.
- Tested multiple fresh official candidates (space weather, ENSO, earthquake, heat-risk outlook) and rejected near-duplicates lacking material new deltas.
- Executed mandatory fallback and selected WPSR for broad consequence and decision utility.
- Added WPSR entry to `docs/datasets-catalog.md` under **Energy, trade, and maritime**.

## Appendix: Limitations

- Weekly petroleum balances can be volatile and are sensitive to timing, imports/exports, and seasonal operations.
- Single-week moves should not be over-interpreted without multi-week and year-ago context.
- WPSR is U.S.-centric and should be paired with international oil-flow sources for global attribution.

## Appendix: Confidence

**Confidence: Moderate-High** (first-party official source with stable cadence; interpretation risk mainly comes from short-window volatility).

## Appendix: Sources

- [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)
- [EIA Weekly Petroleum Status Report archive/table hub](https://ir.eia.gov/wpsr/wpsrsummary.pdf)
- [EIA Open Data](https://www.eia.gov/opendata/)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
