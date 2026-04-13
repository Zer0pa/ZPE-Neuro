# V6 Authority Surface — Completion Report

**Repo:** ZPE-Neuro
**Agent:** Codex
**Date:** 2026-04-14
**Branch:** campaign/v6-authority-surface

## Dimensions Executed

- [x] **A: Key Metrics** — rewritten to the repo-manifest V6 slate
- [ ] **B: Competitive Benchmarks** — skipped; the V6 manifest says Neuro has no front-door-ready competitive evidence and forbids adding this section
- [ ] **C: pip Install Fix** — N/A; `pyproject.toml` is already at repo root
- [x] **D: Publish Workflow** — added `.github/workflows/publish.yml`
- [ ] **E: Proof Sync** — N/A; Neuro is not marked `PUBLIC_MISSING_LOCAL_ARTIFACTS`

## Verification

- pip install from root: PASS
- import test: PASS
- Proof anchors verified: 7/7 exist
- Competitive claims honest: YES — no competitive section was added because the manifest explicitly says none exist

## Key Metrics Written

| Metric | Value | Baseline | Proof File |
|--------|-------|----------|------------|
| DANDI_CR | 401.044× | — | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` |
| IBL_CR | 224.299× | — | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json` |
| WAVEFORM_PASS | 1/1 | 3 executed targets | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` |
| ROBUSTNESS | 0 falsification failures | 0.0 crash rate | `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_d_summary.json` |

## Verified Proof Anchors

- `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/verification_summary.md`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_c_summary.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_d_summary.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json`

## Issues / Blockers

- The campaign-wide PyPI standard calls for `LicenseRef-Zer0pa-SAL-6.2`, but the current public Neuro license surface is still internally consistent on `SAL-6.0` across `LICENSE`, `README.md`, and `pyproject.toml`. Neuro was not assigned Dimension C in the repo manifest, and changing package metadata alone would create a contradictory public license surface without a coordinated license-text migration.
- `IBL_CR` is surfaced exactly as directed by the repo manifest and backed by a retained proof artifact. No broader competitive or operator-path claims were added.
