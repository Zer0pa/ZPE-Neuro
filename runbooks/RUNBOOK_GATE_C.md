# RUNBOOK: Gate C (NWB + SpikeInterface Integration Contracts)

## Objective
Validate format/tooling interoperability through NWB roundtrip and SpikeInterface E2E harness.

## Prerequisites
1. Run from a repo checkout.
2. Install the gate stack: `python -m pip install -e '.[gate]'`
3. Use an isolated artifact root per run when comparing or parallelizing results.

## Commands
1. `python3.11 tools/run_gate_c.py --artifact-root artifacts/manual_gate_c --seed 20260220`
2. `python3.11 tools/validate_artifact_schema.py --artifact-root artifacts/manual_gate_c --files neuro_nwb_roundtrip.json neuro_spikeinterface_e2e.json`

## Expected Outputs
- `neuro_nwb_roundtrip.json`
- `neuro_spikeinterface_e2e.json`
- `integration_readiness_contract.json` (intermediate or final content)

## Fail Signatures
- `DEPENDENCY_UNAVAILABLE`
- `ROUNDTRIP_MISMATCH`
- `SPIKEINTERFACE_CONTRACT_FAIL`

## Rollback
1. Patch integration adapters only.
2. If dependency failure persists, apply nearest viable fallback and log comparability impact.
3. Keep dependent claims `INCONCLUSIVE` unless equivalence is proven.

## Falsification Declaration
- Corrupt adapter contract inputs and assert graceful failures without uncaught crashes.
