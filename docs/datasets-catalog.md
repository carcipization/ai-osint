# Datasets Catalog

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/datasets-catalog.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/datasets-catalog.md)

**Dateline:** 2026-03-06 12:07 UTC

Compact reference list. Each item is 1–2 sentences: what it is and why it matters.

**Catalog metadata:** 69 datasets • 11 domains • structure-optimized for cadence retrieval

## Quick navigation
- [Conflict, unrest, and information control](#conflict-unrest-and-information-control)
- [Humanitarian and hazard context](#humanitarian-and-hazard-context)
- [Energy, trade, and maritime](#energy-trade-and-maritime)
- [Aviation and mobility](#aviation-and-mobility)
- [Economy, governance, and structural risk](#economy-governance-and-structural-risk)
- [Ownership, sanctions, and procurement](#ownership-sanctions-and-procurement)
- [AI capability, risk, and labor](#ai-capability-risk-and-labor)
- [Cyber vulnerability and exploitation risk](#cyber-vulnerability-and-exploitation-risk)
- [Domestic public safety](#domestic-public-safety)
- [Telegram/public-channel analytics](#telegrampublic-channel-analytics)
- [Space weather and disruption context](#space-weather-and-disruption-context)

## Retrieval lenses (for fast story triage)
Use this compact map before scanning full entries.

- **Fast operational corroboration (minutes to hourly):** OONI, RIPE Atlas, CAIDA IODA, USGS Earthquake Feeds, NOAA SWPC JSON feeds, CISA KEV Catalog, FIRST EPSS.
- **Event-tracking + anomaly detection (hourly to daily):** ACLED, GDELT, ReliefWeb API, NASA FIRMS, OpenSky Network, ADS-B Exchange, IMF PortWatch.
- **Structural baselines (monthly to annual):** UCDP GED, EM-DAT, UN Comtrade, World Bank Indicators API, IMF Data API, FAOSTAT, SIPRI Milex.
- **Entity/ownership resolution:** OpenSanctions, OpenCorporates API, Open Ownership Register, UK Companies House PSC, GLEIF LEI Golden Copy.

## Catalog maintenance rules (DATASETS_OPTIMIZE)
1. Preserve section-level taxonomy unless a split/merge clearly improves retrieval speed.
2. Prefer editing descriptors over moving entries across sections.
3. Keep each entry to one sentence of scope + one sentence of caveat/value.
4. If adding aliases in future, keep one canonical entry and mention aliases in-text.
5. Re-run duplicate-domain and section-balance checks before publish.

## Conflict, unrest, and information control
- [ACLED](https://acleddata.com/) — Near-real-time conflict and protest event data. Strong for intensity/trajectory checks, but regional reporting lag and source bias require triangulation.
- [UCDP GED](https://ucdp.uu.se/downloads/) — Curated historical conflict events. Best for baseline and long-window comparison, not immediate same-day claims.
- [ICEWS](https://dataverse.harvard.edu/dataverse/icews) — Machine-coded actor/event dataset useful for interaction trend shifts. Treat as signal-heavy and media-dependent, not ground truth.
- [GDELT](https://www.gdeltproject.org/data.html) — Global event/media coding for fast anomaly detection and narrative-shift tracking. Excellent early warning, weaker as final evidentiary anchor.
- [OONI](https://ooni.org/data/) — Network interference and censorship measurements. Useful for shutdown/censorship corroboration, with coverage uneven by probe geography.
- [RIPE Atlas](https://atlas.ripe.net/docs/) — Distributed active internet measurements for reachability/latency checks. Good for disruption diagnostics, limited by probe placement.
- [CAIDA IODA](https://www.caida.org/projects/ioda/) — Outage detection via BGP/darknet/active signals. Strong for macro outage events, less sensitive to app/platform-level blocking.

## Humanitarian and hazard context
- [ReliefWeb API](https://api.reliefweb.int/) — Structured humanitarian situation reports and updates. Useful chronology layer; quality follows upstream submitters.
- [Humanitarian Data Exchange (HDX)](https://data.humdata.org/) — OCHA-managed open humanitarian datasets and APIs for crisis indicators, displacement, and response operations. High-value cross-country evidence layer with dataset-specific quality/coverage variance.
- [EM-DAT](https://www.emdat.be/) — Disaster impact database for severity and cross-event context. Reliable for structured comparisons but estimates revise over time.
- [UNHCR Refugee Data](https://www.unhcr.org/refugee-statistics/download/) — Displacement statistics for migration and conflict follow-through analysis. Be mindful of registration lag.
- [USGS Earthquake Feeds](https://earthquake.usgs.gov/earthquakes/feed/) — Fast seismic event context and magnitude tracking. Great for timing/frequency checks; not causal attribution.
- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) — Satellite fire hotspot detections for wildfire and conflict-adjacent fire patterns. Hotspots are signal, not cause.
- [NOAA IBTrACS](https://www.ncei.noaa.gov/products/international-best-track-archive) — Tropical cyclone tracks for hazard overlays and route-risk context. Cross-era comparability is imperfect.
- [Copernicus CDS (ERA5)](https://cds.climate.copernicus.eu/) — Reanalysis weather/climate fields for baseline comparisons. Excellent contextual control layer with spatial-resolution limits.

## Energy, trade, and maritime
- [UN Comtrade](https://comtrade.un.org/) — Official trade statistics for rerouting and sanctions-evasion pattern checks. Powerful but lagged and occasionally revised.
- [UNCTADstat](https://unctadstat.unctad.org/EN/) — Trade and shipping indicators for structural maritime baselines. Strong macro context; indicator release cadence varies.
- [World Bank Pink Sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet) — Commodity benchmark prices for shock context. Not a retail/local price proxy.
- [IMF PortWatch](https://portwatch.imf.org/datasets/42132aa4e2fc4d41bdaf9a445f688931_0/explore) — AIS-derived chokepoint transit estimates for Suez/Panama-type stress checks. Sensitive to window definitions and AIS coverage.
- [U.S. EIA Open Data](https://www.eia.gov/opendata/) — Official US energy series for oil/gas/power claims. Strong grounding source; unit/metadata discipline required.
- [AGSI+](https://agsi.gie.eu/) — European gas storage dynamics. Useful for storage-stress monitoring, but storage level alone does not imply outages.
- [ENTSO-E Transparency](https://transparency.entsoe.eu/) — Power flows/generation/outage indicators across Europe. High value for grid shock stories; country/product completeness varies.
- [Global Fishing Watch](https://globalfishingwatch.org/datasets-and-code/) — Vessel activity telemetry for disputed waters and maritime behavior changes. AIS gaps/spoofing are recurring limitations.
- [IMO GISIS](https://gisis.imo.org/) — Maritime safety/security registry modules. Good official context source with module-dependent completeness.
- [Vortexa Freight Tracker](https://www.vortexa.com/freight-tracker/) — Commercial tanker flow analytics for rerouting pressure. Strong directional signal, methodology is vendor-defined.
- [MarineCadastre AccessAIS](https://marinecadastre.gov/accessais/) — US-focused AIS archive access. Useful for US waters analyses, not global coverage.
- [AISHub API](https://www.aishub.net/api) — Community AIS data feeds for vessel tracking redundancy. Coverage quality depends on contributor network.

## Aviation and mobility
- [OpenSky Network](https://opensky-network.org/data) — Open flight surveillance data for route anomaly checks. Coverage/rate limits vary by access tier.
- [ADS-B Exchange](https://www.adsbexchange.com/data/) — Broad ADS-B feeds for flight path reconstruction and discontinuities. Commercial endpoint/term changes should be monitored.
- [ADSB.lol Open Data](https://www.adsb.lol/docs/open-data/api/) — Community-backed ADS-B API and archives. Useful as independent aviation corroboration with uneven geography.

## Economy, governance, and structural risk
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) — Cross-country macro/social baselines. Good for context framing, weak for fast-cycle stories.
- [IMF Data API](https://www.imf.org/external/datamapper/api/) — Sovereign and macro indicators for stress-consistency checks. Definitions/coverage differ across IMF datasets.
- [Eurostat APIs (Statistics + Catalogue)](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access) — Official EU statistical APIs with machine-readable JSON-stat access, dataset discovery (TOC/DCAT/RSS), and structured metadata for reproducible regional baselines. High analytical value, but indicator publication cadence and definitional changes must be tracked per dataset.
- [FAOSTAT](https://www.fao.org/faostat/en/) — Food/agriculture structural data for medium/long-horizon analysis. Not suitable for immediate operational claims.
- [ITU ICT Indicators](https://www.itu.int/en/ITU-D/Statistics/Pages/publications/wtid.aspx) — Digital infrastructure and usage baselines. Useful control variable for shutdown/censorship narratives.
- [Worldwide Governance Indicators](https://info.worldbank.org/governance/wgi/) — Institutional context and fragility proxies. Annual composites are poor short-term attribution tools.
- [OECD.AI](https://oecd.ai/) — Cross-country AI ecosystem/policy indicators. Best for comparative policy context, not daily movement.
- [SIPRI Milex](https://www.sipri.org/databases/milex) — Defense spending series for security posture trend framing. Cross-country accounting differences matter.

## Ownership, sanctions, and procurement

**Sanctions provenance rule (quality guardrail):** Use originating-authority lists (e.g., OFAC, Global Affairs Canada, EU official files) as final evidentiary anchors; use aggregators (e.g., OpenSanctions) for discovery, cross-linking, and rapid triage.

- [OpenSanctions](https://www.opensanctions.org/datasets/) — Aggregated designation/entity datasets for sanctions-wave and network monitoring. Confirm high-stakes claims at originating authority.
- [OpenCorporates API](https://api.opencorporates.com/) — Company registry federation for entity resolution and corporate linkage checks. Jurisdiction depth varies.
- [Open Ownership Register](https://register.openownership.org/) — Beneficial ownership datasets for ownership-chain reconstruction. Coverage quality is country-dependent.
- [UK Companies House PSC](https://download.companieshouse.gov.uk/en_pscdata.html) — UK person-with-significant-control snapshots. Powerful for UK ownership-change analysis with filing-lag caveats.
- [USAspending API](https://api.usaspending.gov/) — US federal spending/procurement patterns and vendor concentration. Interpret obligation vs outlay carefully.
- [TED Open Data](https://data.ted.europa.eu/) — EU procurement notices and awards for cross-country trend analysis. Requires normalization across taxonomy changes.
- [UK Contracts Finder API](https://www.contractsfinder.service.gov.uk/apidocumentation) — UK procurement opportunities/awards stream. Field completeness differs across authorities.
- [GLEIF LEI Golden Copy](https://www.gleif.org/en/lei-data/gleif-golden-copy/download-the-concatenated-file) — Daily global legal-entity identifiers and reference data. High-value backbone for cross-border entity deduplication.
- [OFAC Sanctions List Service (SLS)](https://ofac.treasury.gov/sanctions-list-service) — Official U.S. Treasury sanctions list distribution (SDN + consolidated non-SDN datasets) with machine-readable download pathways. Critical primary-source anchor for sanctions designation timing and entity-screening verification.
- [Consolidated Canadian Autonomous Sanctions List](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng) — Global Affairs Canada list of individuals/entities sanctioned under SEMA and JVCFOA, published in HTML/PDF/XML. Valuable jurisdictional complement for cross-country sanctions verification and entity-resolution workflows.

## AI capability, risk, and labor
- [Stanford HELM](https://crfm.stanford.edu/helm/) — Standardized model benchmark tracking for capability/safety comparisons. Protocol drift can mimic model jumps.
- [Epoch AI GPU Clusters](https://epoch.ai/data/gpu-clusters) — Frontier compute concentration and buildout signal. Public disclosure bias means incomplete coverage.
- [AI Incident Database](https://incidentdatabase.ai/) — Curated AI incident records for qualitative risk trend monitoring. Public-report dependence limits completeness.
- [LMArena](https://lmarena.ai/leaderboard) — Human-preference leaderboard signal for model shifts and previews. Preference-based Elo is useful but sampling-sensitive.
- [Artificial Analysis](https://artificialanalysis.ai/) — Multi-benchmark model comparisons for cross-checking leaderboard narratives. Vendor/test selection can shape rankings.
- [Indeed Hiring Lab](https://www.hiringlab.org/) — Labor-market signal on skills demand and hiring shifts. Platform composition effects should be considered.
- [LinkedIn Economic Graph](https://economicgraph.linkedin.com/) — Workforce trend analytics for occupational and skills transitions. Platform sample bias applies.

## Cyber vulnerability and exploitation risk
- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Authoritative list of vulnerabilities observed exploited in the wild for federal prioritization. Crucial corroboration source for exploitation claims.
- [FIRST EPSS](https://www.first.org/epss/data_stats) — Daily exploit-likelihood scoring for CVE triage prioritization. Probability signal, not exploitation confirmation.
- [NIST NVD CVE API](https://nvd.nist.gov/developers/vulnerabilities) — CVE metadata/severity/references and modification tracking. Enrichment lag/revisions are common.

## Domestic public safety
- [FBI CDE/UCR](https://cde.ucr.cjis.gov/) — US crime baseline comparisons across jurisdictions. Participation and categorization shifts can affect comparability.
- [Statistics Canada](https://www.statcan.gc.ca/) — Canadian official statistical series for national and provincial context. Release lag and revisions apply.
- [Chicago Crimes (2001–present)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2) — High-frequency city-level incident records for local anomaly scans. Backfills/reclassifications occur.
- [Toronto MCI](https://open.toronto.ca/dataset/major-crime-indicators/) — Neighbourhood-level major-crime indicators for city trend checks. Definitions differ from US systems.
- [Edmonton EPS occurrences](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data) — Monthly neighbourhood crime indicators for local outlier detection. Not directly comparable across municipalities.

## Telegram/public-channel analytics
- [TGStat API](https://tgstat.com/api/stat) — Public Telegram channel growth/citation signal. Third-party methodology should be treated as a caveated proxy.
- [Telemetr API](https://api.telemetr.io/) — Channel benchmarking and trend data for comparative network scans. Coverage and terms may change.
- [TGDataset](https://github.com/SystemsLab-Sapienza/TGDataset) — Research snapshot corpus for historical Telegram network structure. Best for baseline context, not live operational monitoring.

## Space weather and disruption context
- [NOAA SWPC JSON feeds](https://services.swpc.noaa.gov/json/) — Operational space-weather observations/forecasts (e.g., flare/Kp products). Useful for timing and severity context in comms/power/GNSS stories, with forecast/observed distinction required.
