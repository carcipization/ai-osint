# OSINT Journalism Skill

Purpose: produce high-quality automated OSINT journalism: fast, clear, evidence-based reporting that reads like publishable wire copy.

## Editorial north star

- Optimize for: **story quality**, **reporting reliability**, **publication speed**.
- Rules are tools, not outcomes.
- If a checklist step does not materially improve journalism, skip or shorten it.

## Quick operating mode

1. **Classify the task first**
   - Claim-check (specific claim + provenance URL)
   - OSINT story (new analysis, not a claim-check)
   - Follow-up (re-check prior posts; publish only material changes)
   - Dataset task (catalog addition/optimization)

2. **Pick evidence tiers**
   - Tier 1: official registry/agency/primary release
   - Tier 2: structured monitoring systems (Cloudflare Radar, IODA, OONI, PortWatch, etc.)
   - Tier 3: media/social/aggregators (lead generation)

3. **Set publication confidence**
   - Supported / Not supported / Partly supported / Inconclusive
   - Add explicit caveats for model-derived metrics and method-sensitive estimates

## Dataset intake policy (batch-first)

- Default to **bulk discovery** and **multi-add promotion**, not one-by-one additions.
- Discovery pass target: scan at least tens/hundreds of candidates per run when tooling allows.
- Promotion default: add **3–10 qualified datasets per cycle** (unless quality is genuinely thin).
- Adding only one dataset is unacceptable.
- Prioritize coverage breadth across domains before polishing niche depth.
- Do **not** run AP/story preflight or story publishability gates for dataset selection.

## Claim-check minimum standard

A claim-check must include all of the following before publication:

- `## Claim provenance`
- Direct post URL(s) being checked
- Dateline in exact format: `**Dateline:** YYYY-MM-DD HH:MM UTC`
- Source links in evidence section
- Limitation notes (measurement and update-lag risks)

If no concrete claim-source URL exists, **do not publish in claim-check format**.

## Anti-pattern filter (important)

Avoid weak “mainstream-wire-only + regulator page” checks unless a novel OSINT angle exists.

A piece is novel when it adds at least one of:
- Primary data pull or time-series reconstruction
- Cross-source synthesis that changes the conclusion
- Geospatial or registry linkage not present in headline coverage
- Non-obvious inference that materially extends public reporting

## Lead attribution rule (mandatory)

When the initial idea comes from an existing external story/report/post, always credit it and link it.

Required behavior:
- Add an explicit `Initial lead:` line near the top of STORY posts (immediately after dateline or first paragraph).
- Include outlet/author/account name + direct URL to the lead item.
- Keep attribution specific (do not use vague phrases like “reports said”).
- Separate attribution from contribution: state what new OSINT value this piece adds beyond the lead (new data pull, falsification, cross-source test, etc.).
- If multiple leads informed the idea, list the primary lead first and move others to Sources.

## Cybersecurity focus gate (hard)

Permanent exclusion: do not use CISA KEV as a dataset or story source. KEV-family topics are excluded from publication and dataset intake.

Default stance: cybersecurity is secondary unless the signal is operationally meaningful.

Do not publish cyber stories based only on small statistical drift (minor ratio/percentage movement) without concrete downstream implications.

A cybersecurity story is publishable only if at least one is true:
- active exploitation trajectory materially changed,
- high-severity exposure affects critical infrastructure or broad public attack surface,
- authoritative remediation/patch guidance diverges from observed exploitation reality,
- cross-source evidence indicates a genuine anomaly likely to change defender prioritization.

If none of the above are met, drop or defer the cyber candidate and prioritize other domains.

## Story significance gate (hard, all domains)

Do not publish descriptive drift without decision consequence.

A STORY candidate is publishable only if it passes all three gates:
1. **Anomaly gate:** signal is meaningfully outside expected variation (not routine noise/batch wobble).
2. **Mechanism gate:** plausible explanation tested against at least one artifact/null alternative.
3. **Decision gate:** identifies a concrete actor/action that should change because of this finding.

If a candidate fails any gate, discard it and continue searching.

STORY search rule:
- Keep looking for a publishable story until available datasets/source lanes for that run are exhausted.
- If exhausted and nothing passes all three gates, end with no publish (allowed).

## Story novelty and duplication gate (SKILL quality upgrade)

Do not publish a new story when it only rephrases a very recent conclusion from the same source lane.

Before drafting, run a **last-72h overlap check** against recent STORY posts:
- If headline claim, core metric, and actor/action implication are substantially unchanged, treat as duplicate and no-publish.
- A follow-on is publishable only with at least one material delta: new official release window, sign/regime change, threshold crossing, or a newly validated mechanism that changes action priority.
- Prefer “continuity noted in FOLLOWUP” over issuing near-duplicate STORY posts.
- In `research-traces/`, record one-line duplicate rationale when rejecting a candidate.

## Story format (AP style, mandatory)

Write story posts in AP-style narrative flow first, then append technical notes.

Plain-language rule (mandatory):
- Assume an informed general reader, not a specialist.
- Define acronyms and specialist terms at first mention (e.g., KEV, CVE, EPSS, BOD).
- Prefer concrete language over insider shorthand.

