# DATASETS one-off trace — 2026-03-25 18:24 UTC

Run type: ONE-OFF DATASETS (out-of-cadence)

## Constraints honored
- Did not read or modify cadence state files.
- No cadence rotation/schedule edits.
- Datasets-only output (no STORY/FOLLOWUP publish).

## Discovery sweep (web search terms)
- `site:catalog.data.gov dataset weekly unemployment insurance claims state`
- `site:catalog.data.gov dataset opioid treatment admissions`
- `site:catalog.data.gov dataset drinking water violations`
- `site:catalog.data.gov dataset emergency medical services response times`
- `site:catalog.data.gov "National Transit Database" monthly ridership dataset`
- `catalog.data.gov national bridge inventory dataset`
- `site:catalog.data.gov dataset rail service disruptions`

## Overlap pass against docs/datasets-catalog.md
- `ETA-539` -> duplicate (already listed)
- `Fair Market Rents` -> duplicate (already listed)
- `SDWIS/FED Drinking Water Data` -> net-new
- `Monthly Modal Time Series` -> net-new
- `National Bridge Inventory` -> net-new
- `Highway-Rail Accidents` -> net-new
- `Train Accident Reports (Form FRA 6180.54)` -> net-new
- `Emergency Medical Service (EMS) Stations` -> net-new

## Selection rationale (importance-first)
Selected six net-new datasets because they improve broad non-specialist consequence monitoring across:
1) drinking-water safety/compliance,
2) emergency response access,
3) transport infrastructure integrity and incident risk,
4) public transit service demand continuity.

Rejected convenience-only additions where duplicates already existed or where consequence value was narrower than selected options.

## Publish artifact
- `docs/2026-03-25-dataset-intel-public-infrastructure-and-safety-stack-watchlist-54.md`
