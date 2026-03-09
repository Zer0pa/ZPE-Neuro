# RUNBOOK: ZPE Neuro Wave-1 Master

## Scope Lock
- Lane root: repository root (`/Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro`)
- Editable scope: this repo only (including subfolders)
- Explicitly forbidden targets: files outside this repo boundary, sibling sectors, and any outer-workspace orchestration records

## Authoritative Inputs
1. `README.md`
2. `docs/ARCHITECTURE.md`
3. `docs/LEGAL_BOUNDARIES.md`
4. `proofs/README.md`
5. `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/`
6. Historical external concept-pack references remain outside this repo and are treated as lineage inputs only.

## Environment Bootstrap (Mandatory)
1. `set -a; [ -f .env ] && source .env; set +a`
2. Verify tokenized access via env var names only (no secret values in logs).
3. If bootstrap fails, log blocker and halt before implementation.

## Gate Order (Hard, No Skip)
1. Gate A: runbook/resource lock/schema freeze
2. Gate B: codec + compression/fidelity/sort baseline
3. Gate C: NWB + SpikeInterface integration contracts
4. Gate D: falsification/adversarial/drift/determinism/regression
5. Gate E: packaging + claim adjudication + handoff
6. Gate M1: Kilosort4 comparator execution and direct agreement reporting
7. Gate M2: external corpus parity (Allen + challenge-style + MIT-BIH)
8. Gate M3: embedded target-profile latency evidence upgrade
9. Gate M4: claim stability after comparator/corpus expansion
10. Gate E-G: Appendix E hard gates (`E-G1`..`E-G5`) + RunPod readiness closure
11. Gate F-G: Appendix F closure gates (`F-G1`..`F-G3`) commercialization + comparator closure

## Artifact Contract Freeze
- Output root: `artifacts/2026-02-20_zpe_neuro_wave1/`
- Required PRD artifacts:
  - `handoff_manifest.json`
  - `before_after_metrics.json`
  - `falsification_results.md`
  - `claim_status_delta.md`
  - `command_log.txt`
  - `neuro_sparse_benchmark.json`
  - `neuro_dense_benchmark.json`
  - `neuro_waveform_fidelity.json`
  - `neuro_sort_eval.json`
  - `neuro_embedded_latency.json`
  - `neuro_nwb_roundtrip.json`
  - `neuro_spikeinterface_e2e.json`
  - `neuro_drift_resilience.json`
  - `determinism_replay_results.json`
  - `regression_results.txt`
- Required rubric artifacts:
  - `quality_gate_scorecard.json`
  - `innovation_delta_report.md`
  - `integration_readiness_contract.json`
  - `residual_risk_register.md`
  - `concept_open_questions_resolution.md`
  - `concept_resource_traceability.json`
- Required Appendix E artifacts:
  - `max_resource_lock.json`
  - `max_resource_validation_log.md`
  - `max_claim_resource_map.json`
  - `impracticality_decisions.json`
  - `comparator_license_isolation_note.md`
  - `spike_timing_error_distribution.json`
  - `runpod_readiness_manifest.json` (mandatory when any `IMP-COMPUTE`)
  - `runpod_exec_plan.md` (when any compute path deferred)
  - `runpod_requirements_lock.txt` (pinned dependencies for RunPod replay)
  - `runpod_expected_artifacts.json` (artifact contract for RunPod return)
  - `net_new_gap_closure_matrix.json`

## Deterministic Seed Policy
- Global seed: `20260220`
- Replay seeds (5 fixed runs): `[20260220, 20260221, 20260222, 20260223, 20260224]`
- `PYTHONHASHSEED` pinned per replay run.
- All synthetic corpora, adversarial perturbations, and shuffles must source deterministic RNG streams.

## Falsification-First Claim Plan
| Claim | Promote condition | Falsifier(s) first | Evidence artifact |
|---|---|---|---|
| NEU-C001 | sparse CR >= 50x | malformed metadata, sparse noise stress | `neuro_sparse_benchmark.json` |
| NEU-C002 | dense CR >= 20x | dense burst adversarial noise sweep | `neuro_dense_benchmark.json` |
| NEU-C003 | RMSE <= 1 uV | quantizer stress, truncation, decode corruption | `neuro_waveform_fidelity.json` |
| NEU-C004 | sort agreement >= 90% | threshold perturbation + drifted templates | `neuro_sort_eval.json` |
| NEU-C005 | latency < 900 ns/window | on-target profile timing falsifier + worst-case windows | `neuro_embedded_latency.json` |
| NEU-C006 | NWB bit-consistent roundtrip | HDF5/NWB contract corruption tests | `neuro_nwb_roundtrip.json` |
| NEU-C007 | SpikeInterface E2E pass | extractor contract mutation tests | `neuro_spikeinterface_e2e.json` |
| NEU-C008 | drift drop <= 5% @ 15 um | drift cliff sweep beyond 15 um | `neuro_drift_resilience.json` |

