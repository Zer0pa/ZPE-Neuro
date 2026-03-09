# RUNBOOK: Gate D (Adversarial + Determinism + Drift + Regression)

## Objective
Run Popper-first falsification campaigns and reproducibility checks before final claim adjudication.

## Commands
1. `python3.11 tools/run_gate_d.py --replay-seeds 20260220,20260221,20260222,20260223,20260224`
2. `python3.11 tools/validate_artifact_schema.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1 --files neuro_embedded_latency.json neuro_drift_resilience.json determinism_replay_results.json`

## Expected Outputs
- `neuro_embedded_latency.json`
- `neuro_drift_resilience.json`
- `determinism_replay_results.json`
- `falsification_results.md`
- `regression_results.txt`

## Fail Signatures
- `DETERMINISM_MISMATCH`
- `UNCaught_CRASH`
- `LATENCY_BREACH`
- `DRIFT_BREACH`

## Rollback
1. Patch only failing subsystem.
2. Re-run failed test set and all downstream gate logic.
3. Preserve failed logs for evidence continuity.

## Falsification Declaration
- Run DT-NEU-1..5 suites before any final PASS claim.
