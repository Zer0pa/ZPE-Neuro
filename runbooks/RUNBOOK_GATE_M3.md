# RUNBOOK: Gate M3 (Embedded Target Latency Upgrade)

## Objective
Replace proxy-only latency evidence with target-profile timing evidence or explicit bounded impracticality + RunPod plan.

## Commands
1. `source .venv/bin/activate`
2. `python3.11 tools/run_gate_m3.py`

## Expected Outputs
1. `neuro_embedded_latency.json` includes target-profile section and evidence path.
2. `max_resource_validation_log.md` includes timing harness evidence.
3. `runpod_readiness_manifest.json` + `runpod_exec_plan.md` when `IMP-COMPUTE` is used.

## Fail Signatures
1. `TARGET_PROFILE_UNVERIFIED`
2. `LATENCY_BREACH`
3. `RUNPOD_ARTIFACT_MISSING`

## Rollback
1. Patch latency harness only.
2. Keep claims open if target evidence remains unproven.
3. Rerun M3 and downstream gates.
