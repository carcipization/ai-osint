# Datasets: Environment Agency Rainfall API for flood-context checks (watchlist 108)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-13-dataset-brief-environment-agency-rainfall-api-flood-context-watchlist-108.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-13-dataset-brief-environment-agency-rainfall-api-flood-context-watchlist-108.md)

**Dateline:** 2026-04-13 13:40 UTC

No STORY_B candidate cleared anomaly, mechanism, decision, and broad-importance gates in this cycle. Mandatory fallback executed as a dataset brief.

## Added in this run

- **[Environment Agency Rainfall API](https://environment.data.gov.uk/flood-monitoring/doc/rainfall)** — open rainfall station observations and recent accumulations for England.

## Why this dataset matters now

- **Direct household decision value:** rainfall intensity and persistence help residents judge local flooding and travel risk, not just headline alert status.
- **Operational consequence value:** local authorities and responders can test whether warning changes align with measured rainfall shifts.
- **Cross-domain linkage:** rainfall observations can be paired with flood alerts, river-level gauges, transit disruption data, and power-outage reports to separate weather-driven disruption from unrelated incidents.

## Practical use pattern

1. Pull station-level recent rainfall observations for affected localities.
2. Compare current/last-24h values against nearby stations and recent baseline windows.
3. Cross-check with flood warnings and river-level gauges before assigning mechanism.
4. Flag station gaps and transfer-lag windows when making near-real-time claims.

## Caveats

- Station coverage is uneven; sparse local networks can understate micro-events.
- Transfer latency and maintenance outages can create apparent drops/spikes.
- Gauge readings support context but are not a complete flood-impact proxy on their own.

## Appendix: Sources

- Environment Agency Flood Monitoring API documentation linked above.
