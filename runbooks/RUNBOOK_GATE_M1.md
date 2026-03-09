# RUNBOOK: Gate M1 (Comparator Closure: MountainSort5 First, Kilosort4 Optional)

## Objective
Execute direct comparator closure on benchmark sessions:
1. MountainSort5 on Mac/CPU first (commercial-safe comparator path per Appendix F).
2. Kilosort4 as high-stringency comparator (benchmark-isolated GPL path).

## Preconditions
1. Gates A-E completed.
2. Environment bootstrap succeeded with `.env`.
3. Benchmark corpus and deterministic seeds fixed.
4. Comparator license policy loaded (`comparator_license_isolation_note.md`).

## Commands
1. `set -a; source .env; set +a`
2. `source .venv/bin/activate`
3. `python3.11 tools/run_gate_m1.py`

### Closure Push Debug Commands (2026-02-21)
1. `python - <<'PY' (print spikeinterface default kilosort4 params for version lock)`
2. `python - <<'PY' (KS4-FIX-A: nblocks=0, do_correction=False, threshold tuning)`
3. `python - <<'PY' (KS4-FIX-B: nearest_templates <= channels, template geometry tuning)`
4. `python - <<'PY' (KS4-FIX-C: extended-duration dataset + batch sizing in runpod-ready path)`
5. `python3.11 tools/run_gate_m4.py`
6. `python3.11 tools/run_gate_appendix_e.py`

## Expected Outputs
1. `neuro_sort_eval.json` updated with MountainSort5/Kilosort4 attempt status.
2. `max_resource_validation_log.md` includes M1 command evidence.
3. `impracticality_decisions.json` populated if Kilosort4 is blocked.
4. `comparator_license_isolation_note.md` documents GPL isolation.

## Fail Signatures
1. `MOUNTAINSORT5_INSTALL_FAIL`
2. `MOUNTAINSORT5_RUNTIME_FAIL`
3. `KILOSORT4_INSTALL_FAIL`
4. `KILOSORT4_RUNTIME_FAIL`
5. `LICENSE_ISOLATION_MISSING`
6. `KILOSORT4_ZERO_SAMPLE_TRUNCATEDSVD`
7. `KILOSORT4_NSAMPLES_LT_NCLUSTERS`
8. `RUNPOD_EXEC_CHAIN_FAIL`

## Rollback
1. Patch comparator harness only.
2. Keep prior A-E artifacts unchanged.
3. Rerun M1 and downstream M/E gates.

## Adjudication Rule
- `M1 PASS` requires either MountainSort5 direct comparator success or Kilosort4 direct comparator success with evidence.
- If both are unproven, mark comparator closure `FAIL` with IMP-* evidence.
- If only restricted/non-commercial comparator path exists and no commercial-safe open alternative is executable, mark `PAUSED_EXTERNAL` with evidence.
- For Kilosort4 high-stringency closure, run at least 3 concrete fixes before final residual classification.
