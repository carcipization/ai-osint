# CBP watchlist-match mix shift in early FY2026: USBP share up, port-of-entry volume still high

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-cbp-tsds-encounter-mix-shift-early-fy2026-osint-story.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-cbp-tsds-encounter-mix-shift-early-fy2026-osint-story.md)

**Dateline:** 2026-03-06 06:09 UTC

## AP preflight (publishability gate)

1. **Why AP would run this today:** U.S. border security metrics are a live policy issue, and CBP’s own table now shows a notable shift in terrorism-related encounter composition at the start of FY2026.
2. **What is genuinely new:** The specific early-FY2026 pattern (USBP percentage increase to 0.0971% while OFO port-of-entry terrorism-related encounters are already near FY2025 totals) is a fresh data-point synthesis from primary tables.
3. **Who is affected / what changes:** Border-security policymakers, operational planners, and the public interpreting whether risk is changing versus denominator/method effects.
4. **Strongest “not a story” counterargument:** The signal could be mostly a partial-year denominator artifact, and TSDS-related records are not equivalent to confirmed terrorism offenses.
5. **Editor verdict:** **Publish** — the signal is material, caveated, and decision-relevant if framed explicitly as an early indicator rather than a settled trend.

## Why this update now

A newly updated CBP enforcement table (last modified Feb. 19, 2026) shows two concurrent facts that are easy to miss when read separately: a higher USBP watchlist-match share and still-heavy watchlist-match volume at legal land ports.

## Significance gate (why this matters)

- **If true (structural shift):** Screening burden is becoming more concentrated in specific channels/components, which can change staffing and intelligence-prioritization choices.
- **If false (artifact):** Public and policy narratives may over-read early, partial-year ratios.
- **Who is affected:** CBP component leadership, congressional oversight, local port operations, and media/policy consumers relying on top-line percentages.
- **Decision relevance:** Whether to interpret early FY2026 numbers as risk growth, process change, or denominator math directly affects resource-allocation arguments.

## Evidence (primary, linked)

1. **CBP Enforcement Statistics** (retrieved 2026-03-06 06:02 UTC) reports:
   - USBP terrorism-related encounters: **106 (FY25)** and **34 (FY26 to January)**.
   - USBP “Percentage of Total USBP Encounters”: **0.0287% (FY25)** vs **0.0971% (FY26 to January)**.
   - OFO land-port terrorism-related encounters (all nationalities): **4,011 (FY25)** vs **3,927 (FY26 to January)**.  
   Source: [CBP Enforcement Statistics](https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics)

2. **CBP methodological caveat on TSDS rows** (same table, retrieved 2026-03-06 06:02 UTC): terrorism-related records may include TSDS records; data are screening records and not standalone adjudications of criminal guilt.  
   Source: [CBP Enforcement Statistics — TSDS section notes](https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics)

3. **FBI watchlisting process context** (retrieved 2026-03-06 06:02 UTC): TSDS is a U.S. government screening dataset used for watchlisting and screening support; inclusion criteria and handling are process-governed and sensitive.  
   Source: [FBI Terrorist Watchlisting Transparency Document (PDF)](https://www.fbi.gov/file-repository/counterterrorism/terrorist-watchlisting-transparency-document-april-2024-050224.pdf)

## Method (reproducible)

- Scope: FY25 vs FY26-to-January values from the same CBP table to avoid cross-source denominator drift.
- Metric focus:
  - CBP-reported USBP percentage row (already normalized by component encounters).
  - Component-count comparison (USBP between ports vs OFO at land ports of entry).
- Falsification attempt:
  - Tested whether this can be dismissed as a single noisy monthly value; rejected because the reported shift appears in CBP’s own FY aggregate rows and is accompanied by a component-mix contrast (OFO still near prior-year totals by January).

## Hypotheses and adjudication

1. **Denominator compression hypothesis (supported):** USBP total encounters fell enough that a smaller absolute count can still produce a higher percentage.
   - Prediction: percentage can rise despite lower absolute USBP terrorism-related counts.
   - Test: CBP table shows exactly that pattern (34 vs 106 counts, but 0.0971% vs 0.0287%).

2. **Screening/process shift hypothesis (mixed):** detection prioritization or referral patterns changed, raising hit concentration in some channels.
   - Prediction: component mix should look uneven rather than uniformly down.
   - Test: OFO land-port terrorism-related encounters remain very high early in FY26 (3,927 by January), while USBP share behavior differs; this is directionally consistent but not conclusive.

3. **Artifact-only hypothesis (weakly supported):** apparent shift is mostly a reporting-window artifact and not operationally meaningful.
   - Prediction: all components should scale down similarly in early-year views.
   - Test: OFO near-full-year-equivalent volume by January weakens a pure artifact explanation, though partial-year caveats remain important.

## Limitations

- FY26 values are partial-year (to January) and may revise.
- TSDS-related encounters are screening matches/records context, not direct measures of prosecuted terrorism crimes.
- Cross-component comparability is constrained by different operating contexts (between ports vs land ports of entry).

## Confidence

**Medium.** The core pattern is directly in a primary CBP table, but interpretation risk is non-trivial due to partial-year timing and screening-data semantics.

## One-line decision relevance

Early FY2026 border-security interpretation should treat the watchlist signal as a **composition shift requiring component-level analysis**, not as a simple “up/down” headline.
