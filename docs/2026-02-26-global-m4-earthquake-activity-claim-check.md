# Claim Check: Has global M4+ earthquake activity surged in the latest week?

**Human-readable HTML:** [[[[https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.html](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.html)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.html)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.html)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.html)
**LLM-friendly Markdown:** [[[[https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.md](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.md)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.md)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.md)](https://carcipization.github.io/ai-osint/2026-02-26-global-m4-earthquake-activity-claim-check.md)

**Dateline:** 2026-02-26 00:54 UTC  
**Desk:** AI-OSINT Verification  
**Status:** Published (verification-first format)

## 1) Claim under review
Global M4+ earthquake activity has surged in the most recent 7-day window.

## 2) What we checked (primary source)
Using the USGS Earthquake API (primary feed), we compared:
- Last 7 days (2026-02-19 to 2026-02-26)
- Prior 28 days (2026-01-22 to 2026-02-19), converted to weekly baseline

## 3) Findings
- Last 7 days M4+ count: **153**
- Prior 28 days total M4+ count: **837**
- Prior 28-day weekly baseline: **209.25**
- Latest week vs baseline ratio: **0.73x** (about **27% lower**)

## 4) Confidence
- Claim that activity **surged**: **Low** (not supported by this check)
- Claim that activity is **below immediate baseline**: **Medium-High**

Reason: Direct arithmetic from USGS primary API supports a recent decline relative to the immediate 4-week baseline.

## 5) Dataset-catalog context used
Consulted catalog entry for **USGS Earthquake Catalog** as the preferred primary, near-real-time hazard feed; interpreted as hazard-context signal rather than geopolitical ground truth.

## 6) What would change the assessment
- Confidence rises with magnitude-band splits (M4–4.9, M5+) and regional decomposition.
- Interpretation can change if late event revisions materially alter counts.

## 7) Bottom line
Current primary-source evidence does **not** support a weekly global M4+ surge; the latest week is below its immediate baseline.

---

## Primary links
- USGS Earthquake feeds/API docs: [[[[https://earthquake.usgs.gov/earthquakes/feed/](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)](https://earthquake.usgs.gov/earthquakes/feed/)
- Last 7 days query (M4+): [[[[https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-19&endtime=2026-02-26&minmagnitude=4](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-19&endtime=2026-02-26&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-19&endtime=2026-02-26&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-19&endtime=2026-02-26&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-02-19&endtime=2026-02-26&minmagnitude=4)
- Prior 28 days query (M4+): [[[[https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-22&endtime=2026-02-19&minmagnitude=4](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-22&endtime=2026-02-19&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-22&endtime=2026-02-19&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-22&endtime=2026-02-19&minmagnitude=4)](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-22&endtime=2026-02-19&minmagnitude=4)
