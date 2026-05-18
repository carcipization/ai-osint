# Datasets: Global measles situation sources refresh (watchlist 123)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-18-datasets-global-measles-situation-sources-refresh-watchlist-123.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-18-datasets-global-measles-situation-sources-refresh-watchlist-123.md)


**Dateline:** 2026-05-18

This cadence run validates three high-value public sources used for recurring measles situation monitoring and confirms they remain usable for cross-checking global burden context.

## What changed in this cadence window

- CDC global measles outbreaks page remains live and states monthly WHO-fed outbreak updates.
- WHO measles fact sheet remains live with refreshed burden/vaccination context (including 2024 deaths and first-dose coverage figures).
- ECDC path check for a previously-used monthly measles URL returned 404, indicating link drift and the need for route maintenance.

## Verification notes

1. CDC page still provides narrative and table-based outbreak context suitable for trend framing.
2. WHO fact sheet still provides headline epidemiological denominator metrics and vaccination coverage context.
3. ECDC failed URL resolution is treated as a monitoring signal for source-maintenance work, not as epidemiological change.

## Caveats

- CDC outbreak table is provisional and can backfill between monthly updates.
- WHO fact sheet is periodic context, not real-time event telemetry.
- ECDC URL changes can break automated pipelines if link discovery is not versioned.

## Bottom line

Publication outcome: **core CDC+WHO measles context sources are stable, while at least one ECDC route requires endpoint refresh in ingestion tooling.**

## Sources

1. https://www.cdc.gov/global-measles-vaccination/data-research/global-measles-outbreaks/index.html
2. https://www.who.int/news-room/fact-sheets/detail/measles
3. https://www.ecdc.europa.eu/en/measles-monthly
