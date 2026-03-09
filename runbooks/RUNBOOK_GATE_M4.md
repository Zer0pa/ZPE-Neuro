# RUNBOOK: Gate M4 (Post-Expansion Claim Stability)

## Objective
Validate that NEU claims remain stable after M1-M3 expansions and rerun critical regressions.

## Commands
1. `source .venv/bin/activate`
2. `python3.11 tools/run_gate_m4.py`
3. `python3.11 tools/validate_artifact_schema.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1 --files claim_status_delta.md neuro_sort_eval.json neuro_embedded_latency.json max_claim_resource_map.json`

## Expected Outputs
1. `claim_status_delta.md` refreshed with max-wave adjudication.
2. `net_new_gap_closure_matrix.json` updated.
3. `quality_gate_scorecard.json` refreshed with max-wave gate statuses.

## Fail Signatures
1. `CLAIM_REGRESSION_AFTER_MAX`
2. `EVIDENCE_PATH_MISSING`
3. `INVALID_SCHEMA`

## Rollback
1. Patch only components that regressed in M1-M3.
2. Rerun failed gate and downstream E-gates.
