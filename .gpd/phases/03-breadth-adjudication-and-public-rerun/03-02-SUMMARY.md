---
phase: 03-breadth-adjudication-and-public-rerun
plan: 02
depth: full
one-liner: "The rerun public summary now counts only real waveform breadth targets, keeps overall breadth FAIL, and hands the repo cleanly into the Lane 1 wedge-decision phase."
subsystem: [analysis, validation, documentation]
tags: [breadth, rerun, public-summary, fail-forward]
requires: [03-01-ajile-family-boundary]
provides:
  - a Phase 3 public breadth summary
  - updated roadmap and state surfaces
affects: [03-breadth-adjudication-and-public-rerun, 04-lane-1-wedge-decision, lane-1-authority]
completed: 2026-03-21
---

# Phase 03 Plan 02: Public Breadth Rerun Summary

**The rerun public summary now counts only real waveform breadth targets, keeps overall breadth `FAIL`, and hands the repo cleanly into the Lane 1 wedge-decision phase.**

## Key Results

- Produced `proofs/selected_artifacts/2026-03-21_zpe_neuro_breadth_adjudication/public_corpus_summary.json`.
- Carried forward the selected-window artifact into `public_corpus_window_selection_summary.json` so the Phase 3 packet stays tied to the deterministic scan policy.
- Updated `.gpd/ROADMAP.md`, `.gpd/STATE.md`, and `.gpd/state.json` to mark Phase 3 complete and Phase 4 as the next active task.

## Breadth Verdict

- `DANDI`: retained as the Tier 1 authority anchor, not counted as breadth closure.
- `AJILE12`: excluded from breadth counting because the Phase 3 memo classifies it as `OUT_OF_FAMILY` for Lane 1.
- `IBL`: counted as the real second extracellular waveform target and still `FAIL` on downstream evaluation, so overall breadth remains `FAIL`.

## Next Task

Phase 4 should turn this fail-forward state into a clear product recommendation: a narrower extracellular Lane 1 wedge with stronger authority, plus an explicit note that broader human neural coverage requires a second-mode lane.
