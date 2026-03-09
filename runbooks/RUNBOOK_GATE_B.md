# RUNBOOK: Gate B (Core Codec + Baseline Metrics)

## Objective
Implement deterministic `.zpneuro` codec path and establish baseline compression/fidelity/sort metrics.

## Commands
1. `python3.11 tools/run_gate_b.py --seed 20260220`
2. `python3.11 tools/validate_artifact_schema.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1 --files neuro_sparse_benchmark.json neuro_dense_benchmark.json neuro_waveform_fidelity.json neuro_sort_eval.json`

## Expected Outputs
- `neuro_sparse_benchmark.json`
- `neuro_dense_benchmark.json`
- `neuro_waveform_fidelity.json`
- `neuro_sort_eval.json`
- Updated `before_after_metrics.json` (Gate B section)

## Fail Signatures
- `COMPRESSION_BREACH`
- `FIDELITY_BREACH`
- `SORT_AGREEMENT_BREACH`
- `UNCaught_CRASH`

## Rollback
1. Revert to Gate A snapshot.
2. Patch codec or synthetic corpus logic minimally.
3. Re-run Gate B before proceeding.

## Falsification Declaration
- Execute malformed metadata + adversarial threshold perturbations before claim promotion.
