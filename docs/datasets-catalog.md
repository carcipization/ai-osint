# Datasets Catalog

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
- **URL:** https://acleddata.com/
- **Coverage:** Global conflict/unrest events (country-level availability varies)
- **Cadence:** Frequent updates
- **Topic tags:** geopolitics, unrest, conflict
- **Good for:** Detecting spikes in protests, violence, and conflict-event shifts
- **Caveats:** Methodology definitions matter; reporting lag and source bias by region
- **Story-use ideas:** "Protest intensity in X region jumps Y% week-over-week"

### GDELT Events
- **URL:** https://www.gdeltproject.org/
- **Coverage:** Global media-derived event signals
- **Cadence:** Near real-time
- **Topic tags:** geopolitics, unrest, media signals
- **Good for:** Early-change detection and narrative shifts across regions/topics
- **Caveats:** Media-coverage bias; not a direct ground-truth dataset
- **Story-use ideas:** "Media event-code surge preceded policy move"

### USGS Earthquake Catalog
- **URL:** https://earthquake.usgs.gov/earthquakes/feed/
- **Coverage:** Global seismic events
- **Cadence:** Near real-time feeds
- **Topic tags:** disaster, infrastructure risk
- **Good for:** Rapid hazard context for geopolitical/infrastructure stories
- **Caveats:** Natural hazard data; relevance to political stories is contextual
- **Story-use ideas:** "Clustered seismic events near critical infrastructure"

### NASA FIRMS (Fire Information for Resource Management System)
- **URL:** https://firms.modaps.eosdis.nasa.gov/
- **Coverage:** Global fire hotspots from satellite detections
- **Cadence:** Near real-time/daily products
- **Topic tags:** environment, conflict context, disruption
- **Good for:** Detecting unusual fire concentration changes by region
- **Caveats:** Cloud cover/sensor limits; hotspot ≠ confirmed incident cause
- **Story-use ideas:** "Unexpected hotspot spike in region under unrest"

### StatsCan Crime data portal
- **URL:** https://www.statcan.gc.ca/ (datasets vary by table)
- **Coverage:** Canada domestic statistics incl. crime tables
- **Cadence:** Monthly/quarterly/annual depending table
- **Topic tags:** domestic-crime, canada
- **Good for:** Baseline trends and regional crime discontinuities in Canada
- **Caveats:** Release lag; table definitions/revisions
- **Story-use ideas:** "Category-level divergence across provinces"

### FBI CDE / UCR resources
- **URL:** https://cde.ucr.cjis.gov/
- **Coverage:** US crime reporting datasets/dashboards
- **Cadence:** Periodic releases
- **Topic tags:** domestic-crime, us
- **Good for:** US national/regional crime trend comparisons
- **Caveats:** Reporting participation changes; category comparability over time
- **Story-use ideas:** "Outlier metro trend compared to national baseline"

### OECD.AI Policy Observatory / indicators
- **URL:** https://oecd.ai/
- **Coverage:** AI policy, ecosystem, and country indicators
- **Cadence:** Periodic updates
- **Topic tags:** ai, policy, geopolitics
- **Good for:** Cross-country AI policy and capability context
- **Caveats:** Some metrics are composite and methodology-sensitive
- **Story-use ideas:** "Policy change vs investment/compute signal mismatch"
