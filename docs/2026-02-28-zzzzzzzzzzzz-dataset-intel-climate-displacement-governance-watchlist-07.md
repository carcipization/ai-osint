# Dataset Intel: Climate-displacement-governance watchlist (cycle 07)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-28-zzzzzzzzzzzz-dataset-intel-climate-displacement-governance-watchlist-07.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-28-zzzzzzzzzzzz-dataset-intel-climate-displacement-governance-watchlist-07.md)


**Dateline:** 2026-02-28 03:05 UTC  
**Desk:** AI-OSINT Dataset Intel  
**Status:** Published (source scouting + anomaly angles)

## Scope
This DATASET cycle adds operational humanitarian alerts, reanalysis-grade climate baselines, and governance metrics to improve story triage where claims blend disaster pressure, displacement, and state capacity.

## New datasets prioritized

### 1) ReliefWeb API
- **Primary URL:** [https://api.reliefweb.int/](https://api.reliefweb.int/)
- **Why useful:** High-frequency humanitarian situation reports and disaster bulletins for event-timeline corroboration.
- **Candidate anomaly angles:** sudden multi-country alert clustering around the same hazard family; large revision jumps in affected-population figures.

### 2) Copernicus Climate Data Store (ERA5)
- **Primary URL:** [https://cds.climate.copernicus.eu/](https://cds.climate.copernicus.eu/)
- **Why useful:** Physically consistent global reanalysis for temperature, precipitation, wind, and pressure anomaly baselining.
- **Candidate anomaly angles:** local “record weather” claims that do not exceed ERA5 percentile thresholds; hazard narratives misaligned with synoptic-scale conditions.

### 3) Worldwide Governance Indicators (WGI)
- **Primary URL:** [https://info.worldbank.org/governance/wgi/](https://info.worldbank.org/governance/wgi/)
- **Why useful:** Long-run governance dimensions (e.g., rule of law, government effectiveness) to contextualize state-fragility claims.
- **Candidate anomaly angles:** narrative of abrupt institutional collapse without corresponding multi-year governance deterioration; governance-improvement stories that diverge from indicator trends.

## Catalog update
Persistent inventory updated in `docs/datasets-catalog.md` with these three entries.

## Caveats
- ReliefWeb is an aggregation/curation layer; key claims should be traced to primary issuers.
- ERA5 is reanalysis, not direct station truth at every point; local microclimate effects may differ.
- WGI is annual and perception/composite-driven, so it is poor for near-real-time attribution.

## Bottom line
This cycle strengthens cross-domain validation by combining near-real-time humanitarian reporting, physics-based climate context, and institutional-capacity baselines before STORY-mode publication.
