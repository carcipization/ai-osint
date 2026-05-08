# STORY Slot Trace + EVOLVE Fallback (2026-05-08)

## Slot intent
- Requested slot: STORY
- Reuters exclusion respected (not used as lead/evidence/corroboration)
- Core decision question applied first-principles: "What fresh, measurable anomaly has concrete non-specialist decision consequences now, and can it be independently validated in-slot?"

## Why STORY did not publish this run
- Quick sweep did not surface a defensible, fresh anomaly with enough same-slot independent confirmation to clear publication confidence without resorting to article-led seeds.
- Candidate set in this run was duplicate-heavy/weakly specified at lead stage, creating avoidable friction before evidence pulls.
- To avoid low-value/noise publication, STORY was held and one EVOLVE fallback iteration was executed in-slot as required.

## EVOLVE hypothesis
If candidate packets are generated in a structured way before deep validation, then weak/ambiguous leads can be filtered faster, candidate rotation improves, and next-7-day STORY publish probability rises via better throughput.

## Repo-level change made
- Added: `scripts/story_candidate_packet.py`
- Function: generates required 4-item candidate packets for each lead:
  1) testable question
  2) three required evidence checks
  3) one falsifier
  4) target datasets for interrogation

## Before/after checks
- Before: lead vetting often started from free-form notes; inconsistent packet quality increased time to first defensible candidate.
- After: standardized packet output is machine-readable JSON and can be generated in seconds for multiple leads, enabling faster triage/rotation.
- Sanity check executed:
  - `python3 scripts/story_candidate_packet.py --lead "Port congestion spike in Mediterranean" --lead "Unexpected hospital admissions jump"`
  - Output validated (2 packets generated, complete required fields).

## Expected effect on publishability
- Faster candidate decomposition and falsification planning in early slot minutes.
- Higher probability of finding at least one publishable candidate within slot time by reducing lead ambiguity and speeding abandonment of weak leads.
- No additional publish-gating added; this reduces friction rather than adding restrictions.
