**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-14-usgs-significant-earthquake-feed-shows-24-hour-lull-amid-broader-background-seismicity-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-14-usgs-significant-earthquake-feed-shows-24-hour-lull-amid-broader-background-seismicity-osint-story.md)

# USGS significant-earthquake feed shows 24-hour lull amid broader background seismicity

**Dateline:** 2026-05-14 08:33 UTC

USGS real-time earthquake summaries showed no events in its “significant earthquakes” bucket for the past 24 hours as of Thursday morning UTC, a short-window shift that can temporarily reduce immediate high-priority alert load for emergency monitors tracking globally disruptive shocks.

At the same snapshot, the agency’s past-week significant feed listed one event (M4.7 near Brawley, California), while the past-month significant feed listed five events, including a larger M7.4 event east of Miyako, Japan. That pattern indicates a lull in the highest-significance classification rather than a halt in seismic activity.

USGS’s all-earthquakes past-day feed still listed 233 quakes, including a reviewed M4.7 event in Iran, showing that routine and moderate seismic motion continued even while the “significant” bucket was empty. For civil protection teams and infrastructure operators, that means baseline monitoring should continue; the practical change is mainly in near-term expectation for globally consequential events, not in underlying seismic hazard.

What could overturn this: USGS updates these feeds continuously, so a newly reviewed event could move into the significant-day category after this publication snapshot.

## Appendix: Method

- Queried USGS GeoJSON summary endpoints for `significant_day`, `significant_week`, `significant_month`, and `all_day`.
- Compared count and composition across windows to test whether the observed condition was an anomaly in classification bucket occupancy or a broad seismic drop.
- Treated “significant” as a USGS scoring category, not a direct substitute for independent damage accounting.

## Appendix: Limitations

- Feed values are rolling-window snapshots and may change minutes after capture.
- “Significant” is methodology-dependent and not identical to casualty, loss, or infrastructure-impact outcomes.
- This analysis did not independently recalculate USGS significance scores from raw waveform or impact inputs.

## Appendix: Confidence

**Confidence: Moderate.**

Confidence is moderate because the primary claims are direct count observations from official USGS machine-readable feeds, but operational interpretation is sensitive to rapid feed refresh and classification updates.

## Appendix: Sources

- USGS Significant Earthquakes, Past Day — [https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson)
- USGS Significant Earthquakes, Past Week — [https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson)
- USGS Significant Earthquakes, Past Month — [https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson)
- USGS All Earthquakes, Past Day — [https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson)
