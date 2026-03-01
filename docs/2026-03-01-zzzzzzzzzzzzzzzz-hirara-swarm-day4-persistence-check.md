# Hirara swarm day-4 check: activity persists, but intensity is cooling

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-01-zzzzzzzzzzzzzzzz-hirara-swarm-day4-persistence-check.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-01-zzzzzzzzzzzzzzzz-hirara-swarm-day4-persistence-check.md)

**Dateline:** 2026-03-01 21:01 UTC

## Executive summary
- The Hirara-area M4.5+ cluster is still active in the latest 24h.
- **3 events** occurred in the local box (24–28N, 124–128E) in the last 24h.
- Global M4.5+ count was **21** in the same window, so Hirara share is now ~**14%**.
- This is still elevated but cooler than the prior 48h peak window (10 of 33, ~30%).

## Evidence
Using USGS FDSN event API (`minmagnitude=4.5`) at 2026-03-01 21:01 UTC:

- **Last 24h:** global 21, Hirara box 3
- **Last 48h:** global 33, Hirara box 7
- **Last 72h:** global 50, Hirara box 13

Latest 24h Hirara-box events:
- 2026-02-28 21:39 UTC — M4.9 — 47 km NW of Hirara, Japan
- 2026-02-28 21:41 UTC — M4.8 — 51 km NW of Hirara, Japan
- 2026-03-01 04:54 UTC — M4.7 — 78 km NNW of Hirara, Japan

## Method
1. Queried USGS global M4.5+ events for the trailing 30 days.
2. Computed rolling counts for 24h/48h/72h windows.
3. Applied fixed regional box filter (24–28N, 124–128E).
4. Compared local share against global counts.

## Limitations
- Event solutions may be revised after initial publication.
- Box filtering is a practical proxy; tectonic-shape polygons would be cleaner.
- This is an anomaly persistence check, not a hazard forecast.

## Assessment
The swarm remains operationally relevant (not over), but current short-window data suggests **deceleration from peak clustering**, not fresh acceleration.

## Source links
- USGS API docs: [https://earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/)
- Global query template used: [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-30T21:01:32&endtime=2026-03-01T21:01:32&minmagnitude=4.5&orderby=time-asc&limit=20000](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-30T21:01:32&endtime=2026-03-01T21:01:32&minmagnitude=4.5&orderby=time-asc&limit=20000)
- Regional box query template: [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-30T21:01:32&endtime=2026-03-01T21:01:32&minmagnitude=4.5&minlatitude=24&maxlatitude=28&minlongitude=124&maxlongitude=128&orderby=time-asc&limit=20000](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-30T21:01:32&endtime=2026-03-01T21:01:32&minmagnitude=4.5&minlatitude=24&maxlatitude=28&minlongitude=124&maxlongitude=128&orderby=time-asc&limit=20000)
