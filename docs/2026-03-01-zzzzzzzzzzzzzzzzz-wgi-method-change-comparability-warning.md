# Claim check: “WGI year-over-year changes can be read directly without vintage checks”

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-01-zzzzzzzzzzzzzzzzz-wgi-method-change-comparability-warning.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-01-zzzzzzzzzzzzzzzzz-wgi-method-change-comparability-warning.md)

**Dateline:** 2026-03-01 21:06 UTC

## Executive summary
- This claim is **unsafe/partly incorrect** for current WGI use.
- World Bank documentation for the 2025 WGI edition states methodological updates and historical recalculation back to 1996.
- Practical implication: analysts should avoid naive cross-vintage comparisons without checking methodology/version notes.

## Evidence
Primary/official project page states:
- 2025 edition introduces updates to source screening, indicator mapping, and aggregation model.
- Historical estimates were recalculated back to 1996 for consistency.

Sources:
- World Bank WGI home/publication page: [https://www.worldbank.org/en/publication/worldwide-governance-indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators)
- WGI DataBank endpoint: [https://databank.worldbank.org/source/worldwide-governance-indicators](https://databank.worldbank.org/source/worldwide-governance-indicators)
- Methodology reference (WGI update paper index): [https://ideas.repec.org/p/wbk/wbrwps/10952.html](https://ideas.repec.org/p/wbk/wbrwps/10952.html)

## Assessment
**Verdict:** Treat “simple year-over-year WGI movement” claims with caution unless the analysis explicitly controls for vintage/method updates.

This is not saying WGI is unusable; it means interpretation discipline matters more when methodology and back-series recalculation have changed.

## Why this matters for OSINT
Governance indicators are commonly used to support geopolitical risk narratives. If vintage effects are ignored, analysts can overstate trend breaks or policy impacts.

## Limitations
- This check validates methodology-change risk, not country-specific trend direction.
- Full country-level re-estimation impact requires downloading and comparing affected series directly.
