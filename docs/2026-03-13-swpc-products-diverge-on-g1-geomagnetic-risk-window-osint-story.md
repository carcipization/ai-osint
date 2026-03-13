# SWPC products diverge on March 13–14 G1 geomagnetic-risk window, lowering short-horizon confidence (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-13-swpc-products-diverge-on-g1-geomagnetic-risk-window-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-13-swpc-products-diverge-on-g1-geomagnetic-risk-window-osint-story.md)

**Dateline:** 2026-03-13 15:01 UTC

Initial lead: follow-up recheck of NOAA SWPC geomagnetic-risk products after a prior G1-window forecast.

## Story
NOAA’s Space Weather Prediction Center is currently signaling mixed guidance for the March 13–14 minor-storm window: its machine-readable planetary K-index forecast now tops out below the G1 threshold, while its text forecast products still describe likely or expected G1 periods.

The strongest disconfirming evidence appears in SWPC’s forecast JSON feed, where the highest projected Kp value is 4.67 and no Kp≥5 slot appears in the parsed window. SWPC’s observed K-index feed also shows recent realized values peaking at 4.67. By contrast, SWPC’s 3-day geomagnetic text forecast still includes one 5.00 Kp interval and 40% minor-storm probabilities for March 13 and March 14, and its latest forecast discussion continues to say periods of G1 storming are expected.

The likely mechanism for this mismatch is product-timing desynchronization across SWPC output channels rather than a fully settled forecast reversal, though SWPC’s discussion also notes a newly analyzed CME signature expected to pass below Earth’s orbit, which can reduce Earth-impact risk from that specific ejecta.

The decision consequence is operational: grid, satellite, and GNSS users should treat this as a lower-confidence storm window and key off the next synchronized SWPC update cycle before escalating beyond routine minor-storm readiness.

What could overturn this: a subsequent SWPC cycle that realigns all products around Kp≥5 would restore higher confidence in a realized G1 interval.

## Appendix: Method
- Reframed testable question for follow-up: do current SWPC products still align on G1-threshold risk for March 13–14?
- Pulled four first-party SWPC artifacts: observed Kp JSON, forecast Kp JSON, 3-day geomagnetic text forecast, and forecast discussion text.
- Recomputed threshold test mechanically (`any(forecast_kp >= 5.0)`) and compared with text-product language.
- Ran contradiction pass: attempted to disprove downgrade thesis by checking whether updated SWPC text still asserts G1 conditions (it does).

## Appendix: Limitations
- SWPC products update on different schedules, so temporary divergence can reflect release timing rather than true forecast conflict.
- JSON parsing here uses current rolling feed window and may include or exclude near-boundary rows as files refresh.
- This story assesses forecast coherence, not end-state geophysical impacts.

## Appendix: Confidence
**Confidence:** Medium

Rationale: high confidence that current SWPC products are internally divergent at check time; medium confidence on ultimate event-level intensity because the divergence may resolve quickly in either direction.

## Appendix: Sources
- SWPC observed planetary K-index JSON: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- SWPC forecast planetary K-index JSON: [https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- SWPC 3-day geomagnetic forecast text: [https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt](https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt)
- SWPC forecast discussion text: [https://services.swpc.noaa.gov/text/discussion.txt](https://services.swpc.noaa.gov/text/discussion.txt)
- NOAA space weather scales explanation: [https://www.swpc.noaa.gov/noaa-scales-explanation](https://www.swpc.noaa.gov/noaa-scales-explanation)
