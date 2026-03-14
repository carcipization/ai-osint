# NOAA SWPC escalates geomagnetic storm warning to G2 (Moderate) after earlier G1 cycle (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-14-noaa-swpc-escalates-geomagnetic-storm-warning-to-g2-moderate-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-14-noaa-swpc-escalates-geomagnetic-storm-warning-to-g2-moderate-osint-story.md)

**Dateline:** 2026-03-14 00:01 UTC

Initial lead: NOAA Space Weather Prediction Center operational alert stream (`alerts.json`) showing late-cycle threshold escalation.

## Story
NOAA’s Space Weather Prediction Center escalated its March 13–14 geomagnetic event guidance from G1 to G2, issuing a K-index 6 warning and then a K-index 6 threshold alert late Friday UTC.

The strongest direct evidence is SWPC’s alert feed: a `K06W` warning at 23:38 UTC tagged “NOAA Scale: G2 - Moderate,” followed by a `K06A` alert at 23:39 UTC stating the K-index 6 threshold was reached at 23:40 UTC. Earlier products in the same sequence were `K05W`/`K05A` (G1), indicating a formal severity step-up rather than a continuity update.

A near-term contradiction remains in machine-readable observed K-index values, which at this check still showed a latest reported value of 5.67 in the planetary K-index feed. That mismatch can occur when alert issuance leads slower rolling observation updates, so the key verified fact is the official SWPC warning/alert escalation itself.

The decision consequence is operational and immediate: grid and satellite operators who were treating this as a minor-storm window now need to run moderate-storm contingencies until the current warning window is superseded, while aviation and high-latitude GNSS-dependent users should monitor subsequent SWPC updates more tightly.

What could overturn this: a rapid SWPC downgrade/cancellation in the next update cycle would reduce escalation duration, but it would not negate that a G2 threshold warning/alert was issued and triggered.

## Appendix: Method
- Pulled SWPC `alerts.json` and sorted by issuance time to reconstruct event sequence (K05 -> K06 products).
- Extracted exact timestamps and threshold statements from `K06W` and `K06A` messages.
- Cross-checked SWPC observed planetary K-index JSON for latest reported values at check time.
- Used NOAA scales page for impact framing consistency.

## Appendix: Limitations
- SWPC alerts are operational and can be revised quickly; validity windows may be shortened or extended.
- Observed K-index feed can lag alert issuance, creating temporary product desynchronization.
- This report assesses warning/alert escalation and immediate implications, not post-event damage outcomes.

## Appendix: Confidence
**Confidence:** Medium-High

Rationale: high confidence in official SWPC escalation products and timestamps; medium confidence in short-window intensity persistence because active alerts can change rapidly.

## Appendix: Sources
- SWPC Alerts feed: [https://services.swpc.noaa.gov/products/alerts.json](https://services.swpc.noaa.gov/products/alerts.json)
- SWPC observed planetary K-index JSON: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- NOAA space weather scales explanation: [https://www.swpc.noaa.gov/noaa-scales-explanation](https://www.swpc.noaa.gov/noaa-scales-explanation)
