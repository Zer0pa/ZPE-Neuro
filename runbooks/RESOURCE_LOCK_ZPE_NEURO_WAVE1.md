# RESOURCE LOCK: ZPE Neuro Wave-1

## Locked Runtime
- Python: `3.11.x`
- Deterministic env vars:
  - `PYTHONHASHSEED` set per replay seed
  - `ZPE_NEURO_GLOBAL_SEED=20260220`

## Locked Datasets/Comparators
1. MEArec synthetic benchmark source
   - Preferred: `MEArec` package generated corpus
   - Lock metadata: package version, seed, channel count, duration, sampling rate
2. Allen Brain Atlas or equivalent large-scale neural dataset
   - Preferred: public NWB sample
   - Lock metadata: source URL, retrieval timestamp, hash/snapshot id where available
3. Neuralink public challenge comparator
   - Preferred: public challenge sample
   - Lock metadata: source URL, retrieval timestamp, checksum
4. Kilosort4 comparator
   - Preferred: direct Kilosort4 run via SpikeInterface
   - Lock metadata: sorter version, parameter preset, seed
5. SpikeSift comparator methodology
   - Preferred: paper-code method if accessible
   - Lock metadata: citation, drift protocol details
6. RAMAN tinyML findings
   - Documentation-only lock: citation + extracted rationale section
7. Allen Neuropixels (AWS)
   - Lock metadata: manifest path, session id(s), retrieval timestamp
8. MIT-BIH via WFDB
   - Lock metadata: record ids, sampling rate, annotation source
9. Rhythm-SNN evidence
   - Lock metadata: citation URL, retrieval timestamp, hypothesis mapping id

## Substitution Rules (Hard)
1. If preferred resource unavailable, use nearest viable alternative in-lane.
2. Log exact failure signature, substitution chosen, and comparability impact.
3. Do not claim equivalence unless objectively demonstrated.
4. Keep dependent claims `INCONCLUSIVE` when equivalence is unproven.
5. If only restricted/non-commercial resource exists and no commercial-safe open alternative is executable, mark dependent closure `PAUSED_EXTERNAL`.

## Impracticality Policy Lock
1. Allowed codes only: `IMP-LICENSE`, `IMP-ACCESS`, `IMP-COMPUTE`, `IMP-STORAGE`, `IMP-NOCODE`.
2. Every impractical decision must include command evidence, error signature, fallback, and claim-impact note.
3. Any compute-constrained path (`IMP-COMPUTE`) requires:
   - `runpod_readiness_manifest.json`
   - `runpod_exec_plan.md`
   - `runpod_requirements_lock.txt`
   - `runpod_expected_artifacts.json`

## Provenance Logging
- All retrievals and environment checks must be appended to `artifacts/2026-02-20_zpe_neuro_wave1/command_log.txt`.
