# Research Trace — 2026-03-13 NOAA geomagnetic peak timing story

## Run metadata
- Mode: ONE-OFF STORY (out-of-cadence)
- UTC start: 2026-03-13 ~03:40

## Situational-awareness sweep (world-state trigger)
Searches run:
- `NOAA SWPC geomagnetic storm watch March 13 2026 G2`
- `USGS significant earthquakes past day March 2026`
- `UN OCHA latest humanitarian situation update March 2026 flood earthquake conflict`

Candidate notes:
1. **SWPC geomagnetic forecast update**
   - Freshness artifact: `3-day-forecast.txt` issued `2026 Mar 13 0030 UTC`; `3-day-geomag-forecast.txt` issued `2026 Mar 12 2205 UTC`.
   - Availability: good (direct text + JSON endpoints live).
   - Baseline comparability: available via `daily-geomagnetic-indices.txt`.
   - Decision surface: grid/satcom/aviation HF operators doing short-horizon checks.
   - Status: **accepted**.

2. **USGS significant earthquakes**
   - Freshness artifact: `significant_day.geojson` (count 0), `significant_week.geojson` (2 events, none new in last 24h).
   - Reject reason: no current-day significant-event anomaly to support a same-cycle story.

3. **OCHA humanitarian updates (Myanmar/Mozambique)**
   - Freshness artifact: recent updates exist.
   - Reject reason: no clear, testable short-window anomaly with robust baseline comparison in this run window.

## Anomaly trigger sweep
Checks run:
- SWPC machine-readable products (`noaa-scales.json`, `daily-geomagnetic-indices.txt`, `current-space-weather-indices.txt`)
- USGS event-volume vs significant-event feeds (`all_day.geojson`, `significant_day.geojson`)

Anomaly candidates:
- **SWPC**: forecasted transition from observed sub-G1 conditions to a forecast Kp 5 (G1 threshold) interval, with 40% minor-storm probabilities on Mar 13 and Mar 14.
- **USGS**: significant-day count zero despite high all-event count; judged routine filter behavior, not a publishable anomaly.

## Verification ledger (trace-to-copy mapping)
1. Source: https://services.swpc.noaa.gov/text/3-day-forecast.txt  
   - Timestamp: issued 2026-03-13 00:30 UTC  
   - Classification: Observation  
   - Proves: expected max Kp 5.00 (G1), interval breakdown incl. 15–18 UTC Mar 13, mechanism note (positive-polarity coronal hole).  
   - Limitation: forecast product; can revise.

2. Source: https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt  
   - Timestamp: issued 2026-03-12 22:05 UTC  
   - Classification: Observation  
   - Proves: minor-storm probability 40/40/20 and Ap forecast 20/20/12.  
   - Limitation: probabilistic, not realized outcome.

3. Source: https://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt  
   - Timestamp: issued 2026-03-13 03:30 UTC  
   - Classification: Observation  
   - Proves: recent observed planetary K values were generally below storm threshold immediately before forecast window.  
   - Limitation: partial current day entries include placeholder -1 values.

4. Source: https://services.swpc.noaa.gov/products/noaa-scales.json  
   - Timestamp: fetched 2026-03-13 ~03:41 UTC  
   - Classification: Observation  
   - Proves: forward days encoded as G1/minor with associated R/S probabilities.  
   - Limitation: reflects current model snapshot only.

## Contradiction / falsification pass
- Counter-thesis: forecasted G1 window remains near-threshold and may not verify in realized Kp values.
- Targeted check: compared forecast Kp blocks/probabilities with current/last-day indices and noaa-scales JSON.
- Result: no direct contradiction found; uncertainty retained as forecast-led signal.

## Could this be wrong because...
- Top disconfirming hypothesis: coronal-hole stream influence underperforms, keeping realized Kp below 5.
- Invalidating evidence to watch: updated SWPC forecast downgrades, or observed Kp blocks never reach 5 through Mar 14.
- Found or missing: missing yet (future realization window pending).

## Last-72h overlap check
- Near-overlap item: 2026-03-12 NOAA G1 window story.
- Duplicate rationale: **not treated as duplicate** because this run adds a newly issued forecast cycle with explicit intraday peak timing and refreshed probability framing for Mar 13–15 operations.
