# RUNBOOK: Gate E-G (Appendix E Hard Gates)

## Objective
Close Appendix E hard gates (`E-G1`..`E-G5`) with complete resource-attempt evidence and RunPod readiness where required.

## Commands
1. `source .venv/bin/activate`
2. `python3.11 tools/run_gate_appendix_e.py`

## Expected Outputs
1. `max_resource_lock.json`
2. `max_resource_validation_log.md`
3. `max_claim_resource_map.json`
4. `impracticality_decisions.json`
5. `comparator_license_isolation_note.md`
6. `net_new_gap_closure_matrix.json`
7. `runpod_readiness_manifest.json` (if any `IMP-COMPUTE`)
8. `runpod_exec_plan.md` (if any compute deferral)
9. `runpod_requirements_lock.txt` (if any compute deferral)
10. `runpod_expected_artifacts.json` (if any compute deferral)

## Fail Signatures
1. `E-G1_FAIL` (not all E3 resources attempted)
2. `E-G2_FAIL` (comparator closure lacks Kilosort4 or documented impact)
3. `E-G3_FAIL` (theory used as executable proof)
4. `E-G4_FAIL` (missing/invalid IMP-* entry)
5. `E-G5_FAIL` (missing RunPod artifacts for compute-constrained paths)

## Rollback
1. Patch gate metadata/validation only.
2. No claim promotion without executable evidence file paths.