## Command Ledger (Planned)
| Gate | Command | Expected output signature | Fail signature | Rollback |
|---|---|---|---|---|
| A | `python3.11 tools/validate_runbook_contract.py` | `RUNBOOK_CONTRACT_OK` | missing gate/runbook/schema file | patch runbooks/schema only |
| B | `python3.11 tools/run_gate_b.py --seed 20260220` | C001-C004 artifacts generated | threshold breach/crash | revert to Gate A snapshot; patch codec |
| C | `python3.11 tools/run_gate_c.py --seed 20260220` | NWB/SI evidence artifacts | import/contract mismatch | patch adapters; rerun C+ |
| D | `python3.11 tools/run_gate_d.py --replay-seeds 20260220,20260221,20260222,20260223,20260224` | falsification, determinism, drift artifacts | non-zero crash, hash mismatch | patch minimal failure; rerun D+ |
| E | `python3.11 tools/run_gate_e.py --artifact-root artifacts/2026-02-20_zpe_neuro_wave1` | claim/rubric/manifest pack | missing file or invalid schema | patch packaging metadata only |
| M1 | `python3.11 tools/run_gate_m1.py` | Kilosort4 attempt evidence + comparator closure decision | install/runtime failure | log IMP-* + fallback + impact |
| M2 | `python3.11 tools/run_gate_m2.py` | Allen/Neuralink-style/MIT-BIH attempt matrix | access/license/compute failure | log IMP-* + keep dependent status open |
| M3 | `python3.11 tools/run_gate_m3.py` | target-profile latency evidence update | no target profile evidence | keep NEU-C005 open if unproven |
| M4 | `python3.11 tools/run_gate_m4.py` | post-expansion claim stability adjudication | regression after expansion | patch minimally and rerun M1-M4 |
| E-G | `python3.11 tools/run_gate_appendix_e.py` | E-G1..E-G5 summary + RunPod readiness | missing attempts/invalid IMP code/missing runpod artifact | patch gating metadata only |
| F-G | `python3.11 tools/run_gate_appendix_e.py` | F-G1..F-G3 summary (MountainSort5/Kilosort4 closure + license boundary) | comparator unresolved or no commercialization status | patch comparator closure pipeline, rerun M1+ |
| All | `python3.11 tools/run_full_wave1.py --max-wave` | full A-E + M/E gates complete | any hard gate fail | fix failed gate + downstream rerun |

## Closure Push Addendum (2026-02-21)
Objective: close remaining `IMP-COMPUTE` and `INCONCLUSIVE` blockers with executable evidence before adjudication.

### Predeclared Kilosort4 Blocker Exhaustion Loop (Minimum 3 concrete fixes)
1. `KS4-FIX-A` (drift/low-channel guidance):
   - Apply Kilosort4 small-probe guidance from official parameters docs: set `nblocks=0` and `do_correction=False` for <=64-channel context; lower detection thresholds (`Th_universal`, `Th_learned`) by 1-2.
   - Expected pass signal: sorter run completes with non-zero units and mean accuracy >= 0.90.
   - Fail signature examples: `ValueError: Found array with 0 sample(s)`, `No spikes detected`.
2. `KS4-FIX-B` (template geometry stability):
   - Set `nearest_templates <= num_channels`; tune `min_template_size` / `dminx` based on probe spacing guidance.
   - Expected pass signal: extractor does not fail in `extract_wPCA_wTEMP` and yields sortable units.
   - Fail signature examples: `n_samples < n_clusters`, `TruncatedSVD` zero-sample.
3. `KS4-FIX-C` (data volume / runtime path):
   - Increase `batch_size` and recording duration for improved drift/statistical support; run exact chain in RunPod-ready environment.
   - Expected pass signal: `gate_m1_summary.json` reports `kilosort4_run_success=true`.
   - Fail signature examples: runtime OOM, container/GPU unavailability, repeated zero-spike failure.

