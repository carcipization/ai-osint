# Dataset Strategy (finding stories in data)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/dataset-strategy.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/dataset-strategy.md)


**Dateline:** 2026-02-27  
**Status:** Living guide

## Purpose
Use this when you **don’t** have a specific claim yet and need to surface high-value story candidates from datasets.

This is exploration strategy, not claim-verification procedure (that lives in `dataset-playbook.md`).

## Core loop

1. **Map domains**: geopolitics, mobility, procurement, ownership, censorship, hazard, AI infra.
2. **Scan for discontinuities**: level shifts, slope changes, concentration jumps, decouplings.
3. **Cross-domain triangulate**: test whether multiple independent domains move together.
4. **Score candidate stories**: novelty, stakes, verifiability, timeliness.
5. **Promote top candidates** into formal claim-check workflow.

## What to hunt for

### 1) Breaks in baseline
- Sudden jump/drop vs rolling baseline
- Structural break after policy/event boundary
- Persistent deviation (not one-off noise)

### 2) Concentration shifts
- Spend/traffic/ownership moving into fewer entities
- New hub emergence
- Sudden dominance reversal

### 3) Decouplings
- Two metrics that usually track each other diverge
- Narrative says "up" while operational proxy says "flat/down"
- Policy intent vs observed behavior mismatch

### 4) Cross-border reroutes
- Flows move through intermediaries after sanctions/policy pressure
- Alternate corridors appear with lagged confirmation in other datasets

### 5) Synchrony across independent systems
- Similar timing across mobility + procurement + network metadata
- Suggests coordinated underlying process worth testing

## Candidate scoring rubric (fast)

Score each 1–5:

- **Signal strength** (clear discontinuity?)
- **Independent corroboration** (available?)
- **Public interest/stakes**
- **Actionability** (can we publish a tight claim now?)
- **False-positive risk** (invert this score)

Prioritize candidates with high signal + high corroboration + medium/low FP risk.

## Pattern libraries (useful combinations)

### Mobility + sanctions/trade
- ADS-B/AIS + OpenSanctions + UN Comtrade
- Good for reroutes, chokepoint stress, designation-response lag.

### Unrest + censorship
- ACLED/UCDP + OONI + local official statements
- Good for "street activity vs network control" coupling.

### Procurement + ownership
- TED/USAspending/Contracts Finder + OpenOwnership/PSC/OpenCorporates
- Good for vendor concentration and related-entity patterns.

### Hazard + infrastructure
- IBTrACS/FIRMS + maritime/port traffic + advisories
- Good for separating hazard-driven disruption from policy/security narratives.

### Narrative network drift
- TGStat/Telemetr/TGDataset + event timeline + independent reporting
- Good for identifying bridge channels and coordinated amplification windows.

## Weird/obscure source trade-offs

### Behavioral derivatives
Examples: AIS/ADS-B inferred behaviors, anchorage states.

- **Pro:** early signal.
- **Con:** inference errors.
- **Use:** trigger + corroborate, not standalone proof.

### Technical side-effects
Examples: OONI interference measurements.

- **Pro:** direct mechanism clues.
- **Con:** probe-distribution bias.
- **Use:** pair with independent reporting/official statements.

### Research corpora snapshots
Examples: TGDataset.

- **Pro:** strong historical/graph baselines.
- **Con:** not live; scope constraints.
- **Use:** structure/context, not real-time truth.

### Aggregator mega-feeds
Examples: OpenSanctions, GDELT, OpenCorporates.

- **Pro:** broad discovery speed.
- **Con:** inherited upstream errors/latency.
- **Use:** discovery/prioritization; verify against primaries before strong claims.

## Escalation rule (to playbook)

Escalate a candidate into `dataset-playbook.md` workflow only if:

- it can be written as one falsifiable claim,
- at least two independent sources are available,
- and one plausible null explanation can be tested quickly.

If not, keep it in watchlist mode.

## Anti-patterns

- Forcing causal language from correlational scans.
- Publishing one-feed anomalies with no controls.
- Chasing novelty over reproducibility.
- Ignoring release/revision mechanics.

## Output format for scouts

For each candidate, record:

- **Claim stub** (one sentence)
- **Observed anomaly** (what changed + window)
- **Datasets used**
- **Null test to run next**
- **Initial confidence** (low/medium/high)

Keep scout outputs terse; promote only high-quality candidates.
