# Panama Canal FY2025 rebound claim: can we verify the reported +19.3% transit jump?

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzz-panama-canal-fy2025-transit-rebound-claim-check.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-02-zzzzzzzzzzzzzzzzzzzzzz-panama-canal-fy2025-transit-rebound-claim-check.md)

**Dateline:** 2026-03-02 06:50 UTC

## Claim (evaluated)
A travel-industry post claims the Panama Canal Authority reported FY2025 vessel transits rose **19.3% to 13,404 ships** versus FY2024.

## Verdict
**Supported (for the official-reporting claim), with methodology caveat for third-party AIS replication.**

The Panama Canal Authority publication explicitly states FY2025 transits were **13,404**, up **19.3%** from **11,240** in FY2024. An independent AIS-derived chokepoint series (IMF PortWatch) also shows a strong year-over-year increase for Panama Canal crossings over the same fiscal-year framing, supporting the direction and scale of recovery even though absolute counts differ by source definition.

## Claim provenance
- Claim source type: Secondary claim (industry article citing primary authority figures)
- Claim URL: [https://adept.travel/news/2025-12-03-panama-canal-cruises-2026](https://adept.travel/news/2025-12-03-panama-canal-cruises-2026)
- Primary-source corroboration URL: [https://pancanal.com/en/panama-canal-maintains-operational-and-financial-strength/](https://pancanal.com/en/panama-canal-maintains-operational-and-financial-strength/)
- Key claim checked: FY2025 transits increased 19.3% to 13,404 from 11,240 in FY2024.

## Evidence
1. **Panama Canal Authority (primary statement):** reports FY2025 transits = **13,404**, FY2024 = **11,240**, and YoY change = **+19.3%**.  
   [https://pancanal.com/en/panama-canal-maintains-operational-and-financial-strength/](https://pancanal.com/en/panama-canal-maintains-operational-and-financial-strength/)

2. **IMF PortWatch AIS-derived chokepoint dataset (independent directional check):**
   - Service: [https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer)
   - Panama Canal port id: `chokepoint2`
   - Fiscal-year aggregation (Oct–Sep) from daily `n_total`:
     - FY2024: **9,012**
     - FY2025: **10,984**
     - Change: **+21.9%**

3. **Context source for cruise-season framing (not used for arithmetic):**
   [https://pancanal.com/en/panama-canal-cruise-season-2025-2026-begins/](https://pancanal.com/en/panama-canal-cruise-season-2025-2026-begins/)

## Reproducible query (PortWatch)
Panama Canal daily rows for 2023–2025:

[https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint2%27%20AND%20year%20IN%20(2023%2C2024%2C2025)&outFields=year%2Cmonth%2Cday%2Cn_total&returnGeometry=false&orderByFields=year%2Cmonth%2Cday&resultRecordCount=2000](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?f=json&where=portid%3D%27chokepoint2%27%20AND%20year%20IN%20(2023%2C2024%2C2025)&outFields=year%2Cmonth%2Cday%2Cn_total&returnGeometry=false&orderByFields=year%2Cmonth%2Cday&resultRecordCount=2000)

## Analysis
This check confirms the concrete numeric claim as stated by the canal authority. Independent AIS-derived chokepoint counts also indicate a strong rebound in FY2025, with a similar magnitude of improvement (+21.9%). That convergence is a meaningful OSINT signal: two different measurement systems agree on a substantial post-drought recovery trend.

## Limitations
- The claim is verified as a statement of **official Panama Canal figures**; this does not independently audit canal accounting systems.
- PortWatch `n_total` and authority transit totals are not guaranteed to be definitionally identical (coverage, classification, timing cutoffs, and revision policies may differ).
- Fiscal-year boundary assumptions (Oct–Sep) were applied consistently for replication, but alternative periodization can shift percentages.
- This check does not predict future drought restrictions or booking reliability outcomes.

## Bottom line
The published claim that Panama Canal FY2025 transits rose **19.3% to 13,404** is **supported** by the primary authority source, and independently consistent with AIS-derived chokepoint trend data showing a comparably strong year-over-year rebound.