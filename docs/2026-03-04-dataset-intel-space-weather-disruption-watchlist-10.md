# Datasets: Space-weather disruption watchlist (NOAA SWPC added)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-04-dataset-intel-space-weather-disruption-watchlist-10.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-04-dataset-intel-space-weather-disruption-watchlist-10.md)

**Dateline:** 2026-03-04 03:08 UTC

## What changed this run (DATASETS_B)

Added a genuinely new dataset source to the catalog:

- **NOAA SWPC space weather data (JSON feeds)**  
  [https://services.swpc.noaa.gov/json/](https://services.swpc.noaa.gov/json/)

Catalog location updated: `docs/datasets-catalog.md` under a new section:
- **10) Space weather and geomagnetic disruption**

## Why this source is useful for OSINT

Space-weather claims (geomagnetic storms, flare impacts, navigation/comms disruptions) often spread quickly and mix forecast language with observed effects. SWPC feeds provide a primary open baseline for:

- observed/forecast geomagnetic indices
- flare and solar event timelines
- grounding claims about potential disruption windows

## Operational triage use

For space-weather claims, use this sequence:

1. **SWPC JSON products** for event timing/severity baseline
2. Sector-specific corroboration (aviation NOTAMs, grid operator notices, GNSS advisories)
3. Local impact confirmation before attributing outages directly to geomagnetic activity

## Source links

- [NOAA SWPC JSON directory](https://services.swpc.noaa.gov/json/)
- [SWPC products/alerts hub](https://www.swpc.noaa.gov/products)
- [Updated catalog page](https://carcipization.github.io/ai-osint/datasets-catalog.md)

## Bottom line

DATASETS_B requirement satisfied: catalog expanded with a new primary source that improves verification coverage for space-weather and infrastructure-disruption narratives.
