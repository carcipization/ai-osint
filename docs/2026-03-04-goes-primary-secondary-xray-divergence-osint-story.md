# NOAA GOES X-ray feeds briefly diverged as primary stream dropped to zero while secondary remained non-zero

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-04-goes-primary-secondary-xray-divergence-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-04-goes-primary-secondary-xray-divergence-osint-story.md)

**Dateline:** 2026-03-04 09:06 UTC

NOAA Space Weather Prediction Center (SWPC) one-day GOES X-ray feeds showed a short divergence window in which the primary stream reported zero flux while the secondary stream continued to report non-zero values.

In a timestamp-matched comparison of 0.1–0.8nm channel records, 39 of 1,437 common timestamps met that condition. The divergence concentrated in two windows: 2026-03-03 09:03–09:39 UTC and 2026-03-04 08:58–08:59 UTC.

During the divergence minutes, primary records in this sample carried `electron_contaminaton=true`, while matched secondary samples were non-zero and not flagged contaminated. Separately, SWPC geomagnetic products showed a Kp=5 (G1) period on 2026-03-03 21:00 UTC, indicating an operationally active space-weather day rather than a fully quiet baseline period.

This is a data-behavior observation, not a claim of instrument fault.

## Appendix: Method

- Pulled SWPC one-day GOES X-ray JSON feeds for `primary` and `secondary`.
- Filtered to energy channel `0.1-0.8nm`.
- Joined on `time_tag`.
- Counted cases where `primary.flux == 0` and `secondary.flux > 0`.
- Reviewed contamination flags and contiguous time windows.

## Appendix: Limitations

- Short-window observation; not a provider incident determination.
- No causal attribution to hardware or pipeline failure.
- Persistence needs re-checking in future windows.

## Appendix: Confidence

**Medium.** Timestamped divergence is directly observable in feed data, but cause attribution requires provider-side technical context.

## Appendix: Sources

1. [SWPC GOES primary X-rays (1 day)](https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json)
2. [SWPC GOES secondary X-rays (1 day)](https://services.swpc.noaa.gov/json/goes/secondary/xrays-1-day.json)
3. [SWPC planetary K-index product](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
4. [SWPC alerts feed](https://services.swpc.noaa.gov/products/alerts.json)
