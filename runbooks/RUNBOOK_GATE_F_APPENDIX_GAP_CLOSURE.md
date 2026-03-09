# RUNBOOK: Gate F-G (Appendix F Gap-Closure + Commercialization)

## Objective
Close Appendix F gates with explicit commercialization-safe comparator coverage and bounded GPL usage:
1. `F-G1`: close M1 by MountainSort5 or Kilosort4 evidence.
2. `F-G2`: rerun M4 immediately after M1 closure.
3. `F-G3`: verify GPL comparator isolation note and commercialization status.

## Commands
1. `set -a; source .env; set +a`
2. `source .venv/bin/activate`
3. `python3.11 tools/run_gate_m1.py`
4. `python3.11 tools/run_gate_m4.py`
5. `python3.11 tools/run_gate_appendix_e.py`

## Expected Outputs
1. `gate_m1_summary.json`
2. `gate_m4_summary.json`
3. `gate_appendix_e_summary.json` (includes F-gate map)
4. `net_new_gap_closure_matrix.json`
5. `comparator_license_isolation_note.md`

## Fail Signatures
1. `F-G1_FAIL` (no executable MountainSort5/Kilosort4 closure)
2. `F-G2_FAIL` (M4 not rerun or not stable)
3. `F-G3_FAIL` (GPL scope/commercialization state absent)
4. `PAUSED_EXTERNAL_REQUIRED` (restricted-only path without commercial-safe alternative)

## Rollback
1. Patch comparator execution logic only.
2. Preserve existing A-E artifacts and previous max-wave logs.
3. Rerun M1 -> M4 -> E-G/F-G chain only.
