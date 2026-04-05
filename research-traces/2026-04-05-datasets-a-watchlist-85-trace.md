# DATASETS_A trace — 2026-04-05

- Slot: DATASETS_A
- UTC run window: 2026-04-05 21:39–21:46

## Situational-awareness sweep

Queries sampled:
1. `Reuters April 2026 major supply chain disruption latest`
2. `AP Reuters April 2026 public safety infrastructure outage latest`
3. `WHO CDC April 2026 outbreak update hospitalizations`
4. `FAO WFP April 2026 food security emergency update`

Consequence classes observed:
- Public-health burden updates (respiratory/hospitalization context)
- Urban public-safety and mobility-service pressure
- Ongoing energy/food disruption background risk

## Discovery/anomaly sweep

- Bulk intake command:
  - `python3 scripts/bulk_dataset_intake.py --pages 2 --rows 200 --top 80`
- Artifacts:
  - `research-traces/20260405T213931Z-bulk-dataset-intake.json`
  - `research-traces/20260405T213931Z-bulk-dataset-intake.csv`
  - `research-traces/20260405T213931Z-bulk-dataset-intake-summary.md`

Blocked/error from bulk run:
- Source: HDX CKAN package_search
- URL: `https://data.humdata.org/api/3/action/package_search?rows=200&start=0`
- Error: `HTTP 406 Not Acceptable`
- UTC timestamp: `2026-04-05 21:39`
- Retry outcome: not required for DATASETS_A selection because qualifying non-HDX candidates exceeded target range; log retained for follow-up monitoring.

## Overlap pass and selection

Selected 6 net-new datasets (3–10 target met):
- Provisional COVID-19 Death Counts by Week Ending Date and State
- Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence
- Monthly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System
- Transportation Economic Trends (TET) data
- Motor Vehicle Collisions - Crashes
- Traffic Crashes - Crashes

Rejected/held examples:
- Already in catalog: Licensed and Certified Healthcare Facility Listing, Medicare Monthly Enrollment, Air Traffic Passenger Statistics, MTA Subway Stations.
- Low consequence for this cycle: lottery and narrow administrative listings.

## Output decision

- Published datasets-intel post: `2026-04-05-dataset-intel-mortality-hospital-load-and-urban-crash-risk-stack-watchlist-85.md`
- Updated `docs/datasets-catalog.md` with six new entries.