Required order:
1. Headline
2. Dateline
3. **Story** (clean narrative: lead, nut graf, key findings, implications)
4. **Appendix: Method**
5. **Appendix: Limitations**
6. **Appendix: Confidence**
7. **Appendix: Sources**

Do **not** include editorial throat-clearing in the story body (e.g., “why this is publishable”, “AP preflight”, internal gate checklists). If editorial justification is needed, store it in `research-traces/`.

## Method notes for internet-shutdown stories

When checking outage-duration claims:
- Separate **ordering conclusion** (A longer than B) from **exact-hour precision**.
- Treat decimal-hour values as method outputs unless independently recomputed.
- Look for partial-allowlist phases; “near zero” traffic can still coexist with whitelisted access.
- Triangulate at least two independent measurement families when possible:
  - routing/visibility signals
  - traffic/application-layer signals

## Follow-up slot discipline

- Sample recent high-impact stories (target 3–10, based on available time).
- FOLLOWUP runs do **not** publish docs posts.
- If there is a **meaningful update** (new primary data, official revision, materially changed conclusion), report it in Telegram summary and prioritize as a future STORY candidate.
- If no material updates, explicitly say so for sampled items in Telegram summary.
- **Cadence rotation rule (no exceptions):** always advance to the next slot after completing a FOLLOWUP sampling pass, even when no publishable update is found (no-op FOLLOWUP still rotates state).

## Feed rules (mandatory)

Publication policy source of truth: `/home/pi/.openclaw/workspace/ai-osint/policy/publication_policy.json`.

- Feed includes only STORY and DATASETS_INTEL publications.
- Exclude FOLLOWUP, SELF, SKILL, and DATASETS_OPTIMIZE entries from the public story feed.
- In feed-facing dataset headlines, use `Datasets: ...` (never `DATASETS_A/B/OPTIMIZE:` labels).
- Place dataset references at the bottom of index, below the feed (Datasets Catalog first, then Dataset Playbook).

## Publication header format (mandatory)

At the top of every published markdown post, include clickable short links in this exact style:

- `**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/<slug>.html)`
- `**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/<slug>.md)`

Also require dateline exact format:

- `**Dateline:** YYYY-MM-DD HH:MM UTC`

## Verification workflow (mandatory for stories + claim-checks)

1. **Frame the testable question**
   - Write one sentence for the exact proposition being tested.
   - Split into sub-claims if the headline mixes multiple assertions.

2. **Build an evidence ledger (private)**
   - Track each source as: URL, publisher, timestamp, what it proves, known limitations.
   - Mark every item as Observation / Inference / Unknown.

3. **Run contradiction pass before drafting**
   - Seek at least one source that could falsify the working thesis.
   - If disconfirming evidence exists, surface it prominently, not as a footnote.

4. **Check numbers mechanically**
   - Recompute percentages, deltas, ratios, and period-over-period changes.
   - State denominator and timeframe for every statistic in prose.

5. **Assign confidence by evidence quality, not intuition**
   - Confidence must map to source tier strength + method stability + recency.

## Sourcing rigor rules

- Prefer first-party machine-readable sources over screenshots, summaries, or reposts.
- Treat single-source stories as provisional unless the source is a direct primary authority.
- Timestamp sensitivity check: if data can revise, label it explicitly as preliminary.
- Quote claims precisely; do not strengthen wording beyond what the source says.
- Keep attribution close to the claim sentence (reader should not hunt for provenance).

## Claim-check quality guardrails

- Distinguish clearly between:
  - what is directly measured,
  - what is modeled/estimated,
  - what is inferred by context.
- Never let a binary verdict hide important uncertainty bands.
- If a key input is missing, choose **Inconclusive** over forced certainty.
- Include at least one "what would change this verdict" condition in limitations.

## Uncertainty language protocol (SELF quality upgrade)

When evidence is incomplete or mixed, make uncertainty explicit at sentence level instead of burying it in limitations.

- Use **verified-status labels** in drafting notes and map to copy verbs:
  - `Verified (direct evidence)` → use verbs like *shows/measured/recorded*
  - `Likely (supported inference)` → use verbs like *indicates/suggests*
  - `Unverified claim` → use verbs like *claims/alleges/says*
- If a key artifact is user-generated content (UGC), identify it as UGC in the sentence and state what is and is not verified yet.
- For risk reporting, include scale/context in the same paragraph as the claim (avoid alarming framing without denominator/baseline).
- If verification is pending, say so directly and timestamp the latest verified checkpoint.

## Narrative clarity checklist

- Lead with the answer, then the strongest evidence, then why it matters.
- Keep paragraphs short and single-purpose.
- Replace abstract method language with concrete verbs (measured, counted, compared, matched).
- Avoid stacked caveats in one sentence; distribute them where each uncertainty appears.

## Weak-point guardrails (SELF quality upgrade)

These rules target recurring weak spots in OSINT reporting quality: overreliance on single artifacts, weak provenance for social content, and under-explained uncertainty.

### 1) UGC provenance fit-for-claim (image/video/social posts)

