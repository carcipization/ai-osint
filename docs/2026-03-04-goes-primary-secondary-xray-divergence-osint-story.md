# NOAA GOES X-ray feed divergence: primary stream briefly zeroed while secondary remained nominal

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-04-goes-primary-secondary-xray-divergence-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-04-goes-primary-secondary-xray-divergence-osint-story.md)

**Dateline:** 2026-03-04 09:06 UTC

## Story
Using SWPC 1-day GOES X-ray JSON feeds (0.1–0.8nm channel):

- Common timestamps compared: **1,437**
- Timestamps where primary flux was **0** while secondary flux was **>0**: **39**
- Divergence clustered in:
  - **2026-03-03 09:03–09:39 UTC** (37 minutes)
  - **2026-03-04 08:58–08:59 UTC** (2 minutes)
- In those divergence minutes, primary records show `electron_contaminaton=true`; secondary was reporting non-zero flux with contamination flag false in matched samples.

Context signal: SWPC geomagnetic products showed a **Kp=5 (G1)** period on 2026-03-03 21:00 UTC, confirming this was an operationally active space-weather window, not a fully quiet day.

## Appendix: Method
1. Pull both JSON feeds for 1-day X-ray data (`primary` and `secondary`).
2. Filter to energy channel `0.1-0.8nm`.
3. Join on `time_tag`.
4. Count timestamps where `primary.flux==0` and `secondary.flux>0`.
5. Inspect contamination flags and contiguous intervals.

## Appendix: Limitations
- This is a short-window observational check, not a NOAA incident report.
- We do not infer hardware fault; divergence may reflect expected correction/quality-control behavior.
- Findings should be re-checked in subsequent windows to determine persistence rate.

## Appendix: Confidence
**Medium.** The divergence event is directly observable and timestamped, but causal attribution (instrument behavior vs expected QC/filtering behavior) requires provider-side technical context.

## Appendix: Sources
- [SWPC GOES primary X-rays (1 day)](https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json)
- [SWPC GOES secondary X-rays (1 day)](https://services.swpc.noaa.gov/json/goes/secondary/xrays-1-day.json)
- [SWPC planetary K-index forecast/history product](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- [SWPC alerts feed](https://services.swpc.noaa.gov/products/alerts.json)
