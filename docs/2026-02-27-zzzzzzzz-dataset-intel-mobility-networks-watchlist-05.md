# Dataset Intel: Mobility, ownership, procurement, and Telegram-network watchlist (off-cycle 05)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzz-dataset-intel-mobility-networks-watchlist-05.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzz-dataset-intel-mobility-networks-watchlist-05.md)

**Dateline:** 2026-02-27 00:00 UTC  
**Desk:** AI-OSINT Dataset Intel  
**Status:** Published (off-cycle expansion)

## Scope
Off-cycle expansion requested to add 2-3 practical dataset examples for each of five priority dataset types:
1) ADS-B flight tracks, 2) AIS maritime tracking, 3) corporate + beneficial ownership, 4) procurement/contract awards, 5) Telegram channel graph/metadata.

## New datasets prioritized

## 1) ADS-B flight tracks

### OpenSky Network Data
- **Primary URL:** [[https://opensky-network.org/data](https://opensky-network.org/data)](https://opensky-network.org/data)
- **Why useful:** High-value source for research-grade flight telemetry access (real-time + historical workflows).
- **Candidate anomaly angles:** sanctioned-tail-number routing shifts; abnormal military/government traffic concentration by corridor.

### ADS-B Exchange Data & Historical Products
- **Primary URL:** [[https://www.adsbexchange.com/data/](https://www.adsbexchange.com/data/)](https://www.adsbexchange.com/data/)
- **Why useful:** Broad unfiltered flight-tracking coverage with historical retrieval options.
- **Candidate anomaly angles:** sudden disappearance/reappearance patterns; reroutes around conflict or airspace closures.

### ADSB.lol Open Data API
- **Primary URL:** [[https://www.adsb.lol/docs/open-data/api/](https://www.adsb.lol/docs/open-data/api/)](https://www.adsb.lol/docs/open-data/api/)
- **Why useful:** Community-driven open API and historical archives useful for rapid prototyping and triangulation.
- **Candidate anomaly angles:** emergency/diversion spikes; unusual private-jet bridge patterns between hubs.

## 2) AIS maritime tracking

### MarineCadastre AccessAIS (US-focused AIS)
- **Primary URL:** [[https://marinecadastre.gov/accessais/](https://marinecadastre.gov/accessais/)](https://marinecadastre.gov/accessais/)
- **Why useful:** Downloadable authoritative AIS vessel traffic data products for US waters and approaches.
- **Candidate anomaly angles:** chokepoint queue expansion; abnormal loitering near infrastructure.

### AISHub API
- **Primary URL:** [[https://www.aishub.net/api](https://www.aishub.net/api)](https://www.aishub.net/api)
- **Why useful:** Aggregated AIS feed access in API formats for monitoring vessel behavior over time.
- **Candidate anomaly angles:** transponder silence clusters; abrupt route deviations by vessel class.

### Global Fishing Watch datasets/code
- **Primary URL:** [[https://globalfishingwatch.org/datasets-and-code/](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)
- **Why useful:** AIS-derived vessel behavior layers with strong maritime analytics context.
- **Candidate anomaly angles:** suspicious activity collapse/shift near disputed waters; effort spikes near EEZ boundaries.

## 3) Corporate registry + beneficial ownership

### OpenCorporates API
- **Primary URL:** [[https://api.opencorporates.com/](https://api.opencorporates.com/)](https://api.opencorporates.com/)
- **Why useful:** Broad multi-jurisdiction company registry aggregation with source provenance.
- **Candidate anomaly angles:** rapid director/officer reshuffles before sanctions/enforcement events.

### Open Ownership Register (BODS)
- **Primary URL:** [[https://register.openownership.org/](https://register.openownership.org/)](https://register.openownership.org/)
- **Why useful:** Structured beneficial-ownership graph data using BODS for cross-entity linkage.
- **Candidate anomaly angles:** layered beneficial-owner changes before major contract awards.

### UK Companies House PSC snapshot
- **Primary URL:** [[https://download.companieshouse.gov.uk/en_pscdata.html](https://download.companieshouse.gov.uk/en_pscdata.html)](https://download.companieshouse.gov.uk/en_pscdata.html)
- **Why useful:** Bulk beneficial-ownership disclosures for UK entities.
- **Candidate anomaly angles:** concentration of control updates in specific sectors or shell clusters.

## 4) Procurement/contract awards

### USAspending API
- **Primary URL:** [[https://api.usaspending.gov/](https://api.usaspending.gov/)](https://api.usaspending.gov/)
- **Why useful:** Detailed federal awards/contract data with robust filtering and agency/recipient views.
- **Candidate anomaly angles:** sudden award concentration into new vendors; outlier contract growth by NAICS/agency.

### TED Open Data + TED API (EU)
- **Primary URL:** [[https://data.ted.europa.eu/](https://data.ted.europa.eu/)](https://data.ted.europa.eu/)  
- **API docs:** [[https://docs.ted.europa.eu/api/latest/index.html](https://docs.ted.europa.eu/api/latest/index.html)](https://docs.ted.europa.eu/api/latest/index.html)
- **Why useful:** Pan-EU public procurement notices and linked structured access.
- **Candidate anomaly angles:** synchronized procurement surges across member states in strategic sectors.

### UK Contracts Finder API
- **Primary URL:** [[https://www.contractsfinder.service.gov.uk/apidocumentation](https://www.contractsfinder.service.gov.uk/apidocumentation)](https://www.contractsfinder.service.gov.uk/apidocumentation)
- **Why useful:** UK contract notices and award metadata for domestic procurement monitoring.
- **Candidate anomaly angles:** repeated winner patterns below headline thresholds; geographic spend clustering.

## 5) Telegram channel graph + message metadata (public channels)

### TGStat Statistics API
- **Primary URL:** [[https://tgstat.com/api/stat](https://tgstat.com/api/stat)](https://tgstat.com/api/stat)
- **Why useful:** Channel-level growth, reach, and citation-style indicators useful for network mapping.
- **Candidate anomaly angles:** coordinated growth bursts across related channels; citation-ring behavior.

### Telemetr public API
- **Primary URL:** [[https://api.telemetr.io/](https://api.telemetr.io/)](https://api.telemetr.io/)
- **Why useful:** Large channel analytics index useful for cross-channel comparison and trend monitoring.
- **Candidate anomaly angles:** engagement discontinuities around narrative campaigns.

### TGDataset research corpus (Sapienza)
- **Primary URL:** [[https://github.com/SystemsLab-Sapienza/TGDataset](https://github.com/SystemsLab-Sapienza/TGDataset)](https://github.com/SystemsLab-Sapienza/TGDataset)
- **Why useful:** Large public-channel research dataset for structural graph experiments and historical modeling.
- **Candidate anomaly angles:** centrality shifts and bridge-channel emergence across language communities.

## Caveats
- Coverage and licensing vary widely; production use should validate terms per source.
- Aggregator datasets can inherit reporting/selection bias from upstream feeds.
- Telegram analyses should stay on public-channel data and avoid privacy-invasive collection patterns.
- Cross-platform anomalies should be treated as hypotheses until independently corroborated.

## Catalog update
Persistent inventory updated in `docs/datasets-catalog.md` with all sources above under this off-cycle section.

## Bottom line
This off-cycle package materially expands transport-network, ownership-network, spend-network, and public Telegram-network observability—improving pre-story anomaly detection and cross-domain corroboration.