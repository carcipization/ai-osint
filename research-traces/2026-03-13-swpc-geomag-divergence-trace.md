# STORY_B trace — SWPC geomagnetic-risk product divergence

**Date:** 2026-03-13
**Question tested:** Do NOAA SWPC products still support a likely G1 geomagnetic-storm window for March 13–14?

## Candidate and duplication gate (last 72h)
- Related recent post: `2026-03-12-noaa-flags-likely-g1-geomagnetic-storm-window-for-march-13-14-osint-story`.
- Material delta found: official SWPC product disagreement now exists between machine-readable Kp forecast outputs and text discussion/forecast language.
- Duplication decision: **not a duplicate**; this run reports a new contradiction that changes operational confidence.

## Evidence ledger

### Observation (direct)
1. SWPC planetary K-index forecast JSON
   - URL: https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json
   - Checked: 2026-03-13 15:01 UTC
   - What it shows: maximum forecast Kp value in current feed = 4.67; no Kp>=5 interval in parsed rows.
   - Limitation: feed is rolling and can revise; window composition can shift intraday.

2. SWPC observed planetary K-index JSON
   - URL: https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json
   - Checked: 2026-03-13 15:01 UTC
   - What it shows: recent observed maximum 4.67; latest observed value 4.67 at 09:00 UTC.
   - Limitation: short-horizon context; does not itself forecast upcoming slots.

3. SWPC 3-day geomagnetic forecast (text)
   - URL: https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt
   - Issued: 2026-03-12 22:05 UTC
   - What it shows: includes one Kp=5.00 interval (13 Mar 15–18UT) and 40% minor-storm probabilities on 13/14 Mar.
   - Limitation: issuance time older than latest discussion; text and JSON products can desynchronize.

4. SWPC forecast discussion (text)
   - URL: https://services.swpc.noaa.gov/text/discussion.txt
   - Issued: 2026-03-13 12:30 UTC
   - What it shows: still states periods of G1 (Minor) storming expected on 13–14 Mar; notes CME analysis suggests ejecta passes below Earth’s orbit.
   - Limitation: narrative discussion does not provide full slot-by-slot Kp table.

### Inference
- Current SWPC products are not fully synchronized on threshold risk: machine-readable Kp forecast implies sub-G1 peak, while text products still describe likely/periodic G1.

### Unknown
- Whether the divergence reflects feed-latency timing, product update sequencing, or a pending consolidated forecast revision.

## Contradiction pass
- Strongest counter-thesis: G1 risk still valid because authoritative SWPC text products continue to state it.
- Result: counter-thesis is supported by text products, but challenged by machine-readable Kp forecast and recent observed values.
- Reporting choice: publish contradiction explicitly and downgrade confidence to medium.

## Could this be wrong because...
- The JSON forecast may lag or lead textual products around issuance boundaries.
- A later SWPC cycle could restore Kp>=5 and resolve divergence in the opposite direction.
- Mitigation: time-stamp all product checks and frame as synchronization divergence, not definitive cancellation.
