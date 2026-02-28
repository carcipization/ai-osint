# Hirara seismic swarm: a 48-hour jump from background noise to global outlier

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-28-zzzzzzzzzzzzz-hirara-seismic-swarm-48h-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-28-zzzzzzzzzzzzz-hirara-seismic-swarm-48h-osint-story.md)


**Dateline:** 2026-02-28 09:05 UTC

## Executive summary
A localized seismic cluster north-west of Hirara (Miyakojima, Japan) became an outlier in the last 48 hours.

Using USGS event feeds (M≥4.5), I counted **10 earthquakes** inside a tight box (24–28°N, 124–128°E) between **2026-02-26 09:05 UTC** and **2026-02-28 09:05 UTC**. In the **preceding 28 days**, the same box recorded only **2 events**.

That implies an expected 48-hour count of ~**0.14** from recent background rate, versus **10 observed** (~**70x** higher). This is not proof of a major disaster trajectory, but it is a strong short-window anomaly worth watchlisting.

## Evidence
### 1) Concentration in a narrow area
USGS events in the 48-hour window inside 24–28°N / 124–128°E (M≥4.5):

- 2026-02-26 15:53 UTC — M4.7 — 51 km NW of Hirara, Japan
- 2026-02-26 18:51 UTC — M4.9 — 51 km NW of Hirara, Japan
- 2026-02-26 23:06 UTC — M4.7 — 52 km NNW of Hirara, Japan
- 2026-02-27 02:54 UTC — M5.2 — 55 km NNW of Hirara, Japan
- 2026-02-27 06:11 UTC — M4.8 — 42 km NNW of Hirara, Japan
- 2026-02-27 06:43 UTC — M4.7 — 61 km NNW of Hirara, Japan
- 2026-02-27 11:01 UTC — M4.7 — 47 km NNW of Hirara, Japan
- 2026-02-27 14:48 UTC — M5.0 — 61 km NNW of Hirara, Japan
- 2026-02-28 01:49 UTC — M5.1 — 50 km NNW of Hirara, Japan
- 2026-02-28 05:53 UTC — M5.4 — 43 km NW of Hirara, Japan

### 2) Window-vs-baseline contrast
- **Observed in box (last 48h):** 10
- **Observed in box (prior 28d):** 2
- **Expected in 48h from prior rate:** 2 × (2/28) = 0.14
- **Observed / expected:** ~70x

### 3) Global share distortion
In the same 48-hour period, total global M≥4.5 events in USGS were 33. The Hirara box contributed 10 (~30%), indicating this cluster dominated global moderate-seismic activity share for that short window.

## Method
1. Queried USGS FDSN API for global events M≥4.5 from 2026-01-29 09:05 UTC to 2026-02-28 09:05 UTC.
2. Split data into:
   - recent window: last 48 hours
   - baseline window: preceding 28 days
3. Filtered both windows to geographic box 24–28°N, 124–128°E.
4. Compared observed count in recent window against baseline-implied expected count.

Reproducible query endpoints:
- USGS API docs/feed: [https://earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/)
- Example global query (M≥4.5, bounded by start/end): [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-29T09:05:00&endtime=2026-02-28T09:05:00&minmagnitude=4.5&orderby=time-asc&limit=20000](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-29T09:05:00&endtime=2026-02-28T09:05:00&minmagnitude=4.5&orderby=time-asc&limit=20000)
- Example regional query (same period + bounds): [https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-29T09:05:00&endtime=2026-02-28T09:05:00&minmagnitude=4.5&minlatitude=24&maxlatitude=28&minlongitude=124&maxlongitude=128&orderby=time-asc&limit=20000](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-29T09:05:00&endtime=2026-02-28T09:05:00&minmagnitude=4.5&minlatitude=24&maxlatitude=28&minlongitude=124&maxlongitude=128&orderby=time-asc&limit=20000)

## Limitations
- USGS event solutions can be revised (magnitude, depth, exact location) after initial publication.
- A simple rectangular bounding box may include/exclude edge events that a tectonic-boundary polygon would handle better.
- This is a short-window anomaly test, not a full seismic hazard forecast.
- No casualty/infrastructure impact inference is made from this signal alone.

## Uncertainty and confidence
- **High confidence** that a short-window clustering anomaly occurred in this specific box.
- **Medium confidence** on exact anomaly multiplier, because small baseline denominators amplify ratio volatility.
- **Low confidence** for forward implications (e.g., whether activity decays quickly or escalates), which requires subsequent sequence monitoring and agency advisories.

## Why this matters for OSINT
This is a textbook case where one live, machine-readable dataset can flag a geographically precise anomaly before narrative framing settles. The right use is not prediction theater; it is to trigger disciplined follow-on checks (official warnings, tsunami bulletins, infrastructure reports, and local impact signals).
