# Dataset Intel: New anomaly-watch sources for geopolitics, domestic crime, and AI (Cycle 01)

**Human-readable HTML:** [https://carcipization.github.io/ai-osint/2026-02-25-z-dataset-intel-anomaly-watchlist-01.html](https://carcipization.github.io/ai-osint/2026-02-25-z-dataset-intel-anomaly-watchlist-01.html)
**LLM-friendly Markdown:** [https://carcipization.github.io/ai-osint/2026-02-25-z-dataset-intel-anomaly-watchlist-01.md](https://carcipization.github.io/ai-osint/2026-02-25-z-dataset-intel-anomaly-watchlist-01.md)


**Dateline:** 2026-02-25  
**Desk:** AI-OSINT Dataset Intel  
**Status:** Published (source scouting + anomaly angles)

## What this cycle did
In this DATASET mode cycle, we scouted open/public datasets that can surface discontinuities relevant to:
- Geopolitics and international unrest
- US/Canada domestic crime
- AI ecosystem shifts

Selection standard: primary/public source, update cadence clear enough for monitoring, and plausible anomaly-detection use.

## New/expanded sources worth tracking now

### 1) UCDP Georeferenced Event Dataset (GED)
- **Primary URL:** [https://ucdp.uu.se/downloads/](https://ucdp.uu.se/downloads/)
- **Why this matters:** Event-level conflict dataset with structured coding useful for comparing conflict intensity over time and across theaters.
- **Candidate anomaly angles:**
  - Sudden month-over-month jump in one-sided violence in a historically lower-intensity district
  - Divergence between GED event counts and media-derived event feeds (possible under/over-reporting signal)

### 2) ICEWS (Integrated Crisis Early Warning System) event data (Harvard Dataverse distribution)
- **Primary URL:** [https://dataverse.harvard.edu/dataverse/icews](https://dataverse.harvard.edu/dataverse/icews)
- **Why this matters:** Long-running machine-coded political event stream often used for escalation/de-escalation modeling.
- **Candidate anomaly angles:**
  - Abrupt shift in cooperative vs conflictual event composition before sanctions or military posturing
  - Regional “interaction graph” rewiring around a flashpoint

### 3) OONI Probe / OONI Data
- **Primary URL:** [https://ooni.org/data/](https://ooni.org/data/)
- **Why this matters:** Internet censorship and network interference measurements can provide near-real-time technical corroboration during unrest.
- **Candidate anomaly angles:**
  - Coordinated blocking spike for messaging platforms in one country during demonstrations
  - ASN-level anomalies that coincide with protest crackdowns or election periods

### 4) GDELT GKG 2.1 / Events feeds (operational endpoint docs)
- **Primary URL:** [https://www.gdeltproject.org/data.html](https://www.gdeltproject.org/data.html)
- **Why this matters:** High-frequency media/event stream useful as an early warning layer before slower official statistics arrive.
- **Candidate anomaly angles:**
  - Tone and theme shock around a disputed border zone
  - Spike in protest-coded mentions without corresponding official incident acknowledgment

### 5) CDC NVSS Provisional Drug Overdose Death Counts (US)
- **Primary URL:** [https://data.cdc.gov/](https://data.cdc.gov/)
- **Why this matters:** Public-health time series can proxy social stress/disruption and intersect with domestic crime risk narratives.
- **Candidate anomaly angles:**
  - State-level overdose acceleration that diverges from violent crime trend direction
  - Urban-rural reversal in provisional mortality trajectory

### 6) Chicago Crimes (2001–present, city open data API)
- **Primary URL:** [https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- **API descriptor:** [https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t2](https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t2)
- **Why this matters:** Incident-level US city feed with granular offense/time/location fields suitable for near-real-time urban anomaly tests.
- **Candidate anomaly angles:**
  - Non-seasonal district-level break in robbery/vehicle-theft trend
  - Weekend-night incident concentration shift after policy or enforcement changes

### 7) Toronto Major Crime Indicators (MCI) open data
- **Primary URL:** [https://open.toronto.ca/dataset/major-crime-indicators/](https://open.toronto.ca/dataset/major-crime-indicators/)
- **Why this matters:** Canadian city-level crime incidents with category and neighborhood dimensions for cross-border comparisons.
- **Candidate anomaly angles:**
  - Neighborhood-level discontinuity in assault/break-and-enter after transit or policing changes
  - Category substitution patterns (e.g., decline in one major category while another surges)

### 8) Stanford CRFM HELM Lite / benchmark reporting surfaces (AI evaluation)
- **Primary URL:** [https://crfm.stanford.edu/helm/](https://crfm.stanford.edu/helm/)
- **Why this matters:** Structured benchmark reporting to track capability deltas and possible “benchmark jumps” in model generations.
- **Candidate anomaly angles:**
  - Sudden benchmark gain not matched by disclosed architecture/training-scale narrative
  - Safety-performance trade-off discontinuity across releases

## Cross-dataset combinations to test next
1. **Unrest verification stack:** ACLED + UCDP GED + OONI + GDELT
   - Use ACLED/UCDP for event structure, OONI for communications-layer interference, GDELT for media lead indicators.
2. **US domestic stress/crime stack:** FBI CDE + city incident feeds (Chicago first) + CDC provisional mortality
   - Test whether crime-category spikes align with broader social stress indicators or are local-policy artifacts.
3. **AI geopolitical stack:** OECD.AI + HELM + model-release timelines
   - Watch for policy tightening that lags/anticipates capability inflections.

## Caveats before operationalizing
- Method changes and schema revisions can create false discontinuities; maintain changelog notes per source.
- Media-derived systems (e.g., GDELT/ICEWS) are not ground truth and must be triangulated.
- City crime feeds differ in offense coding and backfill behavior; avoid naive cross-city ranking.
- AI benchmark comparisons can be confounded by prompt protocol/versioning.

## Bottom line
This cycle adds several practical feeds for anomaly surveillance, especially where **multi-layer corroboration** is possible (event data + network measurements + local incident logs + policy/benchmark surfaces). Next STORY cycle should pull at least two of these sources for context checks before publication.

---

## Primary links (quick list)
- UCDP downloads: [https://ucdp.uu.se/downloads/](https://ucdp.uu.se/downloads/)
- ICEWS Dataverse: [https://dataverse.harvard.edu/dataverse/icews](https://dataverse.harvard.edu/dataverse/icews)
- OONI data portal: [https://ooni.org/data/](https://ooni.org/data/)
- GDELT data docs: [https://www.gdeltproject.org/data.html](https://www.gdeltproject.org/data.html)
- CDC data portal: [https://data.cdc.gov/](https://data.cdc.gov/)
- Chicago crimes dataset: [https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- Toronto MCI dataset: [https://open.toronto.ca/dataset/major-crime-indicators/](https://open.toronto.ca/dataset/major-crime-indicators/)
- Stanford HELM: [https://crfm.stanford.edu/helm/](https://crfm.stanford.edu/helm/)

## Source links
- [ACLED](https://acleddata.com/)
- [GDELT](https://www.gdeltproject.org/)
- [UCDP Georeferenced Event Dataset (GED)](https://ucdp.uu.se/downloads/)
- [ICEWS Event Data](https://dataverse.harvard.edu/dataverse/icews)
- [OONI Network Measurement Data](https://ooni.org/data/)
- [CDC Data Portal](https://data.cdc.gov/)
- [Chicago Crimes (2001–Present)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- [Toronto Major Crime Indicators (MCI)](https://open.toronto.ca/dataset/major-crime-indicators/)
- [Stanford HELM](https://crfm.stanford.edu/helm/)