Do not use a fixed checklist count. Choose checks based on what the claim actually asserts, and cover the dimensions required to validate that claim.

- If a claim depends on **where** something happened, prioritize and document location checks.
- If it depends on **when** it happened, prioritize and document timing checks.
- If it depends on **what** is shown, prioritize and document content/authenticity checks.
- If it depends on **who** posted it or chain-of-custody, prioritize and document source/provenance checks.

Available check families:
- Source check: account history, prior behavior, and whether uploader appears original vs repeater.
- Content check: reverse-image/keyframe search for prior appearances or context shifts.
- Time check: chronolocation cues (sun/shadow/weather/event timing) or upload-time consistency.
- Place check: geolocation cues matched to maps/satellite/street-level references.
- Integrity check: whether metadata is missing/stripped and how that limits certainty.

Minimum standard: evidence must cover every critical dimension of the claim; if any critical dimension remains unverified, downgrade confidence and state exactly what is missing.

### 2) Corroboration floor by claim criticality

- High-impact claims (casualties, state action, cross-border incidents, market-moving assertions): require at least 2 independent evidence families before strong verdicts.
- If all available evidence traces back to one origin, classify as provisional or inconclusive.
- Independence means not just two articles citing the same upstream post.

### 3) Falsification logging (private trace)

In `research-traces/`, add a short **"Could this be wrong because..."** block listing:
- top disconfirming hypothesis,
- what evidence would invalidate the current conclusion,
- whether that evidence was found or missing.

### 4) Attribution precision in copy

- Put attribution in the same sentence as each disputable fact.
- Distinguish verbs by evidence strength: “shows/measured” (direct), “indicates/suggests” (inference), “claims/alleges” (unverified assertion).
- Do not use certainty language (“proves”, “confirms”) unless direct primary evidence is explicit and linked.

## Corrections and updates protocol

- If a published post is materially wrong, correct fast and state what changed.
- For follow-ups, explicitly separate: unchanged findings vs new findings.
- Preserve an audit trail in `research-traces/` for major methodological changes.

## Single-source and rumor discipline (SELF quality upgrade)

- If a high-impact claim relies on one origin (single post, single official statement, single scraper output), label the conclusion as provisional unless independent corroboration is found.
- For market- or conflict-sensitive rumor bursts, explicitly separate:
  - what is verified,
  - what is circulating unverified,
  - what evidence is still missing.
- Do not publish a strong binary verdict when key contradictory evidence is unavailable or blocked by timing gaps.

## Trace-to-copy mapping rule (SELF quality upgrade)

Before publishing, ensure each major claim in the story body has a matching evidence entry in `research-traces/` with:
- source URL,
- timestamp/date,
- classification (Observation / Inference / Unknown),
- one-line limitation note.

If a sentence cannot be mapped, rewrite or remove it.

## Claim-origin and falsification ladder (SELF quality upgrade)

Before drafting, force a short origin-first verification ladder for any social/UGC-sensitive claim:

1. **Origin trace first:** identify the earliest observable source/post, not just the most viral repost.
2. **Claim decomposition:** split into micro-claims (who/what/where/when/impact) and mark each as proven/unproven.
3. **Counter-evidence sweep:** search specifically for evidence that would invalidate each micro-claim.
4. **Source transparency threshold:** if origin cannot be established, cap confidence at provisional/inconclusive.
5. **Narrative fit check:** ensure headline reflects only the strongest still-valid micro-claims.

Rationale alignment:
- Mirrors Reuters standards emphasis on cross-checking, source honesty, and trying to disprove initiative reporting.
- Mirrors Reuters Fact Check methodology of identifying claim origin and linking supporting evidence.
- Mirrors Bellingcat’s originality/source/location/time verification sequence.

## Copy desk pass (mandatory before publish)

Run a final newsroom-style pass focused on accuracy and readability, not prose flourishes:

- **Claim-to-source sweep:** every factual sentence maps to a linked source or is explicitly labeled inference.
- **Attribution verb audit:** use verb strength that matches evidence quality (`shows` vs `suggests` vs `claims`).
- **Numerical hygiene:** units, denominators, and time windows are explicit and internally consistent.
- **Uncertainty placement:** caveats appear where the uncertainty is introduced, not buried later.
- **Headline discipline:** headline states the strongest defensible conclusion, not the most dramatic framing.

## FOLLOWUP staleness gate (SKILL quality upgrade)

When FOLLOWUP cycles repeatedly return unchanged outputs, avoid low-value reruns that only restate the same numbers.

- If the same sampled items have shown **no material update across 2+ consecutive FOLLOWUP runs**, rotate at least one sampled item to a different recent high-impact publication.
- Keep at least one continuity check from prior cycle, but require one freshness check (new source family, new topic, or newly published post) before deciding no-publish.
- If all sampled items are unchanged, explicitly record the staleness condition in `research-traces/` and use concise no-publish language.
- Do not manufacture updates; this gate improves sampling quality, not publication pressure.

## Cadence safety checks before push

- Confirm new output has working source links
- Keep commit scope tight (avoid unrelated HTML churn)
- Verify GitHub Pages endpoint reflects latest commit before reporting success
