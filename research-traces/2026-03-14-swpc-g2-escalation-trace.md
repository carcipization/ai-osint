# STORY_B trace — SWPC escalation from G1 to G2 geomagnetic warning

**Date:** 2026-03-14
**Question tested:** Did NOAA SWPC escalate the March 13–14 geomagnetic event from G1 to G2, and is that materially decision-relevant?

## Importance adjudication
- **Affected actors:** electric-grid operators, satellite operators, aviation/GNSS-dependent users at higher geomagnetic latitudes.
- **Action delta:** move from routine minor-storm monitoring (G1) to heightened moderate-storm readiness checks (G2), including stricter short-horizon contingency posture.
- **Public consequence:** broader potential impact footprint (down to ~55° geomagnetic latitude in SWPC warning text) and higher chance of service perturbations than earlier G1 framing.
- **Convenience-check note:** selected over easier continuity-only updates because this is a formal threshold escalation in official warning/alert products with direct operational consequences.

## Last-72h duplicate gate
- Related recent posts exist on G1 watch/warning.
- **Material delta present:** SWPC issued K06 warning + K06 alert (G2 - Moderate), which is a threshold change from prior G1 framing.
- Duplicate verdict: **not duplicate**.

## Evidence ledger

### Observation (direct)
1. SWPC Alerts JSON
   - URL: https://services.swpc.noaa.gov/products/alerts.json
   - Checked: 2026-03-14 00:02 UTC
   - Findings:
     - `K06W` warning issued 2026-03-13 23:38 UTC (`NOAA Scale: G2 - Moderate`, valid to 2026-03-14 06:00 UTC).
     - `K06A` alert issued 2026-03-13 23:39 UTC with threshold reached 23:40 UTC (`NOAA Scale: G2 - Moderate`).
     - Earlier same day products were `K05W`/`K05A` (G1), confirming escalation sequence.
   - Limitation: operational alerts can be updated/extended quickly.

2. SWPC observed planetary K-index JSON
   - URL: https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json
   - Checked: 2026-03-14 00:02 UTC
   - Finding: latest feed value at check time was Kp 5.67; recent 24–48h maxima in that feed were 5.67.
   - Limitation: feed cadence can lag near-immediate alert issuance.

3. NOAA scales explanation
   - URL: https://www.swpc.noaa.gov/noaa-scales-explanation
   - Used for impact framing consistency between G1 and G2 descriptions.

### Inference
- Official SWPC warning/alert threshold moved from Kp 5 (G1) to Kp 6 (G2), indicating higher expected/realized disturbance severity than prior-cycle framing.

### Unknown
- Whether subsequent update cycles extend, downgrade, or further escalate after the current valid window.

## Contradiction pass
- Counter-thesis: this is just another minor-storm continuation and not materially different.
- Result: falsified by direct K06 warning/alert products and explicit NOAA scale change to G2.

## Could this be wrong because...
- Near-term alerts can be quickly superseded; if SWPC rapidly cancels/downgrades K06 products, escalation may be brief.
- Mitigation: story framed as time-stamped escalation in official products, with explicit update sensitivity.
