# Dataset intel: sanctions authority feeds set for cross-jurisdiction freshness monitoring (Watchlist 16)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-dataset-intel-sanctions-authority-feeds-watchlist-16.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-dataset-intel-sanctions-authority-feeds-watchlist-16.md)

**Dateline:** 2026-03-06 17:45 UTC

This run is a DATASETS one-off. Added/confirmed sanctions authority sources to support cross-jurisdiction freshness and reconciliation workflows.

## Added dataset set

1. **UN Security Council Consolidated List (XML)**  
   - URL: [https://scsanctions.un.org/resources/xml/en/consolidated.xml](https://scsanctions.un.org/resources/xml/en/consolidated.xml)  
   - Why it matters: primary multilateral sanctions baseline with machine-readable export.

2. **OFAC Sanctions List Service (SLS)**  
   - URL: [https://ofac.treasury.gov/sanctions-list-service](https://ofac.treasury.gov/sanctions-list-service)  
   - Why it matters: official U.S. sanctions distribution path and update anchor.

3. **Consolidated Canadian Autonomous Sanctions List (Global Affairs Canada)**  
   - URL: [https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)  
   - Why it matters: official Canada authority list with HTML/PDF/XML pathways.

## Catalog impact

- Section: **Ownership, sanctions, and procurement**
- Purpose: strengthen primary-source sanctions ingestion and freshness checks across U.S./Canada/UN authorities.

## Limitations

- Authorities have different legal scopes and publication pipelines; timing mismatches do not imply legal contradiction.
- Some endpoints expose transport-level file timestamps that may not equal substantive-list changes.

## Sources

- [UNSC consolidated list resources](https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list)
- [UNSC consolidated XML](https://scsanctions.un.org/resources/xml/en/consolidated.xml)
- [OFAC sanctions list service](https://ofac.treasury.gov/sanctions-list-service)
- [Global Affairs Canada consolidated sanctions page](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)
