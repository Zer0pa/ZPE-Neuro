---
phase: 06-blind-clone-authority-pack-baseline
plan: 01
depth: full
one-liner: "Phase 6 establishes a fresh `.[gate,dev]` baseline, removes hidden Gate C dependency assumptions, and keeps full blind-clone closure explicitly open."
subsystem: [packaging, execution, validation]
tags: [blind-clone, gate-c, gate-d, packaging]
requires: [05-01]
provides:
  - a minimal clean-env gate extra
  - a repaired Gate C spikeinterface probe
  - fresh-env Gate C and Gate D replay evidence
  - an explicit remaining blind-clone gap statement
affects: [06-blind-clone-authority-pack-baseline, gate-c, gate-d, packaging]
completed: 2026-03-21
---

# Phase 06 Plan 01: Blind-Clone Authority Pack Baseline

**Phase 6 repaired the repo's hidden Gate C clean-env assumptions and established a fresh `.[gate,dev]` baseline without converting that baseline into a blind-clone closure narrative.**

## Key Results

- Added a dedicated `gate` extra to `pyproject.toml` and made the Gate C replay surface explicit.
- Moved `ibl_public.py` S3 and SpikeGLX imports behind the code paths that actually need them, so the Phase 1-5 helper modules no longer require those dependencies just to import.
- Replaced the Gate C simple-sorter probe with a repo-owned SpikeInterface harness that performs serialized by-channel peak detection, snippet extraction, sklearn clustering, and sorting materialization without the hidden numba requirement.
- Verified a fresh `.[gate,dev]` environment passes the 12-test Phase 1-5 unit slice plus Gate C and Gate D when they run sequentially.

## Decisive Evidence

- Fresh `.[gate,dev]` install completed in `/tmp/zpe-neuro-gate-venv`.
- Unit slice result: `12 passed` from `tests/test_wave1_codec.py`, `tests/test_wave1_determinism.py`, `tests/test_wave1_metrics.py`, `tests/test_public_corpus_window_selection.py`, `tests/test_ibl_public.py`, `tests/test_ibl_refinement.py`, and `tests/test_breadth_adjudication.py`.
- Gate C result: `artifacts/2026-02-20_zpe_neuro_wave1/gate_c_summary.json` -> `PASS`.
- Gate D result: `artifacts/2026-02-20_zpe_neuro_wave1/gate_d_summary.json` -> `PASS`.
- Parallel fresh-env Gate C and Gate D replay against the shared artifact root produced an HDF5 file-lock collision, so the current baseline is sequential only and not yet a full cold-clone authority pack.

## Interpretation

- The March 20 repo-local gate reruns were scientifically useful, but they depended on hidden workspace state. Phase 6 turned that hidden state into an explicit package boundary and a repo-owned Gate C harness.
- The repaired Gate C probe still does more than peak detection alone: it serializes the recording, reruns SpikeInterface detection on the serialized surface, extracts snippets, clusters them, and materializes a sorting object.
- This closes the clean-env baseline question for the Gate C/Gate D slice, but it does **not** close blind-clone verification, Allen-risk handling, release-boundary work, or heavier public-corpus/proof replay.

## Next Task

Run the next blind-clone phase as a true cold-clone authority-pack replay with isolated artifact roots, then decide whether the heavier public-corpus and proof extras need further decomposition beyond `.[gate]`.

```yaml
gpd_return:
  status: completed
  files_written:
    - ".gpd/phases/06-blind-clone-authority-pack-baseline/06-01-PLAN.md"
    - ".gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md"
    - ".gpd/ROADMAP.md"
    - ".gpd/STATE.md"
    - ".gpd/state.json"
    - "pyproject.toml"
    - "src/zpe_neuro/ibl_public.py"
    - "src/zpe_neuro/wave1.py"
    - "runbooks/20260321T161508Z_codex_receipt.md"
  issues:
    - "Sequential fresh-env Gate C/Gate D replay is established, but full blind-clone authority-pack closure is still open."
    - "Shared artifact roots still collide under parallel Gate C and Gate D execution."
    - "Allen parity and release-boundary work remain open."
  next_actions:
    - "$gpd-progress --full"
    - "$gpd-plan-phase 6"
    - "Run a true cold-clone authority-pack replay with isolated artifact roots."
  phase: "06"
  plan: "01"
  tasks_completed: 5
  tasks_total: 5
```
