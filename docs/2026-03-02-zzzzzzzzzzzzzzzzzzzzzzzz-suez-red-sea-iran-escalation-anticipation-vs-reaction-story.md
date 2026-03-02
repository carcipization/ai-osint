# Suez and Red Sea shipping before the Iran shock: anticipation or just reaction?

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzzzz-suez-red-sea-iran-escalation-anticipation-vs-reaction-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzzzz-suez-red-sea-iran-escalation-anticipation-vs-reaction-story.md)

**Dateline:** 2026-03-02 06:51 UTC

## Why this matters
The core policy/logistics question is not only whether traffic changed after the Iran strikes, but whether carriers and routing patterns were already positioning for a wider regional war risk before the shooting started.

## Event timeline (UTC)

- **2026-02-03** — Maersk/Hapag-Lloyd announce one Gemini service (ME11) would resume transiting the Red Sea/Suez from mid-February, under naval-assistance/security conditions, with explicit contingency language if security deteriorates.  
  - Maersk release: [https://www.maersk.com/news/articles/2026/02/03/first-gemini-service-to-transit-the-red-sea](https://www.maersk.com/news/articles/2026/02/03/first-gemini-service-to-transit-the-red-sea)  
  - Reuters write-up: [https://www.reuters.com/business/maersk-hapag-lloyd-transit-red-sea-with-one-their-shared-services-2026-02-03/](https://www.reuters.com/business/maersk-hapag-lloyd-transit-red-sea-with-one-their-shared-services-2026-02-03/)

- **2026-02-27** — Maersk says it will temporarily reroute some sailings around the Cape of Good Hope due to “unforeseen constraints” in the Red Sea operating environment.  
  - Reuters: [https://www.reuters.com/world/middle-east/maersk-reroutes-some-sailings-around-africa-due-unforeseen-constraints-in-red-2026-02-27/](https://www.reuters.com/world/middle-east/maersk-reroutes-some-sailings-around-africa-due-unforeseen-constraints-in-red-2026-02-27/)

- **2026-02-28** — Reuters live coverage reports U.S.-Israeli strikes on Iran and regional retaliation.  
  - Reuters live file: [https://www.reuters.com/world/iran-crisis-live-explosions-tehran-israel-announces-strike-2026-02-28/](https://www.reuters.com/world/iran-crisis-live-explosions-tehran-israel-announces-strike-2026-02-28/)

- **2026-03-01 01:40 UTC (Reuters timestamp)** — Reuters bulletin says Iranian state media confirmed Khamenei was killed in the strikes.  
  - Reuters bulletin: [https://www.reuters.com/world/middle-east/irans-supreme-leader-khamenei-killed-iranian-state-media-confirm-2026-03-01/](https://www.reuters.com/world/middle-east/irans-supreme-leader-khamenei-killed-iranian-state-media-confirm-2026-03-01/)

## Transit evidence (high-frequency chokepoint data)
Source class: IMF PortWatch daily chokepoint AIS series.

- Dataset service root: [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer)
- Series used:
  - `chokepoint1` = Suez Canal
  - `chokepoint7` = Cape of Good Hope (substitute route proxy)
  - `chokepoint4` = Bab el-Mandeb (threat-gate context)

### Reproducible query links
- Suez (`chokepoint1`), 2025–2026 daily totals:  
  [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint1%27%20AND%20year%20IN%20(2025%2C2026](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint1%27%20AND%20year%20IN%20(2025%2C2026))&outFields=year%2Cmonth%2Cday%2Cn_total&returnGeometry=false&orderByFields=year%2Cmonth%2Cday&resultRecordCount=5000
- Cape (`chokepoint7`), 2025–2026 daily totals:  
  [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint7%27%20AND%20year%20IN%20(2025%2C2026](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint7%27%20AND%20year%20IN%20(2025%2C2026))&outFields=year%2Cmonth%2Cday%2Cn_total&returnGeometry=false&orderByFields=year%2Cmonth%2Cday&resultRecordCount=5000
- Bab el-Mandeb (`chokepoint4`), 2025–2026 daily totals:  
  [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint4%27%20AND%20year%20IN%20(2025%2C2026](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint4%27%20AND%20year%20IN%20(2025%2C2026))&outFields=year%2Cmonth%2Cday%2Cn_total&returnGeometry=false&orderByFields=year%2Cmonth%2Cday&resultRecordCount=5000

### Data freshness check
Latest available date in these PortWatch series at publication time: **2026-02-22**.

That means the dataset does **not yet include** traffic for:
- the **2026-02-27** Maersk reroute announcement,
- the **2026-02-28** strikes,
- and **2026-03-01** confirmation shock.

## Pre-event vs post-event window comparison (explicit baseline + uncertainty)
Given data lag, we run a pre-shock structural comparison around the **2026-02-03** “partial return” advisory:

- **Baseline window:** 2026-01-06 to 2026-02-02 (28 days)
- **Comparison window:** 2026-02-03 to 2026-02-22 (20 days)
- Metric: daily `n_total`
- Uncertainty: bootstrap 95% CI for mean difference (5,000 resamples)

Results:

- **Suez Canal (`chokepoint1`)**
  - Baseline mean: **38.14 ships/day**
  - Comparison mean: **38.90 ships/day**
  - Difference: **+0.76/day** (**+2.0%**)
  - Bootstrap 95% CI (difference): **[-2.45, +4.05]**

- **Cape of Good Hope (`chokepoint7`)**
  - Baseline mean: **86.29 ships/day**
  - Comparison mean: **85.70 ships/day**
  - Difference: **-0.59/day** (**-0.7%**)
  - Bootstrap 95% CI (difference): **[-7.04, +5.96]**

Interpretation: before the kinetic Iran escalation window, we do not see a statistically clear shift in aggregate Suez-vs-Cape flows in PortWatch daily totals.

## Mechanism, actors, and incentives
- **Actors:** Global liners (Maersk/Hapag-Lloyd as directly observed), insurers/security partners, and naval escort frameworks.
- **Mechanism:** Route choice toggles between Suez and Cape based on expected security delay risk, not just fuel distance economics.
- **Incentives:**
  - Use Suez when security/escort conditions look manageable (shorter transit, better asset utilization).
  - Revert to Cape quickly when expected disruption uncertainty rises (schedule reliability and crew/cargo risk management).

The Feb 3 and Feb 27 advisories from the same carrier show exactly this two-way optionality.

## Disconfirming checks / counter-hypotheses
1. **Seasonality and ordinary network churn:** February routing variance may reflect normal schedule resets, weather, and alliance implementation effects, not geopolitical anticipation.
2. **Data revision and lag risk:** PortWatch is high-frequency but not same-day. Current lag (latest = Feb 22) blocks direct observation of post-strike reaction.
3. **Single-carrier advisory bias:** Maersk signals may not represent the full carrier universe simultaneously.
4. **Aggregate masking:** Daily chokepoint totals may hide composition shifts (e.g., container vs tanker) that matter for “war anticipation.”

## Did industry anticipate?
**Grade: Partial / Inconclusive (decision-relevant).**

Why:
- **Yes, partially:** The Feb 27 pre-strike reroute advisory indicates at least some operators were already managing elevated regional risk before the confirmed Iran-war escalation headlines.
- **But not proven at system level:** Aggregate Suez/Cape PortWatch totals through Feb 22 show no clear pre-shock break, and we cannot yet observe Feb 27 onward in this dataset.

So the strongest defensible claim now is: **carrier-level anticipation signals existed, but chokepoint flow data is still too lagged to confirm a broad industry-wide anticipation regime versus immediate reaction.**

## Limitations
- This publication is constrained by PortWatch availability through 2026-02-22 at run time.
- Reuters live page extraction can be sparse in machine-readable snapshots; timeline relies on Reuters page timestamps/dated bullets where available.
- No proprietary freight booking, war-risk premium, or insurer quote data were used in this pass.

## Confidence
**Moderate on carrier-behavior timeline; low-to-moderate on aggregate anticipation-vs-reaction attribution until post-2026-02-28 traffic data lands.**

## Bottom line
Current evidence does **not** support a clean “industry anticipated war escalation” or “industry only reacted after strikes” binary. The better reading is **partial anticipation at carrier decision level, with system-level traffic proof pending due to data lag**.