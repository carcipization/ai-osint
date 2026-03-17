# NOAA issues G2 geomagnetic storm watch for March 19 after March 16 CME

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-17-noaa-issues-g2-geomagnetic-storm-watch-for-march-19-after-march-16-cme-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-17-noaa-issues-g2-geomagnetic-storm-watch-for-march-19-after-march-16-cme-osint-story.md)

**Dateline:** 2026-03-17 13:42 UTC

## Story

Initial lead: [NOAA SWPC bulletin — G2 Moderate Geomagnetic Storm Watch Issued](https://www.swpc.noaa.gov/news/g2-moderate-geomagnetic-storm-watch-issued-1).

NOAA’s Space Weather Prediction Center has issued a **G2 (moderate) geomagnetic storm watch for March 19 (UTC day)** after a coronal mass ejection (CME) on March 16, according to the agency’s watch bulletin and machine-readable alert feed. For power operators, satellite teams, and high-latitude aviation and communications planners, this is a concrete short-horizon risk window rather than routine background variability.

The strongest current mechanism is NOAA’s own CME-impact pathway: SWPC’s watch message links the March 19 risk window to CME material launched on March 16 and states potential impacts can include power-grid fluctuations, satellite orientation irregularities, and high-frequency radio fading at higher latitudes. SWPC’s planetary K-index forecast also projects a jump into storm territory on March 19, with predicted Kp values reaching **6.33 (G2)** in the 06:00 UTC interval.

Decision consequence is immediate and broad enough for non-specialists: utilities and satellite-dependent services should tighten contingency posture for the March 19 window, and travelers in high-latitude routes should expect some possibility of communications or navigation degradation if forecast intensity verifies.

What could overturn this: if CME arrival is weaker or delayed versus current modeling, observed Kp could remain below G2 and reduce the practical disruption risk.

## Appendix: Method

- Framed testable question: did NOAA move from background/low-end space-weather conditions to a new moderate-storm watch with explicit timing and operational implications?
- Pulled primary evidence from SWPC’s official news bulletin and `alerts.json` machine-readable stream (`WATA30` watch entries).
- Cross-checked forecast trajectory in SWPC `noaa-planetary-k-index-forecast.json`, including predicted storm-scale intervals for March 19.
- Contradiction pass: reviewed recent observed Kp values, which were mostly below storm thresholds on March 17, and treated elevated impacts as forecast-conditional rather than observed-now.

## Appendix: Limitations

- This is a forecast-led operational watch; realized impacts depend on CME arrival timing, orientation, and coupling conditions that can change close to event time.
- Kp forecast bins are model outputs and can revise before and during the event window.
- This report does not independently model region-by-region grid or satellite vulnerability.

## Appendix: Confidence

**Confidence: Medium.**

Confidence is high that NOAA issued the watch and specified the risk window and impact classes; confidence is moderate on realized severity because the key peak conditions are still forecast, not yet observed.

## Appendix: Sources

- [NOAA SWPC: G2 Moderate Geomagnetic Storm Watch Issued (2026-03-16 21:15 UTC)](https://www.swpc.noaa.gov/news/g2-moderate-geomagnetic-storm-watch-issued-1)
- [NOAA SWPC alerts JSON (`WATA30` watch messages)](https://services.swpc.noaa.gov/products/alerts.json)
- [NOAA SWPC planetary K-index forecast JSON](https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json)
- [NOAA SWPC planetary K-index observed JSON](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json)
- [NOAA space weather scales explainer](https://www.swpc.noaa.gov/noaa-scales-explanation)
