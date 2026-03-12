# Research Trace — ONE-OFF STORY (2026-03-12 03:31 Europe/London)

## Situational-awareness brief (mandatory)
Timestamp window: 2026-03-12 03:31–03:34 Europe/London

Search terms + top developments:
- `Reuters world news March 2026 energy disruption shipping attacks latest`
  - Reuters: Oil up nearly 5% as fresh attacks on ships in Strait of Hormuz (https://www.reuters.com/business/energy/us-oil-prices-up-nearly-3-middle-east-crisis-constrains-supply-2026-03-10/)
- `US TSA checkpoint travel numbers latest March 2026`
  - TSA passenger volumes page (https://www.tsa.gov/travel/passenger-volumes)
- `NOAA space weather geomagnetic storm alert March 2026`
  - NOAA SWPC homepage/forecast surfaces show elevated geomagnetic potential into March 13 (https://www.swpc.noaa.gov/)

Candidate lanes from brief:
1. Hormuz disruption -> shipping/energy market stress (freshness high, baseline comparability medium, data availability medium)
2. TSA throughput trend (freshness high, comparability high, but duplicate risk high due very recent in-repo TSA stories)
3. NOAA space weather geomagnetic forecast threshold crossing (freshness high, comparability high, decision surface clear for grid/satellite/HF operators)

Selected lane: NOAA geomagnetic forecast (best availability + clear threshold/decision surface + lower duplication risk).

## Testable proposition
NOAA’s latest operational products indicate a transition from mostly sub-storm geomagnetic conditions to a likely G1 (Minor) storm window on March 13–14, enough to justify short-horizon operational watchfulness without implying severe-grid conditions.

## Evidence ledger

1) URL: https://services.swpc.noaa.gov/text/3-day-forecast.txt  
Publisher: NOAA SWPC  
Timestamp: `:Issued: 2026 Mar 12 0030 UTC`  
What it proves: Greatest expected 3-hour Kp for Mar 12–14 is `5.00 (NOAA Scale G1)`; prior 24h observed max Kp was 4.  
Class: Observation  
Limitations: Forecast product (forward-looking) and can be revised.

2) URL: https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt  
Publisher: NOAA SWPC  
Timestamp: `:Issued: 2026 Mar 11 2205 UTC`  
What it proves: Minor-storm probability jumps to `40%` on Mar 13 and `40%` on Mar 14; forecast Ap rises to `20` for both days.  
Class: Observation  
Limitations: Probabilistic and method-sensitive to solar-wind evolution.

3) URL: https://services.swpc.noaa.gov/text/discussion.txt  
Publisher: NOAA SWPC  
Timestamp: `:Issued: 2026 Mar 12 0030 UTC`  
What it proves: Forecast mechanism cites CIR/CH HSS onset around midday Mar 13; states G1 likely and persistence through Mar 14.  
Class: Observation (mechanism statement from forecaster)  
Limitations: Mechanism is model-informed expert forecast, not direct future observation.

4) URL: https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json  
Publisher: NOAA SWPC services  
Timestamp: pulled 2026-03-12 ~03:33 UTC  
What it proves: Last 7 days observed Kp max `4.67`; last 24h max below G1 threshold.  
Class: Observation  
Limitations: Rolling window; retrospective updates possible.

5) URL: https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json  
Publisher: NOAA SWPC services  
Timestamp: pulled 2026-03-12 ~03:33 UTC  
What it proves: Forecast peak `Kp 5.00` appears in one interval (`2026-03-13 15:00:00`, labeled G1).  
Class: Observation  
Limitations: Single-interval threshold touch does not guarantee prolonged storm conditions.

6) URL: https://www.swpc.noaa.gov/noaa-scales-explanation  
Publisher: NOAA SWPC  
Timestamp: fetched 2026-03-12 ~03:34 UTC  
What it proves: G1 is “Minor”; expected impacts include weak grid fluctuations and minor satellite-operation impacts.  
Class: Observation  
Limitations: Scale descriptions are generalized and not event-specific.

## Contradiction pass
Disconfirming hypothesis sought: forecast uplift may be routine noise, not a meaningful anomaly.

Findings:
- Counter-evidence exists: expected peak is only G1 (minor), with only one forecast interval at Kp 5 in current machine-readable forecast.
- This reduces severity framing; story must avoid implying broad severe disruption.
- Nonetheless, threshold-crossing from recent sub-G1 observed values + explicit CH HSS mechanism supports a limited, operationally relevant update.

## Could this be wrong because...
- Top disconfirming hypothesis: CH HSS onset arrives weaker/later than forecast and Kp remains below 5.
- Invalidating evidence needed: updated SWPC runs removing G1 likelihood or observed Kp staying sub-5 through Mar 14.
- Status: not yet available at publication time.

## Last-72h overlap / duplication check
Checked recent STORY posts in `docs/` (last 72h) — topics were Fed/TGA/TSA; no recent space-weather story lane overlap found. Not a duplicate.

## Decision
Publish STORY with moderate confidence and explicit caveat that this is a minor-threshold operational watch signal, not a severe event.
