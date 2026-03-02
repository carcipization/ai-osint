# Suez Canal in early 2026: checking the “~60% down” transit claim with primary AIS-derived data

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-02-suez-canal-first-week-2026-transits-down-60-percent-claim-check.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-02-suez-canal-first-week-2026-transits-down-60-percent-claim-check.md)

**Dateline:** 2026-03-02 06:34 UTC

## Claim (evaluated)
A shipping-industry report says: **“In the first week of 2026, Suez Canal transits were still around 60% below the same week in 2023.”**

## Verdict
**Directionally supported, magnitude slightly overstated in this replication window.**

Using IMF PortWatch daily chokepoint transit-call data (AIS-derived), I get:
- **2023-01-01 to 2023-01-07:** 498 total transits (n_total)
- **2026-01-01 to 2026-01-07:** 241 total transits (n_total)
- Change: **-51.6%**

That is a very large sustained decline versus pre-diversion baseline, but below a literal 60% in this exact Jan 1–7 window. Different week definitions (rolling 7-day windows, reporting-week conventions, vessel-class weighting, DWT weighting) can move the percentage.

## Claim provenance
- **Outlet / quoted source:** Splash247 (quoting BIMCO analyst Niels Rasmussen)
- **Claim URL:** [https://splash247.com/suez-traffic-still-60-down-100-days-after-last-houthi-attack/](https://splash247.com/suez-traffic-still-60-down-100-days-after-last-houthi-attack/)
- **Claim timestamp:** 2026-01-08 (page publication date)

## Evidence and method
### Primary dataset used
- IMF PortWatch — Daily Chokepoint Transit Calls and Trade Volume Estimates (Feature Service):
  - Item page: [https://www.arcgis.com/sharing/rest/content/items/42132aa4e2fc4d41bdaf9a445f688931?f=json](https://www.arcgis.com/sharing/rest/content/items/42132aa4e2fc4d41bdaf9a445f688931?f=json)
  - Service endpoint: [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer)

### Reproducible query (Suez chokepoint records for 2023 + 2026)
[https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint1%27%20AND%20year%20IN%20(2023%2C2026](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint1%27%20AND%20year%20IN%20(2023%2C2026))&outFields=date%2Cyear%2Cmonth%2Cday%2Cn_total%2Ccapacity&returnGeometry=false&resultRecordCount=5000

### Replication arithmetic
- Sum `n_total` for `portid='chokepoint1'`, 2023-01-01..2023-01-07: **498**
- Sum `n_total` for `portid='chokepoint1'`, 2026-01-01..2026-01-07: **241**
- Percent change = (241 − 498) / 498 = **-51.6%**

## Why this is still OSINT-significant
Even with a stricter replication window yielding ~52% (not ~60%), the signal indicates a persistent post-2023 structural diversion away from the Suez route in aggregate transit calls. In operational monitoring, that size of gap is materially significant for routing cost, lead times, and vessel-demand balance.

## Limitations
- The claim references BIMCO analysis; BIMCO’s exact internal week/window and weighting logic may differ from this Jan 1–7 replication.
- PortWatch is AIS-derived and subject to signal quality, classification choices, and post-hoc revisions.
- `n_total` (count of transits) is not equivalent to economic value, ton-mile demand, or revenue impact.
- This check does not infer causality for each transit change; it evaluates scale consistency of the public claim.

## Confidence
- **High confidence** in the directional conclusion (transits far below 2023 baseline).
- **Medium confidence** in exact percent-point reconciliation with the quoted “~60%” due to week-definition and weighting differences.
