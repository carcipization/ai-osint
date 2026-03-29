# STORY_B trace — 2026-03-29 — Wheatstone LNG weeks-long repair signal

**Run window (UTC):** 2026-03-29 17:39–17:43  
**Slot:** STORY_B

## Dual-trigger sweep

### 1) World-state trigger (active developments)
Queries run:
- `Reuters March 29 2026 Narelle disrupting Australia LNG weakens tropical cyclone`
- `Reuters March 29 2026 diesel trucking slump update`
- `Reuters March 29 2026 DHS shutdown TSA update`
- `Reuters March 29 2026 Philippines WESM update`
- `Reuters March 29 2026 global food prices transport disruptions`

Top candidates identified:
1. **Australia LNG disruption duration shift** (new Reuters Mar 29: Wheatstone repairs likely to take weeks).
2. DHS/TSA shutdown operational strain updates (ongoing, but near-overlap with recent publication).
3. Continued diesel/trucking cost squeeze (already published this day in STORY_A slot).

### 2) Anomaly trigger (blind dataset/signal pass)
Checks attempted:
- LNG infrastructure status shift from short-term outage framing to explicit multi-week restoration horizon.
- Capacity concentration check using facility capacities in Reuters continuity coverage:
  - Wheatstone: 8.9 mtpa
  - Gorgon: 15.9 mtpa
  - North West Shelf: 14.3 mtpa

Result:
- **Anomaly gate PASS (qualitative duration anomaly):** event shifted from uncertain outage/restart status to explicit weeks-long impairment window at a major LNG facility.
- Quant baseline caveat: no independent real-time throughput dataset successfully pulled in this short window.

## Selection gates
- **Anomaly gate:** PASS (material duration change from outage uncertainty to multi-week repair timeline).
- **Mechanism gate:** PASS (storm damage extends LNG impairment despite partial normalization at Gorgon).
- **Decision gate:** PASS (importers/utilities/industrial buyers should plan for prolonged tightness, not immediate normalization).
- **Importance gate:** PASS (gas/electricity bill risk channel for non-specialists via global LNG tightness).

## Rejected candidates
- **DHS/TSA update:** rejected for STORY_B due near-duplicate framing risk with very recent publication and no hard throughput normalization/reversal datapoint in this run.
- **Diesel/trucking:** rejected due same-day publication in prior slot.
- **Philippines WESM:** rejected due no material mechanism delta in this run window.

## Bluesky pass (mandatory)
Distinct queries run (5):
1. `site:bsky.app trending.bsky.app feed Iran Negotiations`
2. `site:bsky.app trending.bsky.app feed cyclone`
3. `site:bsky.app LNG Australia cyclone Narelle`
4. `site:bsky.app energy prices March 2026 bsky.social`
5. `site:bsky.app power outage Australia March 2026 bsky.social`

Trending topics reviewed:
- `Iran Negotiations`
- `Iran Conflict`
- `Iran War`
- `Israel-Iran War`

Trend-derived query additions:
- Added energy-price and power-outage oriented Bluesky queries (4,5) from trend context linking conflict-energy and downstream service disruptions.

Dataset leads from Bluesky:
- None promoted this run (results were mostly JS-gated feed shells, low-signal profile pages, or stale/irrelevant posts).

## Polymarket pass (mandatory)
Distinct scans/queries run (3):
1. `site:polymarket.com predictions oil commodities march 2026`
2. `site:polymarket.com predictions natural gas`
3. `site:polymarket.com predictions geopolitics iran ceasefire`

How used:
- Expectation-shift context only; not used as factual evidence.

Limitations noted:
- Contract surfaces were fragmented with mixed horizon definitions.
- Search snippets often AI-summary style and can omit resolution details.
- Liquidity/contract framing heterogeneity limits direct inference.

## Source links used
- https://www.reuters.com/business/energy/chevron-says-repairs-wheatstone-gas-facility-take-weeks-2026-03-29/
- https://www.reuters.com/business/energy/australia-lng-disruptions-continue-after-narelle-thousands-without-power-2026-03-29/
- https://www.reuters.com/business/energy/chevron-reports-outage-australian-gas-facilities-due-cyclone-2026-03-26/
