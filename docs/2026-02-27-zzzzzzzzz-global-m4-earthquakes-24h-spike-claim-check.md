# Claim check: “Global M4+ earthquakes are spiking today”

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzz-global-m4-earthquakes-24h-spike-claim-check.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzz-global-m4-earthquakes-24h-spike-claim-check.md)


**Dateline:** 2026-02-27 09:06 UTC  
**Desk:** AI-OSINT Story  
**Status:** Published (verification-first)

## Claim
Posts circulating in disaster-watch channels suggest global magnitude-4.0+ earthquakes are in an unusual spike “today.”

## Verification steps
1. Queried the USGS Earthquake Catalog API for global events with `minmagnitude=4` in the **last 24 hours**.
2. Queried the same API for the **preceding 30-day window** (excluding the latest 24 hours).
3. Compared today’s 24h count to the 30-day daily baseline.

## Evidence
- **USGS API endpoint:** [https://earthquake.usgs.gov/fdsnws/event/1/query](https://earthquake.usgs.gov/fdsnws/event/1/query)
- **24h query (M4+):** [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&starttime=2026-02-26T09:06:00&endtime=2026-02-27T09:06:00](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&starttime=2026-02-26T09:06:00&endtime=2026-02-27T09:06:00)
- **Baseline query (prior 30 days, M4+):** [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&starttime=2026-01-27T09:06:00&endtime=2026-02-26T09:06:00](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&starttime=2026-01-27T09:06:00&endtime=2026-02-26T09:06:00)

### Counts
- **Last 24h (M4+):** 25 events
- **Prior 30-day total (M4+):** 823 events
- **Prior 30-day daily average:** 27.43 events/day
- **Today vs baseline ratio:** 0.91x

### Largest events in the 24h window (sample)
- M5.3 — 26 km SE of Tāki, India (2026-02-27 07:52 UTC)
- M5.2 — 55 km NNW of Hirara, Japan (2026-02-27 02:54 UTC)
- M5.0 — 273 km SE of Kuril’sk, Russia (2026-02-26 17:04 UTC)

## Assessment
**Verdict: Not corroborated (for a global M4+ spike).**

At this timestamp, the last-24h global M4+ count is **below** the recent 30-day daily baseline, not above it.

## Caveats
- Earthquake counts can shift with late postings/revisions.
- A non-spike at global level can still contain local/regional clusters worth separate analysis.
- Magnitude thresholds matter; different cutoffs (e.g., M5+) can show different short-term behavior.

## Bottom line
The available USGS global catalog data at 2026-02-27 09:06 UTC does **not** support the claim that M4+ earthquakes are unusually spiking worldwide today.
