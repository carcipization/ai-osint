# Datasets Catalog

**Dateline:** 2026-03-01 06:01 UTC  
**Human-readable HTML:** [https://carcipization.github.io/ai-osint/datasets-catalog.html](https://carcipization.github.io/ai-osint/datasets-catalog.html)  
**LLM-friendly Markdown:** [https://carcipization.github.io/ai-osint/datasets-catalog.md](https://carcipization.github.io/ai-osint/datasets-catalog.md)

Compact inventory of high-value open datasets for AI-OSINT stories.

## Use rules (short)
- Prefer primary/public sources.
- Triangulate at least 2 independent sources for strong claims.
- Check cadence/lag before interpreting short-window moves.
- Treat media-derived and third-party aggregations as signals, not ground truth.

## Fast taxonomy
- **Near-real-time signals:** GDELT, OONI, USGS, FIRMS, ENTSO-E, AGSI+, OpenSky/ADS-B, AIS feeds
- **Structural baselines:** World Bank/IMF/FAOSTAT/WGI/ITU/OECD.AI
- **Conflict & humanitarian:** ACLED, UCDP GED, ICEWS, EM-DAT, ReliefWeb, UNHCR
- **Trade/energy/maritime:** UN Comtrade, Pink Sheet, GFW, IMO GISIS, Vortexa
- **Ownership/procurement:** OpenCorporates, OpenOwnership, Companies House PSC, USAspending, TED, Contracts Finder
- **AI capability/risk:** HELM, Epoch GPU clusters, AI Incident DB
- **Domestic crime/public safety:** FBI CDE, StatsCan, Chicago, Toronto MCI, Edmonton EPS

---

## 1) Conflict, unrest, and information control

### ACLED
- **URL:** [https://acleddata.com/](https://acleddata.com/)
- **Cadence:** Frequent
- **Good for:** Protest/conflict intensity shifts
- **Caveats:** Reporting lag and regional source bias

### UCDP GED
- **URL:** [https://ucdp.uu.se/downloads/](https://ucdp.uu.se/downloads/)
- **Cadence:** Periodic
- **Good for:** Historical conflict baselines; district-level escalation checks
- **Caveats:** Slower than live feeds

### ICEWS (Harvard Dataverse)
- **URL:** [https://dataverse.harvard.edu/dataverse/icews](https://dataverse.harvard.edu/dataverse/icews)
- **Cadence:** Batch/periodic
- **Good for:** Actor-interaction trend changes; pre-crisis signal testing
- **Caveats:** Machine-coded + media-dependent noise

### GDELT (Events + GKG)
- **URL:** [https://www.gdeltproject.org/data.html](https://www.gdeltproject.org/data.html)
- **Cadence:** Near real-time
- **Good for:** Early anomaly and narrative-shift detection
- **Caveats:** Media bias/language asymmetry; not ground truth

### OONI
- **URL:** [https://ooni.org/data/](https://ooni.org/data/)
- **Cadence:** Ongoing
- **Good for:** Corroborating censorship/shutdown claims
- **Caveats:** Probe coverage uneven; non-detection ≠ no interference

---

## 2) Humanitarian and disaster context

### ReliefWeb API
- **URL:** [https://api.reliefweb.int/](https://api.reliefweb.int/)
- **Cadence:** Frequent
- **Good for:** Situation-report timelines and incident clustering
- **Caveats:** Aggregated quality depends on upstream sources

### EM-DAT
- **URL:** [https://www.emdat.be/](https://www.emdat.be/)
- **Cadence:** Ongoing curated updates
- **Good for:** Cross-validating disaster impact severity
- **Caveats:** Impact estimates evolve over time

### UNHCR Refugee Data Finder
- **URL:** [https://www.unhcr.org/refugee-statistics/download/](https://www.unhcr.org/refugee-statistics/download/)
- **Cadence:** Regular (series-dependent)
- **Good for:** Displacement trend checks
- **Caveats:** Registration lag/revisions

### USGS Earthquake feeds
- **URL:** [https://earthquake.usgs.gov/earthquakes/feed/](https://earthquake.usgs.gov/earthquakes/feed/)
- **Cadence:** Near real-time
- **Good for:** Fast seismic context
- **Caveats:** Hazard signal only; causal claims require extra evidence

### NASA FIRMS
- **URL:** [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)
- **Cadence:** Near real-time/daily
- **Good for:** Fire hotspot anomalies
- **Caveats:** Sensor/cloud limitations; hotspot ≠ cause

### NOAA IBTrACS
- **URL:** [https://www.ncei.noaa.gov/products/international-best-track-archive](https://www.ncei.noaa.gov/products/international-best-track-archive)
- **Cadence:** Ongoing/periodic
- **Good for:** Cyclone hazard overlays for maritime/infrastructure stories
- **Caveats:** Cross-era comparability limits

### Copernicus CDS (ERA5)
- **URL:** [https://cds.climate.copernicus.eu/](https://cds.climate.copernicus.eu/)
- **Cadence:** Regular
- **Good for:** Weather/extreme claims vs historical baselines
- **Caveats:** Reanalysis resolution limits local inference

---

## 3) Energy, trade, and maritime

### UN Comtrade
- **URL:** [https://comtrade.un.org/](https://comtrade.un.org/)
- **Cadence:** Monthly/annual
- **Good for:** Commodity rerouting and sanctions-evasion pattern checks
- **Caveats:** Publication lag + mirror discrepancies

### World Bank Pink Sheet
- **URL:** [https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)
- **Cadence:** Monthly
- **Good for:** Commodity price-shock context
- **Caveats:** Benchmarks, not local retail prices

### AGSI+ (EU gas storage)
- **URL:** [https://agsi.gie.eu/](https://agsi.gie.eu/)
- **Cadence:** Daily/intraday
- **Good for:** Storage stress and drawdown anomalies
- **Caveats:** Storage level ≠ immediate outage risk

### ENTSO-E Transparency
- **URL:** [https://transparency.entsoe.eu/](https://transparency.entsoe.eu/)
- **Cadence:** Near real-time to daily
- **Good for:** Grid flow reversals, outages, generation shocks
- **Caveats:** Completeness/latency varies by TSO and product

### Global Fishing Watch
- **URL:** [https://globalfishingwatch.org/datasets-and-code/](https://globalfishingwatch.org/datasets-and-code/)
- **Cadence:** Product-dependent
- **Good for:** Vessel behavior shifts near disputed waters
- **Caveats:** AIS gaps/spoofing behavior

### IMO GISIS
- **URL:** [https://gisis.imo.org/](https://gisis.imo.org/)
- **Cadence:** Ongoing (module-dependent)
- **Good for:** Maritime safety/security incident context
- **Caveats:** Access/completeness varies

### Vortexa Freight Tracker
- **URL:** [https://www.vortexa.com/freight-tracker/](https://www.vortexa.com/freight-tracker/)
- **Cadence:** Frequent
- **Good for:** Tanker rerouting/chokepoint pressure
- **Caveats:** Commercial methodology/access limits

### MarineCadastre AccessAIS
- **URL:** [https://marinecadastre.gov/accessais/](https://marinecadastre.gov/accessais/)
- **Cadence:** Dataset-dependent
- **Good for:** US-focused vessel density/congestion analysis
- **Caveats:** US-centric; not global coverage

### AISHub API
- **URL:** [https://www.aishub.net/api](https://www.aishub.net/api)
- **Cadence:** Near real-time
- **Good for:** Vessel track monitoring
- **Caveats:** Coverage depends on contributor network/access plan

---

## 4) Aviation and mobility monitoring

### OpenSky Network
- **URL:** [https://opensky-network.org/data](https://opensky-network.org/data)
- **Cadence:** Continuous ingestion
- **Good for:** Flight-route anomalies and corridor pressure checks
- **Caveats:** Access/rate limits vary

### ADS-B Exchange
- **URL:** [https://www.adsbexchange.com/data/](https://www.adsbexchange.com/data/)
- **Cadence:** Near real-time + historical products
- **Good for:** Path reconstruction and traffic discontinuities
- **Caveats:** Commercial terms/endpoints can change

### ADSB.lol Open Data API
- **URL:** [https://www.adsb.lol/docs/open-data/api/](https://www.adsb.lol/docs/open-data/api/)
- **Cadence:** Near real-time + archives
- **Good for:** Redundant open-data triangulation
- **Caveats:** Community coverage uneven geographically

---

## 5) Economy, governance, and structural risk

### World Bank Indicators API
- **URL:** [https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- **Cadence:** Periodic by series
- **Good for:** Cross-country baseline construction
- **Caveats:** Revision/version handling required

### IMF Data API
- **URL:** [https://www.imf.org/external/datamapper/api/](https://www.imf.org/external/datamapper/api/)
- **Cadence:** Periodic by indicator
- **Good for:** Sovereign-risk and macro-stress consistency checks
- **Caveats:** Definition/lag differences across datasets

### FAOSTAT
- **URL:** [https://www.fao.org/faostat/en/](https://www.fao.org/faostat/en/)
- **Cadence:** Periodic/annual
- **Good for:** Food security and agricultural stress baselines
- **Caveats:** Not suitable for real-time inference

### ITU ICT indicators
- **URL:** [https://www.itu.int/en/ITU-D/Statistics/Pages/publications/wtid.aspx](https://www.itu.int/en/ITU-D/Statistics/Pages/publications/wtid.aspx)
- **Cadence:** Annual/periodic
- **Good for:** Digital dependency context for shutdown/censorship claims
- **Caveats:** Annual cadence

### Worldwide Governance Indicators (WGI)
- **URL:** [https://info.worldbank.org/governance/wgi/](https://info.worldbank.org/governance/wgi/)
- **Cadence:** Annual
- **Good for:** Institutional fragility context
- **Caveats:** Composite annual metrics, weak for short-term attribution

### OECD.AI
- **URL:** [https://oecd.ai/](https://oecd.ai/)
- **Cadence:** Periodic
- **Good for:** Cross-country AI policy/ecosystem context
- **Caveats:** Composite indicator sensitivity

### SIPRI Milex
- **URL:** [https://www.sipri.org/databases/milex](https://www.sipri.org/databases/milex)
- **Cadence:** Annual
- **Good for:** Defense spending trajectory checks
- **Caveats:** Cross-country accounting comparability issues

---

## 6) Ownership, sanctions, and procurement

### OpenSanctions
- **URL:** [https://www.opensanctions.org/datasets/](https://www.opensanctions.org/datasets/)
- **Cadence:** Frequent
- **Good for:** Designation-wave and entity-network monitoring
- **Caveats:** Verify high-stakes claims against originating authorities

### OpenCorporates API
- **URL:** [https://api.opencorporates.com/](https://api.opencorporates.com/)
- **Cadence:** Ongoing
- **Good for:** Entity resolution and corporate linkage mapping
- **Caveats:** Jurisdiction depth/latency uneven

### Open Ownership Register (BODS)
- **URL:** [https://register.openownership.org/](https://register.openownership.org/)
- **Cadence:** Regular republish
- **Good for:** Beneficial ownership-chain reconstruction
- **Caveats:** Coverage heterogeneity by country

### UK Companies House PSC bulk
- **URL:** [https://download.companieshouse.gov.uk/en_pscdata.html](https://download.companieshouse.gov.uk/en_pscdata.html)
- **Cadence:** Snapshot releases
- **Good for:** UK ownership-change analysis
- **Caveats:** Filing behavior and snapshot timing effects

### USAspending API
- **URL:** [https://api.usaspending.gov/](https://api.usaspending.gov/)
- **Cadence:** Regular
- **Good for:** Vendor concentration and agency spend shifts
- **Caveats:** Obligation vs outlay interpretation traps

### TED Open Data/API (EU procurement)
- **URL:** [https://data.ted.europa.eu/](https://data.ted.europa.eu/)
- **Cadence:** Ongoing
- **Good for:** Cross-country procurement trend analysis
- **Caveats:** Taxonomy/format transitions need normalization

### UK Contracts Finder API
- **URL:** [https://www.contractsfinder.service.gov.uk/apidocumentation](https://www.contractsfinder.service.gov.uk/apidocumentation)
- **Cadence:** Ongoing
- **Good for:** UK award/opportunity monitoring
- **Caveats:** Field completeness varies by authority

---

## 7) AI capability, risk, and incidents

### Stanford HELM
- **URL:** [https://crfm.stanford.edu/helm/](https://crfm.stanford.edu/helm/)
- **Cadence:** Periodic
- **Good for:** Capability/safety benchmark tracking
- **Caveats:** Protocol changes can mimic jumps

### Epoch AI GPU Clusters
- **URL:** [https://epoch.ai/data/gpu-clusters](https://epoch.ai/data/gpu-clusters)
- **Cadence:** Periodic
- **Good for:** Compute concentration and frontier buildout tracking
- **Caveats:** Public-disclosure bias; not exhaustive

### AI Incident Database (AIAAIC)
- **URL:** [https://incidentdatabase.ai/](https://incidentdatabase.ai/)
- **Cadence:** Ongoing
- **Good for:** Reported AI incident trend monitoring
- **Caveats:** Not exhaustive; public-reporting dependent

---

## 8) Domestic crime and public safety (US/Canada)

### FBI CDE / UCR
- **URL:** [https://cde.ucr.cjis.gov/](https://cde.ucr.cjis.gov/)
- **Cadence:** Periodic
- **Good for:** US crime baseline comparisons
- **Caveats:** Participation and category-comparability shifts

### StatsCan
- **URL:** [https://www.statcan.gc.ca/](https://www.statcan.gc.ca/)
- **Cadence:** Table-dependent
- **Good for:** Canadian baseline trend checks
- **Caveats:** Release lag and table revisions

### Chicago Crimes (2001–present)
- **URL:** [https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- **Cadence:** Frequent
- **Good for:** District/category anomaly tracking
- **Caveats:** Backfills and reclassification changes

### Toronto MCI
- **URL:** [https://open.toronto.ca/dataset/major-crime-indicators/](https://open.toronto.ca/dataset/major-crime-indicators/)
- **Cadence:** Periodic
- **Good for:** Neighbourhood-level trend checks
- **Caveats:** Reporting conventions differ from US systems

### Edmonton EPS Neighbourhood Criminal Occurrences
- **URL:** [https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)
- **Cadence:** Monthly
- **Good for:** Sub-city Canadian outlier detection
- **Caveats:** Local definitions differ across municipalities

---

## 9) Telegram/public-channel analytics

### TGStat API
- **URL:** [https://tgstat.com/api/stat](https://tgstat.com/api/stat)
- **Cadence:** Frequent
- **Good for:** Public-channel growth/citation monitoring
- **Caveats:** Third-party methodology/coverage dependence

### Telemetr API
- **URL:** [https://api.telemetr.io/](https://api.telemetr.io/)
- **Cadence:** Frequent
- **Good for:** Cross-channel benchmarking
- **Caveats:** Terms/pricing/coverage can change

### TGDataset (research corpus)
- **URL:** [https://github.com/SystemsLab-Sapienza/TGDataset](https://github.com/SystemsLab-Sapienza/TGDataset)
- **Cadence:** Snapshot releases
- **Good for:** Historical network baseline research
- **Caveats:** Not a live operational feed
