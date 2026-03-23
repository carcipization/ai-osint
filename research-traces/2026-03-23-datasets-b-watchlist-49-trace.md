# DATASETS_B Trace — 2026-03-23 01:42 UTC

Slot: DATASETS_B (datasets-only publish)

## Discovery and screening

Primary search set:
- `site:catalog.data.gov "Mineral Commodity Summaries 2025 - POTASH Data Release"`
- `site:catalog.data.gov "Mineral Commodity Summaries 2025 - PHOSPHATE ROCK Data Release"`
- `site:catalog.data.gov "Mineral Commodity Summaries 2025 - NITROGEN (FIXED)-AMMONIA Data Release"`
- `site:catalog.data.gov fertilizer price dataset USDA`

Additional verification via CKAN API:
- `https://catalog.data.gov/api/3/action/package_search` used to resolve full dataset slugs and metadata_modified timestamps.

## Selected additions (3)

1) POTASH Data Release (MCS 2025)
- URL: https://catalog.data.gov/dataset/mineral-commodity-summaries-2025-potash-data-release-30a24
- metadata_modified: 2026-01-22T09:26:22.731917
- Selection reason: direct fertilizer-input concentration denominator with broad downstream food-cost relevance.

2) PHOSPHATE ROCK Data Release (MCS 2025)
- URL: https://catalog.data.gov/dataset/mineral-commodity-summaries-2025-phosphate-rock-data-release-d59a6
- metadata_modified: 2026-01-22T09:26:12.066347
- Selection reason: feedstock-level fertilizer chain exposure useful for import/trade shock interpretation.

3) NITROGEN (FIXED)-AMMONIA Data Release (MCS 2025)
- URL: https://catalog.data.gov/dataset/mineral-commodity-summaries-2025-nitrogen-fixed-ammonia-data-release-06a7f
- metadata_modified: 2026-01-22T09:25:42.149609
- Selection reason: key nitrogen-fertilizer risk baseline linking energy/logistics stress to farm-input affordability.

## Rejected/deferred candidates

- Generic MCS aggregate tables already in catalog (world production/capacity/reserves) were not re-added.
- Non-fertilizer MCS commodity pages (e.g., precious/base metals) deferred to avoid diluting consequence-first focus for current food-input risk chain.

## Consequence-first check

All selected datasets map to non-specialist outcomes:
- farm input costs,
- food price pressure,
- planning under supply-route disruption.

## Blocked/errors log (required)

- Source: catalog.data.gov
  URL: https://catalog.data.gov/dataset/mineral-commodity-summaries-2025-mineral-industry-trends-and-salient-statistics-data-relea
  Error: 404-like fetch failure (truncated slug endpoint)
  UTC: 2026-03-23T01:39:56Z
  Retry: failed (same issue); resolved by querying CKAN API for full slug, then deprioritized for this batch.

- Source: catalog.data.gov
  URL: https://catalog.data.gov/dataset/mineral-commodity-summaries-2025-potash-data-release
  Error: web_fetch returned non-readable script payload/failed extraction in one attempt
  UTC: 2026-03-23T01:39:56Z
  Retry: succeeded via CKAN API + full slug resolution.
