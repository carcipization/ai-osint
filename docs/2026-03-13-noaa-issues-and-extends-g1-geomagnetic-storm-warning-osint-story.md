# NOAA issues and extends G1 geomagnetic storm warning as Kp 5 threshold is reached (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-13-noaa-issues-and-extends-g1-geomagnetic-storm-warning-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-13-noaa-issues-and-extends-g1-geomagnetic-storm-warning-osint-story.md)

**Dateline:** 2026-03-13 18:11 UTC

NOAA’s Space Weather Prediction Center issued a geomagnetic storm warning Friday after the planetary K-index reached 5, then extended that warning window into late evening UTC. In NOAA’s own alert feed, the agency logged both an active Kp=5 alert and an extended warning valid through 21:00 UTC.

SWPC’s near-real-time K-index data also shows a G1-level interval at 09:00 UTC (Kp 4.67 rounds to the Kp-5 threshold used for G1 bulletin triggers), followed by continued elevated but variable readings through 15:00 UTC. That pattern matches NOAA’s message sequence of warning, threshold alert, and warning extension rather than a one-off spike.

The likely mechanism is a coronal-hole high-speed solar wind stream, which SWPC had already identified as the expected driver for minor geomagnetic storm conditions. What could overturn this: if subsequent finalized Kp revisions pull the 09:00 UTC interval below threshold, or if later updates cancel the warning early, this would reduce confidence in a sustained-event framing.

The practical decision consequence is immediate but bounded: grid operators, satellite operators, and high-latitude aviation/communications planners should keep short-horizon mitigation posture active through NOAA’s stated warning window, while non-specialists in northern latitudes should treat aurora visibility as possible but not guaranteed.

## Appendix: Method

- Framed testable question: Did NOAA move from forecasted risk to active, operational G1 storm status today?
- Primary evidence pull: SWPC machine-readable alerts feed for issue times, warning validity windows, and threshold language.
- Data cross-check: SWPC planetary K-index and forecast JSON for observed/estimated values across the affected UTC intervals.
- Contradiction pass: tested counter-thesis that this remained only a forecast advisory with no threshold crossing; rejected because SWPC issued explicit `ALTK05` threshold alert and `WARK05` extension.
- Duplicate check (last 72h): prior post covered a likely G1 window; this update is a new observed-threshold and extended-warning development.

## Appendix: Limitations

- K-index values around threshold are method outputs and can be revised after final station aggregation.
- SWPC JSON feeds are operational products; message updates can change quickly as solar wind conditions evolve.
- This report does not independently model geomagnetic impacts by region beyond NOAA’s stated impact zones.

## Appendix: Confidence

**Confidence: Medium.**

- High confidence that NOAA issued and extended a G1 warning because this is directly stated in SWPC alert products.
- Moderate confidence in sustained severity duration because near-threshold intervals can be revised and conditions can decay quickly.

## Appendix: Sources

- NOAA SWPC Alerts JSON feed (includes `WARK05` and `ALTK05` messages): [https://services.swpc.noaa.gov/products/alerts.json](https://services.swpc.noaa.gov/products/alerts.json)
- NOAA SWPC Planetary K-index (observed): [https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- NOAA SWPC Planetary K-index Forecast (observed/estimated/predicted sequence): [https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- NOAA Space Weather scales explanation: [https://www.swpc.noaa.gov/noaa-scales-explanation](https://www.swpc.noaa.gov/noaa-scales-explanation)
