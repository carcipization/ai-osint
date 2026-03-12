# Datasets Catalog

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/datasets-catalog.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/datasets-catalog.md)

**Dateline:** 2026-03-11 21:01 UTC

Compact reference list. Each item is 1–2 sentences: what it is and why it matters.

**Catalog metadata:** 118 datasets • 11 domains • structure-optimized for cadence retrieval

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
- [Telegram and public-channel analytics](#telegram-and-public-channel-analytics)
- [Space weather and disruption context](#space-weather-and-disruption-context)

## Structural QA snapshot
- **Section balance (entries):** Economy/governance (27), Energy/trade/maritime (13), Ownership/sanctions/procurement (11), Humanitarian/hazard (26), Conflict/unrest/info-control (7), AI/risk/labor (7), Domestic public safety (12), Aviation/mobility (9), Cyber exploitation risk (2), Telegram/public-channel analytics (3), Space weather (1).
- **Balance checksum:** 27+13+11+26+7+7+12+9+2+3+1 = **118** (must match catalog metadata count).
- **Skew flag:** space-weather is intentionally narrow and relies on NOAA SWPC as the primary operational feed; expand only when additional machine-readable primary feeds are identified.
- **Catalog hygiene checks:** metadata count aligned to current entries, navigation anchors normalized, and section naming standardized for stable deep links.

## Retrieval aliases (canonical domain tokens)
Use these stable tokens in internal retrieval notes so query phrasing stays consistent across cadence runs.

- **conflict-control:** conflict, unrest, censorship, shutdowns, outages
- **humanitarian-hazard:** earthquakes, disasters, displacement, fires, coastal
- **humanitarian-risk-shards:** country risk-assessment indicator datasets (e.g., HDX country-level risk indicator packs)
- **energy-trade-maritime:** shipping, chokepoints, commodities, power, gas
- **aviation-mobility:** flights, ADS-B, routes, air traffic
- **economy-governance-risk:** macro, central-bank, labor, fiscal, governance
- **ownership-sanctions-procurement:** sanctions, entities, beneficial ownership, contracts
- **ai-risk-labor:** model capability, incidents, compute, hiring
- **cyber-exploitation:** CVE, EPSS, exploitation
- **public-safety:** crime, police, city incidents
- **telegram-analytics:** channels, citations, growth
- **space-weather:** solar flares, geomagnetic, Kp, SWPC

## Retrieval lenses (for fast story triage)
Use this compact map before scanning full entries.

- **Fast operational corroboration (minutes to hourly):** OONI, RIPE Atlas, CAIDA IODA, USGS Earthquake Feeds, NOAA SWPC JSON feeds, FIRST EPSS.
- **Event-tracking + anomaly detection (hourly to daily):** ACLED, GDELT, ReliefWeb API, NASA FIRMS, OpenSky Network, ADS-B Exchange, IMF PortWatch.
- **Structural baselines (monthly to annual):** UCDP GED, EM-DAT, UN Comtrade, World Bank Indicators API, IMF Data API, FAOSTAT, SIPRI Milex.
- **Entity/ownership resolution:** OpenSanctions, OpenCorporates API, Open Ownership Register, UK Companies House PSC, GLEIF LEI Golden Copy.
- **Revision-sensitive series (confidence-capped until confirmed):** Eurostat annual demographic indicators with break/provisional flags, IMF/World Bank indicators near recent release boundaries, and any feed with explicit estimated/provisional markers.

## Catalog maintenance rules (DATASETS_OPTIMIZE)
1. Preserve section-level taxonomy unless a split/merge clearly improves retrieval speed.
2. Prefer editing descriptors over moving entries across sections.
3. Keep each entry to one sentence of scope + one sentence of caveat/value.
4. If adding aliases in future, keep one canonical entry and mention aliases in-text.
5. Re-run duplicate-domain and section-balance checks before publish.
6. For entries used in current-cycle analysis, surface revision/provisional flags in the story method/limitations when the source exposes them.
7. For city-level incident feeds, prefer one canonical entry per city/system and avoid near-duplicate mirrors unless they add distinct fields.
8. For catalog entries with date-stamped titles (e.g., corridor snapshots), keep the version date in the title and note supersession risk in the descriptor.
9. For country-sharded datasets (same schema repeated across countries), prefer one concise naming pattern and keep descriptors template-consistent so retrieval and dedup checks remain stable.
10. When adding multiple country shards in one cycle, record the family label in traces (e.g., "risk-assessment indicators") to speed future overlap checks.

## Freshness and revision-risk tags (retrieval optimization)
Use these compact tags in internal triage notes to avoid over-trusting revision-sensitive feeds.

- **F0 (live/operational):** minute/hourly feeds; high utility for breaking checks, high volatility risk.
- **F1 (daily/near-daily):** strong short-cycle monitoring value; expect occasional backfills.
- **F2 (periodic official):** weekly/monthly official releases; stable baseline, slower signal.
- **F3 (structural/annual):** long-horizon context only; unsuitable for real-time claims.

**Revision flags:**
- **R+ (revision-prone):** source commonly backfills or restates recent periods.
- **R0 (low revision):** revision risk present but typically limited after release cutoffs.

Operational rule: for high-impact claims, avoid single-source conclusions from **F0+R+** datasets without at least one independent corroboration family.

### Country-shard dedup protocol (DATASETS_OPTIMIZE)
- If many country variants of the same dataset family appear in discovery, add only shards that improve geographic coverage gaps for current monitoring priorities.
- Avoid adding adjacent-country shards solely due to recency timestamps when they do not expand decision-relevant coverage.
- In traces, list selected shards and at least one intentionally skipped shard family to document breadth-vs-duplication judgment.

### Municipal-feed comparability protocol (DATASETS_OPTIMIZE)
- Treat cross-city crime and crash feeds as **within-city trend tools first**, not direct city-vs-city ranking tools.
- When used for cross-city context, require a same-period normalization note (population, reporting standard, or offense definition scope).
- If a municipal dataset lacks stable definition history, cap confidence for comparative claims and document the missing standardization artifact.

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
- [NOAA CO-OPS Data Retrieval API](https://api.tidesandcurrents.noaa.gov/api/prod/) — Official U.S. coastal observations/predictions (water level, tides, currents, meteorology) with high-frequency station queries. Strong disruption-context source with station-coverage and interval-limit constraints.
- [Copernicus CDS (ERA5)](https://cds.climate.copernicus.eu/) — Reanalysis weather/climate fields for baseline comparisons. Excellent contextual control layer with spatial-resolution limits.
- [WFP Global Food Prices](https://data.humdata.org/dataset/global-wfp-food-prices) — WFP-curated global market price observations for staple commodities across countries and markets. High-value inflation and food-security signal with country coverage and market-sampling variability.
- [FAO Data in Emergencies (DIEM)](https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data) — FAO emergency household-survey aggregates on livelihoods, food security, and shocks in crisis-affected settings. Useful for humanitarian stress triangulation, but survey timing and sampling frames differ by operation.
- [NYC Air Quality](https://catalog.data.gov/dataset/air-quality) — New York City air quality indicators for pollution-related exposure context and local hazard monitoring. Strong city-level signal with methodology breaks and station coverage changes requiring caution.
- [WFP HungerMap – Ukraine](https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr) — WFP HungerMap indicators for Ukraine covering food-security stress proxies and related humanitarian conditions. Useful for rapid situation tracking with model/input dependency caveats.
- [WFP HungerMap – Haiti](https://data.humdata.org/dataset/wfp-hungermap-data-for-hti) — WFP HungerMap indicators for Haiti providing near-operational food-security stress context. Valuable for crisis monitoring, but indicator construction and reporting cadence can shift.
- [WFP HungerMap – Ecuador](https://data.humdata.org/dataset/wfp-hungermap-data-for-ecu) — WFP HungerMap indicators for Ecuador for emerging food-access and stress pattern checks. Good directional layer that should be triangulated with country sources.
- [CDC Provisional COVID-19 Death Counts by Week and State](https://catalog.data.gov/dataset/provisional-covid-19-death-counts-by-week-ending-date-and-state) — Weekly provisional mortality counts by U.S. state for respiratory-wave and excess-pressure context. High-value public-health signal with known reporting lag and revision risk.
- [CDC COVID-NET Monthly Hospitalization Rates](https://catalog.data.gov/dataset/monthly-rates-of-laboratory-confirmed-covid-19-hospitalizations-from-the-covid-net-surveil) — Laboratory-confirmed COVID-19 hospitalization rates used for severity and burden tracking. Strong trend signal, but coverage reflects surveillance-network design rather than full-population capture.
- [HDX HAPI - Climate: Rainfall](https://data.humdata.org/dataset/hdx-hapi-rainfall) — Harmonized rainfall indicators in the HDX Humanitarian API Pipeline for rapid hydro-climate stress context. Useful for short-cycle hazard corroboration, but gridded/aggregated processing assumptions should be checked before local attribution.
- [Licensed and Certified Healthcare Facility Listing](https://catalog.data.gov/dataset/licensed-and-certified-healthcare-facility-listing-6e3f9) — Structured roster of licensed and certified healthcare facilities for capacity and service-footprint context during public-health or disaster response reporting. Valuable infrastructure baseline with provider-status update lag caveats.
- [FWS Critical Habitat for Threatened and Endangered Species Dataset](https://catalog.data.gov/dataset/fws-critical-habitat-for-threatened-and-endangered-species-dataset-baa5a) — U.S. Fish and Wildlife Service critical-habitat geospatial designations that support environmental exposure and infrastructure-siting risk context in disaster and land-use reporting. High-value federal baseline with designation-update timing and legal-status interpretation caveats.
- [Oman - Risk Assessment Indicators](https://data.humdata.org/dataset/oman---risk-assessment-indicators) — Country-level humanitarian risk indicator package for Oman that supports baseline vulnerability and preparedness context in regional hazard reporting. Useful comparative signal with methodology-version and periodic-refresh caveats.
- [Saint Vincent And The Grenadines - Risk Assessment Indicators](https://data.humdata.org/dataset/saint-vincent-and-the-grenadines---risk-assessment-indicators) — Small-island humanitarian risk indicator series for Saint Vincent and the Grenadines, useful for disaster-exposure and resilience context checks in Caribbean monitoring. Valuable denominator layer with country-scale volatility and update-lag caveats.
- [Kuwait - Risk Assessment Indicators](https://data.humdata.org/dataset/kuwait---risk-assessment-indicators) — Structured humanitarian risk indicators for Kuwait supporting Gulf-region stress-comparison and preparedness-context reporting. Useful baseline input with indicator-definition revision risk.
- [United Arab Emirates - Risk Assessment Indicators](https://data.humdata.org/dataset/united-arab-emirates---risk-assessment-indicators) — Country risk indicator dataset for the UAE that adds machine-readable vulnerability context for regional hazard and response planning analysis. Strong contextual layer with periodic methodology updates to monitor.
- [Trinidad And Tobago - Risk Assessment Indicators](https://data.humdata.org/dataset/trinidad-and-tobago---risk-assessment-indicators) — Humanitarian risk indicators for Trinidad and Tobago supporting Caribbean cross-country baseline checks during tropical and climate-linked stress reporting. Useful contextual benchmark with small-population sensitivity caveats.
- [GDACS RSS Information](https://data.humdata.org/dataset/gdacs-rss-information) — Global Disaster Alert and Coordination System alert feed snapshots for near-real-time disaster signal intake. Strong early-warning utility with alert-severity interpretation and update churn caveats.

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
- [Harmonized Tariff Schedule of the United States (2026)](https://catalog.data.gov/dataset/harmonized-tariff-schedule-of-the-united-states-2024) — Official U.S. tariff schedule classifications and duty-rate tables for import-policy and trade-exposure verification. Authoritative legal baseline, with periodic amendments that require effective-date checks.

## Aviation and mobility
- [OpenSky Network](https://opensky-network.org/data) — Open flight surveillance data for route anomaly checks. Coverage/rate limits vary by access tier.
- [ADS-B Exchange](https://www.adsbexchange.com/data/) — Broad ADS-B feeds for flight path reconstruction and discontinuities. Commercial endpoint/term changes should be monitored.
- [ADSB.lol Open Data](https://www.adsb.lol/docs/open-data/api/) — Community-backed ADS-B API and archives. Useful as independent aviation corroboration with uneven geography.
- [Air Traffic Passenger Statistics](https://catalog.data.gov/dataset/air-traffic-passenger-statistics) — Airport-level passenger throughput and route-level traffic counts for aviation demand and disruption context checks. Strong operational signal with airport-reporting and periodic backfill caveats.
- [MTA Metro-North Delays](https://catalog.data.gov/dataset/mta-metro-north-delays-beginning-2012) — Commuter rail delay records for transport reliability and urban mobility stress monitoring. Useful local operations layer, but incident coding and delay attribution can revise.
- [Alternative Fuel Corridors (November 3 2025)](https://catalog.data.gov/dataset/alternative-fuel-corridors-november-3-2025) — Official designated U.S. alternative-fuel highway corridors for EV/hydrogen fueling coverage baselines in mobility resilience analysis. Useful infrastructure context, but designation status can lag real-world buildout.
- [Electric Vehicle Population Data](https://catalog.data.gov/dataset/electric-vehicle-population-data) — Registration-level electric-vehicle population records for adoption trend and charging-demand context in transport-transition stories. Strong policy-sensitive signal with jurisdiction-specific reporting lag and reclassification caveats.
- [MTA Subway Stations](https://catalog.data.gov/dataset/mta-subway-stations) — Geocoded New York City subway station inventory supporting urban mobility exposure, disruption mapping, and transit-access analysis. Useful static infrastructure layer with occasional metadata/version refresh gaps.
- [NEVI 2 Corridor Groups (October 28 2025)](https://catalog.data.gov/dataset/nevi-2-corridor-groups-october-28-2025) — Corridor groupings for National Electric Vehicle Infrastructure planning and deployment tracking across U.S. routes. Valuable for charging-network rollout monitoring with versioned geometry and milestone-update caveats.

## Economy, governance, and structural risk
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) — Cross-country macro/social baselines. Good for context framing, weak for fast-cycle stories.
- [IMF Data API](https://www.imf.org/external/datamapper/api/) — Sovereign and macro indicators for stress-consistency checks. Definitions/coverage differ across IMF datasets.
- [Eurostat APIs (Statistics + Catalogue)](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access) — Official EU statistical APIs with machine-readable JSON-stat access, dataset discovery (TOC/DCAT/RSS), and structured metadata for reproducible regional baselines. High analytical value, but indicator publication cadence and definitional changes must be tracked per dataset.
- [U.S. Census Bureau APIs](https://www.census.gov/data/developers/data-sets.html) — Official U.S. demographic, housing, and economic datasets (ACS, Decennial, and more) with granular geographic cuts. High utility for domestic baseline/anomaly work, with endpoint/version heterogeneity to manage.
- [Border Crossing Entry Data](https://catalog.data.gov/dataset/border-crossing-entry-data-683ae) — U.S. land-border crossing counts by port, mode, and traveler/vehicle type for trade-and-mobility pressure monitoring. Useful high-frequency policy-sensitivity signal with known seasonality and port-level reporting revision risk.
- [California Public Schools 2024-25](https://catalog.data.gov/dataset/california-public-schools-2024-25) — Statewide school directory and status attributes for district-level infrastructure and enrollment-footprint context in education-governance and local service-capacity reporting. Useful structural denominator with annual roll-over and administrative-code change caveats.
- [Warehouse and Retail Sales](https://catalog.data.gov/dataset/warehouse-and-retail-sales) — U.S. Census monthly warehouse and retail sales time series for demand and inventory-cycle context in macro and supply-chain reporting. Useful high-frequency economic barometer with seasonal-adjustment and revision-window caveats.
- [FRED API (St. Louis Fed)](https://fred.stlouisfed.org/docs/api/fred/) — Large macro/financial time-series API with release, category, and observation endpoints for reproducible economic context checks. Excellent baseline layer, but mixed source provenance across series requires metadata discipline.
- [BLS Public Data API](https://www.bls.gov/developers/) — U.S. Bureau of Labor Statistics machine-readable labor series (employment, CPI, PPI, productivity and more) for high-confidence domestic labor/inflation baselines. Strong official coverage with series-ID and seasonal-adjustment handling required.
- [Quarterly Census of Employment and Wages (QCEW)](https://catalog.data.gov/dataset/quarterly-census-of-employment-and-wages-qcew-a6fea) — U.S. establishment-level employment and wage aggregates by county, industry, and quarter for labor-market stress and regional concentration analysis. Strong denominator source with known publication lag versus faster but noisier survey indicators.
- [BEA Data API](https://apps.bea.gov/API/signup/) — U.S. Bureau of Economic Analysis API for GDP, personal income, international transactions, and regional accounts used in macro claim context checks. Primary-source economic backbone with revision-aware interpretation needed around release windows.
- [ECB Data Portal API / SDW](https://data.ecb.europa.eu/help/api/overview) — European Central Bank Statistical Data Warehouse API for euro area monetary, financial, and banking indicators. High-value eurozone baseline layer, but concept/code-list precision is essential for reproducible pulls.
- [BIS Data Portal API](https://data.bis.org/help/api) — Bank for International Settlements machine-readable macro-financial and banking statistics for cross-border credit, debt, and liquidity context. Strong systemic-risk baseline with careful series-key selection required.
- [OECD SDMX-JSON API](https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html) — OECD programmatic access to macro, labor, and policy indicators in SDMX structures, useful for multi-country denominator checks. High comparability value, but dataset dimensions and revisions vary by domain.
- [U.S. Treasury FiscalData API](https://fiscaldata.treasury.gov/api-documentation/) — Official U.S. Treasury API for debt, cash, deficit, and revenue series used in fiscal stress and financing claims. First-party authority source with table/version metadata discipline needed.
- [Bank of England Database API](https://www.bankofengland.co.uk/boeapps/database/help.asp?Back=Y&Highlight=CSV) — Official Bank of England statistical database endpoints for rates, money, and balance-sheet context in UK-focused macro stories. Valuable central-bank anchor with legacy query syntax constraints.
- [UK ONS APIs (Developer Hub)](https://developer.ons.gov.uk/) — Office for National Statistics APIs and dataset endpoints for UK population, labor, prices, and economic indicators. Strong first-party UK baseline layer with dataset-level release-cadence checks still required.
- [Deutsche Bundesbank SDMX Web Service](https://www.bundesbank.de/en/statistics/time-series-databases/help-for-sdmx-web-service-611112) — Bundesbank machine-readable SDMX service for monetary, banking, and macro-financial series used in Germany/euro-area context checks. High-quality central-bank source with series-key/code-list precision needed for reproducible pulls.
- [Bank of Canada Valet API](https://www.bankofcanada.ca/valet/docs) — Official Bank of Canada Valet API for exchange rates, interest rates, and related financial series suitable for Canada-focused macro and policy verification. Primary-source monetary baseline with endpoint/series metadata discipline required.
- [Japan e-Stat API](https://www.e-stat.go.jp/en/api/) — Government of Japan Statistics Bureau API gateway for official national statistics across demographics, labor, prices, and industry datasets. Valuable first-party Japan denominator source with table-specific update cadence and schema differences to track.
- [FAOSTAT](https://www.fao.org/faostat/en/) — Food/agriculture structural data for medium/long-horizon analysis. Not suitable for immediate operational claims.
- [ITU ICT Indicators](https://www.itu.int/en/ITU-D/Statistics/Pages/publications/wtid.aspx) — Digital infrastructure and usage baselines. Useful control variable for shutdown/censorship narratives.
- [Worldwide Governance Indicators](https://info.worldbank.org/governance/wgi/) — Institutional context and fragility proxies. Annual composites are poor short-term attribution tools.
- [OECD.AI](https://oecd.ai/) — Cross-country AI ecosystem/policy indicators. Best for comparative policy context, not daily movement.
- [Polymarket](https://polymarket.com/) — Real-money event-contract market prices that can act as high-frequency belief proxies for elections, policy, and geopolitical scenarios. Useful as a sentiment/expectations signal, but contract design, liquidity, and participant composition can distort implied probabilities.
- [Metaculus](https://www.metaculus.com/questions/) — Forecast-question platform with probabilistic crowd predictions and time-series forecast histories, useful for expectation-shift monitoring and narrative timing checks. Strong for trend-of-belief signals, but user-base composition and question framing can bias implied probabilities.
- [SIPRI Milex](https://www.sipri.org/databases/milex) — Defense spending series for security posture trend framing. Cross-country accounting differences matter.

## Ownership, sanctions, and procurement

**Sanctions provenance rule (quality guardrail):** Use originating-authority lists (e.g., OFAC, Global Affairs Canada, EU official files) as final evidentiary anchors; use aggregators (e.g., OpenSanctions) for discovery, cross-linking, and rapid triage.

- [OpenSanctions](https://www.opensanctions.org/datasets/) — Aggregated designation/entity datasets for sanctions-wave and network monitoring. Confirm high-stakes claims at originating authority.
- [UN Security Council Consolidated List](https://scsanctions.un.org/resources/xml/en/consolidated.xml) — Official UN consolidated sanctions list in XML/HTML/PDF with committee-linked identifiers. High-value multilateral baseline for cross-jurisdiction sanctions timing and scope checks.
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
- [FIRST EPSS](https://www.first.org/epss/data_stats) — Daily exploit-likelihood scoring for CVE triage prioritization. Probability signal, not exploitation confirmation.
- [NIST NVD CVE API](https://nvd.nist.gov/developers/vulnerabilities) — CVE metadata/severity/references and modification tracking. Enrichment lag/revisions are common.

## Domestic public safety
- [FBI CDE/UCR](https://cde.ucr.cjis.gov/) — US crime baseline comparisons across jurisdictions. Participation and categorization shifts can affect comparability.
- [Statistics Canada](https://www.statcan.gc.ca/) — Canadian official statistical series for national and provincial context. Release lag and revisions apply.
- [Chicago Crimes (2001–present)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2) — High-frequency city-level incident records for local anomaly scans. Backfills/reclassifications occur.
- [Toronto MCI](https://open.toronto.ca/dataset/major-crime-indicators/) — Neighbourhood-level major-crime indicators for city trend checks. Definitions differ from US systems.
- [Edmonton EPS occurrences](https://dashboard.edmonton.ca/dataset/EPS-Neighbourhood-Criminal-Occurrences/xthe-mnvi/data) — Monthly neighbourhood crime indicators for local outlier detection. Not directly comparable across municipalities.
- [NYC Motor Vehicle Collisions – Crashes](https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes) — High-frequency crash records including location, contributing factors, and injury/fatality fields for urban safety trend checks. Valuable operational signal with reporting-lag and post-incident reclassification caveats.
- [311 Service Requests from 2020 to Present](https://catalog.data.gov/dataset/311-service-requests-from-2010-to-present) — NYC non-emergency service-request stream useful for early urban-friction signals (infrastructure complaints, sanitation pressure, local service disruptions) before they appear in formal incident datasets. High-volume lead-generation feed with category-policy changes and reporting behavior bias caveats.
- [Recalls Data](https://catalog.data.gov/dataset/recalls-data) — U.S. product recall notices across consumer, vehicle, and safety-related categories for hazard-monitoring and exposure-context checks. Useful rapid-alert layer with agency-specific taxonomy differences.
- [NYC Motor Vehicle Collisions – Person](https://catalog.data.gov/dataset/motor-vehicle-collisions-person) — Person-level casualty records linked to NYC collision incidents for severity and vulnerable-road-user pattern checks. High granularity with privacy-driven field suppression and revision caveats.
- [Crash Reporting – Drivers Data](https://catalog.data.gov/dataset/crash-reporting-drivers-data) — Driver-level crash report records for contributing-factor and impairment-context analysis in traffic-safety stories. Strong explanatory layer with jurisdiction-specific coding limits.
- [SPD Crime Data: 2008-Present](https://catalog.data.gov/dataset/spd-crime-data-2008-present-c0edb) — Seattle Police Department incident records for city-level trend and hotspot monitoring across offense categories. Useful metro public-safety signal with periodic recoding/backfill caveats.
- [Crime Data from 2020 to 2024](https://catalog.data.gov/dataset/crime-data-from-2020-to-present) — Los Angeles incident-level crime records for high-frequency local safety trend checks and cross-city pattern comparison. Valuable operational layer with reporting-lag and classification-change limitations.

## Telegram and public-channel analytics
- [TGStat API](https://tgstat.com/api/stat) — Public Telegram channel growth/citation signal. Third-party methodology should be treated as a caveated proxy.
- [Telemetr API](https://api.telemetr.io/) — Channel benchmarking and trend data for comparative network scans. Coverage and terms may change.
- [TGDataset](https://github.com/SystemsLab-Sapienza/TGDataset) — Research snapshot corpus for historical Telegram network structure. Best for baseline context, not live operational monitoring.

## Space weather and disruption context
- [NOAA SWPC JSON feeds](https://services.swpc.noaa.gov/json/) — Operational space-weather observations/forecasts (e.g., flare/Kp products). Useful for timing and severity context in comms/power/GNSS stories, with forecast/observed distinction required.
