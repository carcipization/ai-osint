# DATASETS_OPTIMIZE trace — 2026-03-10 21:01 UTC

Scope: catalog quality/structure improvements only (no dataset additions, no docs publication).

Edits made to `docs/datasets-catalog.md`:
1. Updated dateline to current optimization pass time.
2. Expanded **Catalog maintenance rules** with two structural guardrails:
   - Canonical-entry preference for city-level incident feeds to avoid mirror duplication.
   - Version-date retention and supersession caveat for date-stamped datasets.
3. Added **Municipal-feed comparability protocol** under freshness/revision governance:
   - Within-city trend-first usage.
   - Cross-city normalization requirement.
   - Confidence cap when definition history is unstable.

Why:
- Recent catalog growth in municipal/public-safety datasets increases risk of false comparability and duplicate city mirrors.
- These rules improve retrieval hygiene and reduce downstream story-quality errors without changing catalog scope.
