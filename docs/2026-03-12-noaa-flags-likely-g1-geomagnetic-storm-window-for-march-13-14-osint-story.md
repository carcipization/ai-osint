# NOAA flags likely G1 geomagnetic-storm window for March 13–14 after quieter run-up (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-12-noaa-flags-likely-g1-geomagnetic-storm-window-for-march-13-14-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-12-noaa-flags-likely-g1-geomagnetic-storm-window-for-march-13-14-osint-story.md)

**Dateline:** 2026-03-12 03:35 UTC

Initial lead: NOAA Space Weather Prediction Center forecast surfaces highlighting elevated geomagnetic risk into March 13 ([SWPC homepage](https://www.swpc.noaa.gov/)).

## Story
NOAA forecasters now expect the strongest geomagnetic conditions of the next three days to reach Kp 5, the threshold for a G1 (Minor) geomagnetic storm, after a recent stretch that stayed mostly below storm level.

In the agency’s 0030 UTC forecast, the greatest expected three-hour Kp value for March 12–14 is 5.00 (G1). A companion geomagnetic forecast assigns a 40% minor-storm probability on both March 13 and March 14, with forecast Ap values rising to 20 on those days.

That marks a modest but clear step up from near-term observations. NOAA’s recent planetary K-index feed showed a last-24-hour maximum below G1 and a last-7-day peak of 4.67, just under the storm threshold. In practical terms, the signal is less about extreme space weather and more about a short operational window where low-level effects become more plausible.

NOAA’s forecast discussion attributes the shift to the expected onset of a co-rotating interaction region/coronal-hole high-speed stream (CIR/CH HSS) around midday March 13, with unsettled to active conditions and likely G1 intervals continuing into March 14.

Why it matters: a G1 event is classified by NOAA as minor, but it can still nudge decisions for grid and satellite operators that run short-horizon risk checks. NOAA’s own scale describes possible weak power-grid fluctuations and minor satellite-operation impacts at this level.

What could overturn this conclusion: if updated SWPC runs downgrade the stream’s impact or real-time Kp observations stay below 5 through March 14, this would remain a near-miss rather than a realized minor storm window.

## Appendix: Method
- Pulled NOAA SWPC text products (`3-day-forecast.txt`, `3-day-geomag-forecast.txt`, `discussion.txt`) and extracted issuance times, Kp thresholds, Ap forecasts, and stated mechanism.
- Cross-checked machine-readable SWPC products for observed and forecast planetary K-index values.
- Recomputed recent observed context (last 24h and last 7d maxima) against the Kp=5 G1 threshold.
- Used NOAA scales documentation for event-level impact framing.

## Appendix: Limitations
- Forecast guidance can revise as upstream solar-wind conditions change.
- Current machine-readable forecast shows limited duration at Kp 5, so impact intensity may stay patchy.
- This analysis relies on NOAA products and does not independently model magnetospheric response.

## Appendix: Confidence
**Confidence:** Medium

Rationale: High confidence in quoted NOAA product outputs and threshold arithmetic; medium confidence in realized impacts because the event signal is forecast-led and near the lower storm boundary.

## Appendix: Sources
- NOAA SWPC 3-day forecast (text): [https://services.swpc.noaa.gov/text/3-day-forecast.txt](https://services.swpc.noaa.gov/text/3-day-forecast.txt)
- NOAA SWPC 3-day geomagnetic forecast (text): [https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt](https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt)
- NOAA SWPC forecast discussion (text): [https://services.swpc.noaa.gov/text/discussion.txt](https://services.swpc.noaa.gov/text/discussion.txt)
- NOAA SWPC observed planetary K-index JSON: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- NOAA SWPC forecast planetary K-index JSON: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- NOAA Space Weather Scales explanation: [https://www.swpc.noaa.gov/noaa-scales-explanation](https://www.swpc.noaa.gov/noaa-scales-explanation)
