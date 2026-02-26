# Datasets Catalog

**Human-readable HTML:** [[[[[[https://carcipization.github.io/ai-osint/datasets-catalog.html](https://carcipization.github.io/ai-osint/datasets-catalog.html)](https://carcipization.github.io/ai-osint/datasets-catalog.html)](https://carcipization.github.io/ai-osint/datasets-catalog.html)](https://carcipization.github.io/ai-osint/datasets-catalog.html)](https://carcipization.github.io/ai-osint/datasets-catalog.html)](https://carcipization.github.io/ai-osint/datasets-catalog.html)
**LLM-friendly Markdown:** [[[[[[https://carcipization.github.io/ai-osint/datasets-catalog.md](https://carcipization.github.io/ai-osint/datasets-catalog.md)](https://carcipization.github.io/ai-osint/datasets-catalog.md)](https://carcipization.github.io/ai-osint/datasets-catalog.md)](https://carcipization.github.io/ai-osint/datasets-catalog.md)](https://carcipization.github.io/ai-osint/datasets-catalog.md)](https://carcipization.github.io/ai-osint/datasets-catalog.md)


Persistent inventory of open datasets/time-series sources to support AI-OSINT stories.

## How to use this file
- Keep entries concise and practical.
- Prioritize primary/public sources.
- Update when new datasets are discovered or caveats change.
- In STORY mode, consult this list for corroboration, anomaly checks, and context.

## Entry template
- **Name:**
- **URL:**
- **Coverage:** (geo + timeframe)
- **Cadence:** (real-time/daily/weekly/monthly)
- **Topic tags:**
- **Good for:**
- **Caveats:**
- **Story-use ideas:**

---

## Seed entries

### ACLED (Armed Conflict Location & Event Data)
- **URL:** [[[[[[https://acleddata.com/](https://acleddata.com/)](https://acleddata.com/)](https://acleddata.com/)](https://acleddata.com/)](https://acleddata.com/)](https://acleddata.com/)
- **Coverage:** Global conflict/unrest events (country-level availability varies)
- **Cadence:** Frequent updates
- **Topic tags:** geopolitics, unrest, conflict
- **Good for:** Detecting spikes in protests, violence, and conflict-event shifts
- **Caveats:** Methodology definitions matter; reporting lag and source bias by region
- **Story-use ideas:** "Protest intensity in X region jumps Y% week-over-week"

### GDELT Events
- **URL:** [[[[[[https://www.gdeltproject.org/](https://www.gdeltproject.org/)](https://www.gdeltproject.org/)](https://www.gdeltproject.org/)](https://www.gdeltproject.org/)](https://www.gdeltproject.org/)](https://www.gdeltproject.org/)
- **Coverage:** Global media-derived event signals
- **Cadence:** Near real-time
- **Topic tags:** geopolitics, unrest, media signals
- **Good for:** Early-change detection and narrative shifts across regions/topics
- **Caveats:** Media-coverage bias; not a direct ground-truth dataset
- **Story-use ideas:** "Media event-code surge preceded policy move"

### USGS Earthquake Catalog
- **URL:** [[[[[[https://earthquake.usgs.gov/earthquakes/feed/](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)
- **Coverage:** Global seismic events
- **Cadence:** Near real-time feeds
- **Topic tags:** disaster, infrastructure risk
- **Good for:** Rapid hazard context for geopolitical/infrastructure stories
- **Caveats:** Natural hazard data; relevance to political stories is contextual
- **Story-use ideas:** "Clustered seismic events near critical infrastructure"

### NASA FIRMS (Fire Information for Resource Management System)
- **URL:** [[[[[[https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)](https://firms.modaps.eosdis.nasa.gov/)](https://firms.modaps.eosdis.nasa.gov/)](https://firms.modaps.eosdis.nasa.gov/)](https://firms.modaps.eosdis.nasa.gov/)](https://firms.modaps.eosdis.nasa.gov/)
- **Coverage:** Global fire hotspots from satellite detections
- **Cadence:** Near real-time/daily products
- **Topic tags:** environment, conflict context, disruption
- **Good for:** Detecting unusual fire concentration changes by region
- **Caveats:** Cloud cover/sensor limits; hotspot ≠ confirmed incident cause
- **Story-use ideas:** "Unexpected hotspot spike in region under unrest"

### StatsCan Crime data portal
- **URL:** [[[[[[https://www.statcan.gc.ca/](https://www.statcan.gc.ca/)](https://www.statcan.gc.ca/)](https://www.statcan.gc.ca/)](https://www.statcan.gc.ca/)](https://www.statcan.gc.ca/)](https://www.statcan.gc.ca/) (datasets vary by table)
- **Coverage:** Canada domestic statistics incl. crime tables
- **Cadence:** Monthly/quarterly/annual depending table
- **Topic tags:** domestic-crime, canada
- **Good for:** Baseline trends and regional crime discontinuities in Canada
- **Caveats:** Release lag; table definitions/revisions
- **Story-use ideas:** "Category-level divergence across provinces"

### FBI CDE / UCR resources
- **URL:** [[[[[[https://cde.ucr.cjis.gov/](https://cde.ucr.cjis.gov/)](https://cde.ucr.cjis.gov/)](https://cde.ucr.cjis.gov/)](https://cde.ucr.cjis.gov/)](https://cde.ucr.cjis.gov/)](https://cde.ucr.cjis.gov/)
- **Coverage:** US crime reporting datasets/dashboards
- **Cadence:** Periodic releases
- **Topic tags:** domestic-crime, us
- **Good for:** US national/regional crime trend comparisons
- **Caveats:** Reporting participation changes; category comparability over time
- **Story-use ideas:** "Outlier metro trend compared to national baseline"

### OECD.AI Policy Observatory / indicators
- **URL:** [[[[[[https://oecd.ai/](https://oecd.ai/)](https://oecd.ai/)](https://oecd.ai/)](https://oecd.ai/)](https://oecd.ai/)](https://oecd.ai/)
- **Coverage:** AI policy, ecosystem, and country indicators
- **Cadence:** Periodic updates
- **Topic tags:** ai, policy, geopolitics
- **Good for:** Cross-country AI policy and capability context
- **Caveats:** Some metrics are composite and methodology-sensitive
- **Story-use ideas:** "Policy change vs investment/compute signal mismatch"

---

## Additions (2026-02-25 DATASET cycle)

### UCDP Georeferenced Event Dataset (GED)
- **URL:** [[[[[[https://ucdp.uu.se/downloads/](https://ucdp.uu.se/downloads/)](https://ucdp.uu.se/downloads/)](https://ucdp.uu.se/downloads/)](https://ucdp.uu.se/downloads/)](https://ucdp.uu.se/downloads/)](https://ucdp.uu.se/downloads/)
- **Coverage:** Global organized violence event data; long historical span with geo/event detail
- **Cadence:** Periodic releases
- **Topic tags:** geopolitics, conflict, unrest
- **Good for:** Conflict intensity discontinuities, district-level escalation checks, cross-feed validation with ACLED/GDELT
- **Caveats:** Release cadence slower than near-real-time feeds; coding changes/version notes must be tracked
- **Story-use ideas:** "Is a local flare-up a true structural escalation or a transient reporting spike?"

### ICEWS Event Data (Harvard Dataverse)
- **URL:** [[[[[[https://dataverse.harvard.edu/dataverse/icews](https://dataverse.harvard.edu/dataverse/icews)](https://dataverse.harvard.edu/dataverse/icews)](https://dataverse.harvard.edu/dataverse/icews)](https://dataverse.harvard.edu/dataverse/icews)](https://dataverse.harvard.edu/dataverse/icews)](https://dataverse.harvard.edu/dataverse/icews)
- **Coverage:** Global machine-coded political events; long-run historical/event-actor structure
- **Cadence:** Batch/periodic updates via repository releases
- **Topic tags:** geopolitics, early-warning, event-data
- **Good for:** Regime interaction shifts, cooperation-vs-conflict balance changes, pre-crisis signal testing
- **Caveats:** Machine-coding and media-source dependence can inject bias/noise; requires triangulation
- **Story-use ideas:** "Did diplomatic hostility metrics jump before sanctions or kinetic action?"

### OONI Network Measurement Data
- **URL:** [[[[[[https://ooni.org/data/](https://ooni.org/data/)](https://ooni.org/data/)](https://ooni.org/data/)](https://ooni.org/data/)](https://ooni.org/data/)](https://ooni.org/data/)
- **Coverage:** Global internet censorship/interference measurements from distributed probes
- **Cadence:** Frequent/ongoing submissions
- **Topic tags:** censorship, unrest, infrastructure, geopolitics
- **Good for:** Technical corroboration of shutdowns/platform blocking during protests/elections/conflicts
- **Caveats:** Probe coverage varies by country/ASN; non-detections are not definitive evidence of no interference
- **Story-use ideas:** "Did messaging-platform blocking coincide with street mobilization windows?"

### GDELT Data Feeds (Events + GKG)
- **URL:** [[[[[[https://www.gdeltproject.org/data.html](https://www.gdeltproject.org/data.html)](https://www.gdeltproject.org/data.html)](https://www.gdeltproject.org/data.html)](https://www.gdeltproject.org/data.html)](https://www.gdeltproject.org/data.html)](https://www.gdeltproject.org/data.html)
- **Coverage:** Global media-derived events/themes/tone; high-frequency updates
- **Cadence:** Near real-time (multiple updates per hour)
- **Topic tags:** geopolitics, unrest, media-signals
- **Good for:** Early anomaly surfacing and narrative-shift detection before official statistics publish
- **Caveats:** Media-coverage bias and language asymmetries; not direct ground truth
- **Story-use ideas:** "Theme/tone shock appears before official acknowledgement of an incident cluster"

### CDC Data Portal (incl. NVSS Provisional Overdose series)
- **URL:** [[[[[[https://data.cdc.gov/](https://data.cdc.gov/)](https://data.cdc.gov/)](https://data.cdc.gov/)](https://data.cdc.gov/)](https://data.cdc.gov/)](https://data.cdc.gov/)
- **Coverage:** US public-health indicators (national/state/local, dataset dependent)
- **Cadence:** Dataset-specific (often monthly/quarterly updates)
- **Topic tags:** us, domestic-risk, public-health
- **Good for:** Social stress context and divergence analysis alongside domestic crime series
- **Caveats:** Provisional series are revised; lag and suppression rules can affect short-window interpretation
- **Story-use ideas:** "Do overdose and violent-crime trajectories diverge unusually in specific states?"

### Chicago Crimes (2001–Present)
- **URL:** [[[[[[https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- **Coverage:** Chicago incident-level crime records with offense/date/location metadata
- **Cadence:** Frequent city feed updates
- **Topic tags:** us, domestic-crime, city-level
- **Good for:** District/category anomaly detection, near-real-time urban trend checks, policy-change impact monitoring
- **Caveats:** Incident updates/backfills occur; offense definitions and geocoding fields need careful handling
- **Story-use ideas:** "Did robbery or motor-vehicle theft break seasonal pattern in specific districts?"

### Toronto Major Crime Indicators (MCI)
- **URL:** [[[[[[https://open.toronto.ca/dataset/major-crime-indicators/](https://open.toronto.ca/dataset/major-crime-indicators/)](https://open.toronto.ca/dataset/major-crime-indicators/)](https://open.toronto.ca/dataset/major-crime-indicators/)](https://open.toronto.ca/dataset/major-crime-indicators/)](https://open.toronto.ca/dataset/major-crime-indicators/)](https://open.toronto.ca/dataset/major-crime-indicators/)
- **Coverage:** Toronto police-reported major crime incidents by category/neighbourhood/time
- **Cadence:** Periodic municipal updates
- **Topic tags:** canada, domestic-crime, city-level
- **Good for:** Canadian urban crime discontinuity checks and cross-border methodology-aware comparisons
- **Caveats:** Reporting and category conventions differ from US systems; publication lag may vary
- **Story-use ideas:** "Which Toronto neighbourhoods show category-specific outlier changes vs city baseline?"

### Stanford HELM (Holistic Evaluation of Language Models)
- **URL:** [[[[[[https://crfm.stanford.edu/helm/](https://crfm.stanford.edu/helm/)](https://crfm.stanford.edu/helm/)](https://crfm.stanford.edu/helm/)](https://crfm.stanford.edu/helm/)](https://crfm.stanford.edu/helm/)](https://crfm.stanford.edu/helm/)
- **Coverage:** AI model benchmark/evaluation reporting across tasks and scenarios
- **Cadence:** Periodic benchmark/report updates
- **Topic tags:** ai, evaluation, capability-tracking
- **Good for:** Tracking capability/safety trade-offs and identifying suspicious benchmark discontinuities
- **Caveats:** Benchmark design/protocol changes can mimic capability jumps; compare like-for-like settings
- **Story-use ideas:** "Large benchmark jump without matching transparency on training or evaluation protocol"

---

## Additions (2026-02-25 DATASET cycle, late)

### OpenSanctions (global sanctions/watchlist aggregation)
- **URL:** [[[[[[https://www.opensanctions.org/datasets/](https://www.opensanctions.org/datasets/)](https://www.opensanctions.org/datasets/)](https://www.opensanctions.org/datasets/)](https://www.opensanctions.org/datasets/)](https://www.opensanctions.org/datasets/)](https://www.opensanctions.org/datasets/)
- **Coverage:** Multi-jurisdiction sanctions, PEP, and watchlist entities from many official sources
- **Cadence:** Frequent rolling updates (dataset-dependent)
- **Topic tags:** sanctions, geopolitics, compliance, networks
- **Good for:** Tracking designation waves, entity-network expansion, and cross-regime timing gaps
- **Caveats:** Aggregated source; high-stakes claims should be checked against originating authority records
- **Story-use ideas:** "Do sanctions additions accelerate after specific conflict events, and which regimes move first?"

### UN Comtrade (official international goods trade)
- **URL:** [[[[[[https://comtrade.un.org/](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)
- **Coverage:** Bilateral goods trade by commodity/country (annual and monthly goods series)
- **Cadence:** Monthly + annual releases (with lag/revisions)
- **Topic tags:** trade, geopolitics, sanctions-evasion, macro
- **Good for:** Rerouting detection, partner-switch analysis, and commodity-level discontinuity checks
- **Caveats:** Reporting lag/mirror discrepancies; short-window interpretation requires caution
- **Story-use ideas:** "Did dual-use commodity flows reroute through intermediary hubs after sanctions changes?"

### Global Fishing Watch datasets/code
- **URL:** [[[[[[https://globalfishingwatch.org/datasets-and-code/](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)](https://globalfishingwatch.org/datasets-and-code/)
- **Coverage:** Global vessel-activity derivatives (AIS/satellite-informed), fisheries/effort layers
- **Cadence:** Product-specific updates (often frequent/periodic)
- **Topic tags:** maritime, geopolitics, enforcement, infrastructure
- **Good for:** Maritime behavior shifts near disputed waters and chokepoints
- **Caveats:** AIS coverage gaps/spoofing/transponder behavior can bias interpretation
- **Story-use ideas:** "Did apparent vessel activity collapse in a disputed area during a security incident window?"

### Edmonton EPS Neighbourhood Criminal Occurrences
- **URL:** [[[[[[https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data)
- **Coverage:** Edmonton neighbourhood-level monthly criminal occurrence counts
- **Cadence:** Monthly
- **Topic tags:** canada, domestic-crime, city-level
- **Good for:** Sub-city Canadian discontinuity analysis and category/neighbourhood outlier detection
- **Caveats:** Occurrence definitions and local reporting practices differ from other cities
- **Story-use ideas:** "Which neighbourhood-category combinations break from city baseline trend?"

### AI Incident Database (AIAAIC)
- **URL:** [[[[[[https://incidentdatabase.ai/](https://incidentdatabase.ai/)](https://incidentdatabase.ai/)](https://incidentdatabase.ai/)](https://incidentdatabase.ai/)](https://incidentdatabase.ai/)](https://incidentdatabase.ai/)
- **Coverage:** Publicly documented AI incidents across sectors/use-cases
- **Cadence:** Ongoing updates as incidents are documented
- **Topic tags:** ai, safety, incidents, governance
- **Good for:** Risk-event trend monitoring and capability-risk divergence context
- **Caveats:** Not exhaustive; depends on public reporting and curation practices
- **Story-use ideas:** "Are reported AI incidents rising faster than benchmarked capability improvements?"

---

## Additions (2026-02-26 DATASET cycle)

### World Bank Commodities Price Data (Pink Sheet)
- **URL:** [[[[https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)
- **Coverage:** Global commodity benchmark prices (energy, metals, agriculture)
- **Cadence:** Monthly
- **Topic tags:** commodities, macro, geopolitics, unrest-context
- **Good for:** Price-shock context and supply-stress baselining around policy/security events
- **Caveats:** Benchmarks are not local retail prices; lag/revisions can affect short-window reads
- **Story-use ideas:** "Did food/fuel benchmark spikes precede unrest or emergency policy changes?"

### UN Comtrade (official international trade)
- **URL:** [[[[https://comtrade.un.org/](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)
- **Coverage:** Bilateral goods trade by commodity/country (monthly + annual)
- **Cadence:** Monthly/annual releases
- **Topic tags:** trade, sanctions, geopolitics, rerouting
- **Good for:** Detecting intermediary reroutes and commodity-flow discontinuities
- **Caveats:** Mirror-stat differences and publication lag require cautious near-term inference
- **Story-use ideas:** "Did sanctioned-product flows shift through third-country hubs?"

### IMO GISIS modules
- **URL:** [[[[https://gisis.imo.org/](https://gisis.imo.org/)](https://gisis.imo.org/)](https://gisis.imo.org/)](https://gisis.imo.org/)
- **Coverage:** Maritime safety/security modules incl. piracy/casualty references
- **Cadence:** Ongoing (module-dependent)
- **Topic tags:** maritime, chokepoints, security, geopolitics
- **Good for:** Incident clustering around sea-lane stress windows
- **Caveats:** Access/completeness may vary by module/reporting pathway
- **Story-use ideas:** "Are piracy/casualty clusters increasing near strategic corridors?"

### Epoch AI GPU Clusters dataset
- **URL:** [[[[https://epoch.ai/data/gpu-clusters](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)
- **Coverage:** Publicly documented large compute clusters relevant to AI
- **Cadence:** Periodic updates
- **Topic tags:** ai, compute, infrastructure
- **Good for:** Tracking compute concentration and frontier-scale buildout changes
- **Caveats:** Public-disclosure and estimation bias; not exhaustive
- **Story-use ideas:** "Are frontier compute clusters concentrating faster in specific jurisdictions?"

---

## Additions (2026-02-26 DATASET cycle, late)

### SIPRI Military Expenditure Database
- **URL:** [https://www.sipri.org/databases/milex](https://www.sipri.org/databases/milex)
- **Coverage:** Country-level military expenditure time series (long historical span)
- **Cadence:** Annual updates
- **Topic tags:** defense, geopolitics, spending, risk-signals
- **Good for:** Contextualizing force-posture narratives and identifying unusual budget acceleration/slowdown patterns
- **Caveats:** National accounting comparability and exchange-rate effects can distort simple cross-country comparisons
- **Story-use ideas:** "Do reported security escalations align with sustained expenditure changes?"

### IEA Global EV Data Explorer
- **URL:** [https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer)
- **Coverage:** Country-level electric-vehicle stock/sales and charging indicators
- **Cadence:** Annual (with periodic updates)
- **Topic tags:** energy-transition, industry, macro, policy
- **Good for:** Tracking industrial-policy outcomes and supply-chain transition speed by country
- **Caveats:** Series definitions and market-segmentation assumptions vary; avoid overreading single-year shifts
- **Story-use ideas:** "Did subsidy changes create measurable EV adoption discontinuities?"

### NOAA IBTrACS (International Best Track Archive for Climate Stewardship)
- **URL:** [https://www.ncei.noaa.gov/products/international-best-track-archive](https://www.ncei.noaa.gov/products/international-best-track-archive)
- **Coverage:** Global tropical cyclone tracks/intensity from multiple agencies
- **Cadence:** Ongoing/periodic updates
- **Topic tags:** disaster-risk, climate, infrastructure, maritime
- **Good for:** Hazard-context overlays for port/shipping and coastal-infrastructure OSINT stories
- **Caveats:** Cross-basin and historical-era comparability needs care due to observing-system changes
- **Story-use ideas:** "Did cyclone-track clustering raise short-window risk near strategic ports?"
