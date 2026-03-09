# RUNBOOK: Gate M2 (External Corpus Parity)

## Objective
Attempt Allen Neuropixels, challenge-style corpus path, and MIT-BIH/WFDB parity runs with evidence-bound outcomes.

## Commands
1. `set -a; source .env; set +a`
2. `source .venv/bin/activate`
3. `python3.11 tools/run_gate_m2.py`

### Allen Waveform Parity Closure Commands (2026-02-21)
1. `python - <<'PY' (validate cached Allen NWB integrity and read headers)`
2. `python - <<'PY' (EcephysProjectCache.from_warehouse + get_session_data attempt)`
3. `python - <<'PY' (direct well_known_file_download HTTP attempt)`
4. `python3.11 tools/run_gate_m4.py`
5. `python3.11 tools/run_gate_appendix_e.py`

## Expected Outputs
1. `max_resource_validation_log.md` with attempt evidence for all Appendix E3 resources.
2. `max_claim_resource_map.json` with claim linkage and closure state.
3. `spike_timing_error_distribution.json` from MIT-BIH cardiac proxy timing/fidelity test.
4. `impracticality_decisions.json` updates for blocked resources.

## Fail Signatures
1. `ALLEN_ACCESS_FAIL`
2. `NEURALINK_STYLE_RESOURCE_FAIL`
3. `MITBIH_INGEST_FAIL`
4. `E3_RESOURCE_NOT_ATTEMPTED`
5. `ALLEN_NWB_TRUNCATED_FILE`
6. `ALLEN_SESSION_DOWNLOAD_FAIL`

## Rollback
1. Patch external-ingestion harness only.
2. Preserve all previous gate artifacts and logs.
3. Rerun M2 and downstream gates.

## Adjudication Rule
- Any unexecuted E3 item without valid IMP-* entry is a hard fail.
- Allen parity may be closed only with waveform-level executable evidence; metadata-only success remains `INCONCLUSIVE`.
