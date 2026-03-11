# NOAA GOES X-ray divergence persisted as primary feed printed zeros while secondary remained non-zero (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-11-goes-primary-zero-secondary-nonzero-divergence-persisted-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-11-goes-primary-zero-secondary-nonzero-divergence-persisted-osint-story.md)

**Dateline:** 2026-03-11 15:01 UTC

## Story
A divergence seen earlier this month in NOAA Space Weather Prediction Center (SWPC) GOES X-ray feeds reappeared on March 11: the primary 0.1–0.8nm stream printed zero values while the secondary stream stayed non-zero at the same timestamps.

In a timestamp-matched one-day comparison, 61 of 1,437 common 0.1–0.8nm samples met that condition. The divergence was concentrated in a contiguous 60-minute block from 08:48 to 09:47 UTC, plus one additional point at 14:48 UTC.

This pattern is more consistent with feed-quality behavior than with a true collapse in solar X-ray output. During 60 of the 61 divergence points, the primary record carried `electron_contaminaton=true`, while the paired secondary records remained above zero.

What could overturn this: a SWPC provider note showing the secondary stream was degraded during the same timestamps, or a revised feed backfill removing these timestamp-level mismatches.

Why it matters: operations teams using automated space-weather triggers should not treat primary-feed zeros as standalone physical quiet conditions when the secondary feed remains non-zero. A practical mitigation is to add a fallback rule: if primary is zero and contamination is flagged, verify against secondary before issuing downstream “quiet” conclusions.

## Appendix: Method
- Pulled SWPC one-day JSON feeds for GOES primary and secondary X-rays.
- Filtered both feeds to energy channel `0.1-0.8nm`.
- Joined by `time_tag` and counted rows where `primary.flux == 0` and `secondary.flux > 0`.
- Grouped qualifying timestamps into contiguous windows to test whether divergence was random or clustered.
- Checked primary `electron_contaminaton` flag prevalence during divergence points.
- Pulled SWPC planetary K-index product for contextual activity level only.

## Appendix: Limitations
- This is a one-day rolling-window analysis; counts can shift as the window advances.
- `electron_contaminaton` flag semantics are provider-defined; this report describes observed association, not root-cause attribution.
- No direct SWPC incident bulletin was identified in this pass explaining feed behavior.

## Appendix: Confidence
**Confidence:** Medium

The divergence condition is directly observable and reproducible from first-party timestamped feeds. Confidence is lower on causal explanation because provider-side diagnostics were not available in this check.

## Appendix: Sources
1. SWPC GOES primary X-rays (1 day): [https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json](https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json)
2. SWPC GOES secondary X-rays (1 day): [https://services.swpc.noaa.gov/json/goes/secondary/xrays-1-day.json](https://services.swpc.noaa.gov/json/goes/secondary/xrays-1-day.json)
3. SWPC planetary K-index product: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)