### Predeclared Allen External Parity Closure Loop (Minimum 3 concrete attempts)
1. `ALLEN-FIX-A`: verify existing local NWB cache integrity + read path (`pynwb` and/or `EcephysSession.from_nwb_path`).
2. `ALLEN-FIX-B`: attempt `EcephysProjectCache.from_warehouse(...).get_session_data(session_id)` with manifest-backed cache.
3. `ALLEN-FIX-C`: attempt direct `well_known_file_download` HTTP retrieval and structured cache placement.

Each failed attempt must log:
- exact command
- failure signature
- external dependency/root cause
- comparability impact on affected claims (`NEU-C001`, `NEU-C003`, `NEU-C004`)

### Additional Required Artifacts for Closure Push
1. `internet_evidence_log.md` (source links, versions, commands, and mapped fixes).
2. `commercialization_risk_register.md` (comparator licensing boundary + commercialization status).
3. `allen_waveform_parity_eval.json` (waveform-level parity attempt evidence when available).
4. `runpod_m1_exec_results.json` (RunPod-path command evidence and outcomes).

## Dataset/Comparator Resource Lock + Fallbacks
| Resource | Preferred target | Fallback if unavailable | Impact policy |
|---|---|---|---|
| MEArec | official generator package | deterministic in-lane generator | mark equivalence scope clearly |
| Allen Neuropixels (AWS) | AllenSDK + AWS open data | documented equivalent external corpus | keep linked claim `INCONCLUSIVE` if unproven |
| Neuralink challenge style | public challenge corpus | challenge-parameter synthetic proxy | `INCONCLUSIVE` for direct challenge parity |
| Kilosort4 | direct Kilosort4 run | documented equivalent with effect note | fail M1 if not directly measured |
| MountainSort5 | direct SpikeInterface MountainSort5 run | none (required commercial-safe comparator for Appendix F) | if unavailable, keep F-G1 open |
| MIT-BIH via WFDB | PhysioNet WFDB ingestion | none (open public should run locally) | claim impact if ingestion fails |
| SpikeSift comparator | official method/code | methodology reimplementation | methodology-equivalent only |
| RAMAN tinyML | paper findings extraction | none | documentation-only comparator |
| Rhythm-SNN evidence | Nature Comms evidence ingestion | summary from accessible abstract + concept mapping | no benchmark closure from theory alone |

## Allowed Impracticality Codes
- `IMP-LICENSE`, `IMP-ACCESS`, `IMP-COMPUTE`, `IMP-STORAGE`, `IMP-NOCODE`
- Every impractical decision must include:
  - exact command evidence
  - failure signature
  - fallback chosen
  - claim-impact note

## Commercialization Status Rule
- For comparator or dataset resources that are restricted/non-commercial and lack a commercial-safe open alternative, set dependent closure status to `PAUSED_EXTERNAL`.
- `PAUSED_EXTERNAL` must include: blocked resource, command evidence, licensing/access signature, fallback evaluation, and affected claims/gates.
- GPL comparator usage is benchmark-isolated only and must be explicitly documented in `comparator_license_isolation_note.md`.

## Expected Failure Signatures
- `ModuleNotFoundError` for optional integrations.
- `DETERMINISM_MISMATCH` when replay hashes diverge.
- `UNCaught_CRASH` in malformed/adversarial suite.
- `FIDELITY_BREACH` when RMSE > 1.0.
- `COMPRESSION_BREACH` when CR below threshold.
- `ROUNDTRIP_MISMATCH` when NWB digest differs pre/post.
- `E3_RESOURCE_NOT_ATTEMPTED` when attempt-all policy violated.
- `INVALID_IMP_CODE` when impracticality code is outside allowed set.

## Rollback Strategy
1. On gate failure, preserve failed artifacts/logs.
2. Patch minimal failing module only.
3. Rerun failed gate + downstream gates.
4. Never relax thresholds; promote only with evidence.

## Appendix B/E Traceability Plan (Predeclared)
1. SpikeInterface integration: `neuro_spikeinterface_e2e.json`.
2. MEArec source usage: `concept_resource_traceability.json`.
3. NWB roundtrip: `neuro_nwb_roundtrip.json`.
4. Allen external corpus attempt: `max_resource_validation_log.md`.
5. Neuralink challenge-style attempt: `max_resource_validation_log.md`.
6. Kilosort4 baseline comparison: `neuro_sort_eval.json` + `impracticality_decisions.json`.
7. SpikeSift drift comparator: `neuro_drift_resilience.json`.
8. RAMAN tinyML rationale: `concept_open_questions_resolution.md`.
9. MIT-BIH cardiac proxy evidence: `spike_timing_error_distribution.json`.
10. Rhythm-SNN alignment + falsification notes: `max_claim_resource_map.json`.
