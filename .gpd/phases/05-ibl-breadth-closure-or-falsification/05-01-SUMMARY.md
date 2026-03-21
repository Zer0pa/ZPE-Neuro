---
phase: 05-ibl-breadth-closure-or-falsification
plan: 01
depth: full
one-liner: "Phase 5 closes the counted IBL extracellular breadth target under the unchanged downstream contract and leaves the lane narrower but materially stronger."
subsystem: [analysis, execution, validation]
tags: [ibl, breadth, runpod, extracellular]
requires: [04-01-lane-1-wedge-decision]
provides:
  - a bounded IBL search packet
  - a passing second-target IBL evaluation
  - an updated public breadth summary
  - updated lane state surfaces
affects: [05-ibl-breadth-closure-or-falsification, lane-1-authority, public-breadth]
completed: 2026-03-21
---

# Phase 05 Plan 01: IBL Breadth Closure Or Falsification

**Phase 5 executed the bounded IBL rescue route honestly and found a real counted extracellular breadth pass without weakening the downstream contract.**

## Key Results

- Produced `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ibl_refinement_search.json`.
- Produced `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json`.
- Produced `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ibl_refinement_decision.md`.
- Produced `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json`.
- Updated `.gpd/STATE.md`, `.gpd/state.json`, `.gpd/ROADMAP.md`, `ROADMAP.md`, `PUBLIC_AUDIT_LIMITS.md`, and the team packet status pages so the repo reflects the new breadth state honestly.

## Decisive Evidence

- Best IBL candidate: chunk `732`, channels `128:136`, window start `12000`.
- Codec metrics: `110` events, `224.30x` compression ratio, `38.16 uV` RMSE on the searched public IBL slice.
- NWB roundtrip: `PASS`.
- SpikeInterface path: `PASS` with `120` detected peaks and `sorter_probe_status = PASS`.
- Breadth rerun: `PASS` for the narrowed extracellular public packet, with DANDI preserved as the Tier 1 anchor and AJILE12 still `OUT_OF_FAMILY`.

## Interpretation

- The old IBL failure was not a trustworthy lane verdict because it was bound to one first chunk, one first channel span, and one first representative window.
- The Phase 5 search changed only bounded chunk, channel-window, and representative-slice choice. It did not lower the codec, NWB, or SpikeInterface contract.
- This closes the counted public breadth blocker for the narrowed extracellular lane, but it does **not** close blind-clone, Allen-risk, or release-boundary gates.

## Next Task

Use the repaired repo-local truth surfaces plus the new public breadth pass to prepare the next decisive gate: a clean blind-clone authority pack and an explicit remaining-blocker order for Allen, release, and broader commercialization claims.

```yaml
gpd_return:
  status: completed
  files_written:
    - ".gpd/phases/05-ibl-breadth-closure-or-falsification/05-01-SUMMARY.md"
    - ".gpd/STATE.md"
    - ".gpd/state.json"
    - ".gpd/ROADMAP.md"
    - "ROADMAP.md"
    - "PUBLIC_AUDIT_LIMITS.md"
    - "docs/team_packet/01_PRODUCT_AND_AUTHORITY_STATUS.md"
    - "docs/team_packet/02_EXECUTION_AND_PHASE_STATUS.md"
    - "docs/team_packet/06_RISKS_BLOCKERS_AND_DECISIONS.md"
    - "runbooks/20260321T131650Z_codex_receipt.md"
  issues:
    - "Blind-clone verification remains open."
    - "Allen parity and broader commercialization risk remain open."
    - "Release-boundary and public-claim staging remain open."
  next_actions:
    - "$gpd-progress --full"
    - "Prepare the blind-clone authority pack from proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement"
  phase: "05"
  plan: "01"
  tasks_completed: 6
  tasks_total: 6
```
