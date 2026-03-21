---
phase: 03-breadth-adjudication-and-public-rerun
plan: 01
depth: full
one-liner: "Phase 3 converted the AJILE ambiguity into an explicit OUT_OF_FAMILY decision for Lane 1, grounded in the executed DANDI, AJILE, and IBL public artifacts."
subsystem: [analysis, validation]
tags: [ajile, family-boundary, public-corpus, lane-1-authority]
requires: [02-ibl-waveform-slice-execution]
provides:
  - an explicit AJILE family-boundary memo
  - reproducible adjudication logic over the carried-forward public artifacts
affects: [03-breadth-adjudication-and-public-rerun, 04-lane-1-wedge-decision, lane-1-authority]
completed: 2026-03-21
---

# Phase 03 Plan 01: AJILE Family Boundary Summary

**Phase 3 converted the AJILE ambiguity into an explicit `OUT_OF_FAMILY` decision for Lane 1, grounded in the executed DANDI, AJILE, and IBL public artifacts.**

## Key Results

- Added `src/zpe_neuro/breadth_adjudication.py` and `tools/run_public_breadth_adjudication.py` so the family decision is derived from evidence instead of hand-written.
- Wrote `proofs/selected_artifacts/2026-03-21_zpe_neuro_breadth_adjudication/ajile12_family_boundary_decision.md`.
- Preserved the scientific split: DANDI remains the positive spike-oriented anchor, AJILE is explicitly out-of-family for Lane 1, and IBL remains a real but still-failing second extracellular target.

## Validation

- Ran `env PYTHONPATH=src '/Users/Zer0pa/ZPE/ZPE Neuro/.venv/bin/python' -m unittest tests.test_breadth_adjudication` and both tests passed.
- Ran `env PYTHONPATH=src '/Users/Zer0pa/ZPE/ZPE Neuro/.venv/bin/python' tools/run_public_breadth_adjudication.py` and the tool returned `family_boundary_decision = OUT_OF_FAMILY`.

## Decision

AJILE12 should not be treated as a near-miss breadth target for the current spike-oriented codec. It belongs outside the current Lane 1 family boundary unless a later second representation mode is introduced.
