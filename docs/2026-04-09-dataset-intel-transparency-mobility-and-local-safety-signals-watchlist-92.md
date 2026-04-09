# Datasets: transparency, mobility, and local safety signals (watchlist 92)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-09-dataset-intel-transparency-mobility-and-local-safety-signals-watchlist-92.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-09-dataset-intel-transparency-mobility-and-local-safety-signals-watchlist-92.md)

**Dateline:** 2026-04-09 09:56 UTC

This dataset cycle adds five net-new machine-readable sources focused on public-facing accountability and day-to-day service reliability: corporate filing churn, transit disruption pressure, and local public-safety trend baselines. Together, they improve early detection of operational stress that non-specialist audiences can act on (commute planning, local risk posture, and governance oversight).

## Added datasets (5)

1. **[Corporations and Other Entities: All Filings](https://catalog.data.gov/dataset/corporations-and-other-entities-all-filings)**  
   New York State filing-level corporate records (formation, amendment, status events) that help track entity churn and governance stress around employers, contractors, and service providers.

2. **[MTA Subway Major Incidents: Beginning 2015](https://catalog.data.gov/dataset/mta-subway-major-incidents-beginning-2015)**  
   Major-incident records for New York City subway operations that support quick checks on mobility disruptions with direct commuter and emergency-access consequences.

3. **[MTA Bus Speeds: Beginning 2015](https://catalog.data.gov/dataset/mta-bus-speeds-beginning-2015)**  
   Corridor-level speed histories for NYC buses, useful for identifying slowdowns that materially change commute reliability and neighborhood service access.

4. **[Index Crimes by County and Agency: Beginning 1990](https://catalog.data.gov/dataset/index-crimes-by-county-and-agency-beginning-1990)**  
   Long-run county/agency crime baselines for New York State, useful for separating short-term noise from structural safety trend shifts.

5. **[APD Arrests](https://catalog.data.gov/dataset/apd-arrests)**  
   Austin arrest records that add a high-cadence local enforcement pressure signal for detention, court, and community-service load context.

## Why this matters now

- **Accountability + service continuity:** corporate filing events can surface entity instability before downstream labor or service effects are obvious.
- **Mobility consequence:** transit incident and speed datasets convert broad “system strain” narratives into measurable route/corridor impacts.
- **Safety decision utility:** long-run and high-frequency local crime/arrest datasets support faster checks of whether public-safety shifts are transient or persistent.

## Caveats

- Several additions are **city/state scoped**, so they should be used as operational local indicators, not national generalizations.
- Incident/arrest and filing systems can include **reporting lags, recoding, and policy-definition changes**; trend interpretation should use stable windows and metadata notes.
- Transit speed and major-incident fields are sensitive to schedule and classification changes; cross-period comparisons need denominator discipline.

## Appendix: Sources

- data.gov dataset metadata and API endpoints listed above.
- Updated catalog entry file: `docs/datasets-catalog.md`.
