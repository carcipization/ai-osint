# Trace — USGS significant earthquake lull

- Run UTC: 2026-05-14 08:33 UTC
- Seed class: data-first anomaly (USGS earthquake feeds)
- Testable question: Has the global count of USGS-classed significant earthquakes in the latest day/week dropped versus broader monthly baseline enough to matter for near-term response posture?

## Candidate packet
1) **Question**: Is there a short-window lull in significant global quake activity?
2) **Required checks**:
   - USGS significant_day count
   - USGS significant_week count
   - USGS significant_month count/baseline composition
3) **Falsifier**: If significant_day or significant_week show multiple high-impact events at publish time, lull claim fails.
4) **Target datasets**: USGS GeoJSON summary feeds (significant_day/week/month; all_day context)

## Evidence ledger
- Observation: significant_day `count=0` (generated 1778747501000).
  - Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson
  - Limitation: rolling 24h window; can change quickly.
- Observation: significant_week `count=1` (Brawley, CA M4.7) at generation 1778747529000.
  - Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson
  - Limitation: significance score is USGS-specific, not a universal impact metric.
- Observation: significant_month `count=5`; includes prior events in Japan (M7.4), Nevada, Missouri, California.
  - Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson
  - Limitation: monthly window includes older shocks and does not indicate immediate current operational load.
- Context observation: all_day feed `count=233`, including at least one M4.7 event (Iran), showing seismic activity persists outside USGS “significant” bucket.
  - Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
  - Limitation: all_day includes many microquakes; not directly comparable to “significant” classification.

## Claim-evidence matrix
- Claim: No USGS “significant” earthquakes were listed in the past day at snapshot time.
  - Status: supported
- Claim: Past-week significant activity was limited to one event.
  - Status: supported
- Claim: This is a short-window lull, not zero seismic risk.
  - Status: supported (all_day count remains high)

## Could this be wrong because...
- Disconfirming hypothesis: Feed updated after snapshot with a newly classified significant event.
- Invalidating evidence: significant_day count >0 at or before publication timestamp.
- Result: not found at snapshot time; residual update risk remains.

## Selection rationale
- Published as a short-window operational signal with explicit provisional language due to high refresh rate and methodology sensitivity.