# Datasets: Eurostat API suite added for EU structural-baseline and update-tracking workflows (Watchlist 15)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-dataset-intel-eurostat-api-structural-baselines-watchlist-15.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-dataset-intel-eurostat-api-structural-baselines-watchlist-15.md)

**Dateline:** 2026-03-06 12:08 UTC

## What changed

Added one genuinely new source to the datasets catalog:

- **Eurostat APIs (Statistics + Catalogue)** in the *Economy, governance, and structural risk* section.

## Why this source was selected

Eurostat fills a catalog gap: high-quality, machine-readable EU official statistics with both:
1. **Query endpoints** (JSON-stat via Statistics API), and
2. **Discovery/update surfaces** (Catalogue TOC/DCAT/RSS + metabase refreshes).

That combination improves fast triage (what changed), reproducibility (exact filters), and baseline context (cross-country and regional comparisons).

## Quick operator notes

- Use **Statistics API** for compact reproducible pulls with explicit filters (`geo`, `time`, `sinceTimePeriod`, etc.).
- Use **Catalogue API** and RSS/DCAT feeds to monitor newly updated datasets and avoid stale-baseline analysis.
- Treat each indicator with its own publication/revision cadence; do not assume synchronized update timing across domains.

## Files updated

- `docs/datasets-catalog.md`

## Source links

- [Eurostat API data access (overview)](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started)
- [Eurostat Catalogue API (TOC/DCAT/RSS/metabase)](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/catalogue-api)
- [Eurostat API Statistics detailed guidelines](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics)
- [Example live JSON-stat query (`demo_pjan`)](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=DE&sex=T&age=TOTAL&unit=NR&sinceTimePeriod=2024)
