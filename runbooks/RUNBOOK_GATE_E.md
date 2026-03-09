# RUNBOOK: Gate E (Packaging + Claim Adjudication + Handoff)

## Objective
Produce complete artifact pack, scorecard outputs, and evidence-bound claim status deltas.

## Commands
1. `python3.11 tools/run_gate_e.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1`
2. `python3.11 tools/validate_artifact_schema.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1 --files handoff_manifest.json before_after_metrics.json claim_status_delta.md quality_gate_scorecard.json innovation_delta_report.md integration_readiness_contract.json residual_risk_register.md concept_open_questions_resolution.md concept_resource_traceability.json`

## Expected Outputs
- All mandatory PRD artifacts + Appendix C rubric artifacts present and schema-valid.
- `handoff_manifest.json` includes checksums and gate completion state.
- `claim_status_delta.md` cites file paths for every status transition.

## Fail Signatures
- `MISSING_ARTIFACT`
- `INVALID_SCHEMA`
- `CLAIM_WITHOUT_EVIDENCE`

## Rollback
1. Patch packaging/metadata scripts only.
2. No claim promotion without fresh evidence references.

## Falsification Declaration
- Claims remain `UNTESTED`/`INCONCLUSIVE` unless gate evidence satisfies threshold and comparator integrity rules.
