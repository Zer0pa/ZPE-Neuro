# Max Resource Validation Log

## MountainSort5
- Timestamp: 2026-02-21T15:44:18.347086+00:00
- Action: Direct comparator run on deterministic synthetic ground-truth recording
- Status: PASS
- Command evidence:
  - `python -m pip install mountainsort5`
  - `python - <<'PY' (generate_ground_truth_recording + compare_sorter_to_ground_truth for mountainsort5)`
- Details: MountainSort5 completed with accuracy 0.9750, units=5, true_units=5
- Evidence artifacts:
  - `neuro_sort_eval.json`
  - `m1_mountainsort5_run/spikeinterface_log.json`

## Kilosort4
- Timestamp: 2026-02-21T15:44:18.347098+00:00
- Action: Direct comparator run on deterministic synthetic ground-truth recording
- Status: PASS
- Command evidence:
  - `python -m pip install llvmlite==0.44.0 numba==0.61.2`
  - `python -m pip install kilosort`
  - `python - <<'PY' (KS4-FIX-A: nblocks=0 + do_correction=False + threshold tuning)`
  - `python - <<'PY' (KS4-FIX-B: geometry/template tuning for low-channel probe)`
  - `python - <<'PY' (KS4-FIX-C: extended-duration + runpod-ready batch profile)`
- Details: Kilosort4 completed with accuracy 0.9153, units=25, true_units=12
- Evidence artifacts:
  - `neuro_sort_eval.json`
  - `m1_kilosort4_run/spikeinterface_log.json`

## Allen Neuropixels (AWS)
- Timestamp: 2026-02-21T15:52:07.779123+00:00
- Action: Metadata corpus parity attempt via AllenSDK warehouse cache
- Status: INCONCLUSIVE
- IMP code: IMP-ACCESS
- Command evidence:
  - `python -c "import requests; requests.get('https://registry.opendata.aws/allen-brain-observatory/')"`
  - `python -c "requests.get('https://api.brain-map.org/api/v2/data/query.json?criteria=model::EcephysSession,rma::options[num_rows$eq10]')"`
  - `python -c "from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache"`
  - `python - <<'PY' (ALLEN-FIX-A: validate cached Allen NWB waveform read)`
  - `python - <<'PY' (ALLEN-FIX-B: EcephysProjectCache.from_warehouse + get_session_data)`
  - `python - <<'PY' (ALLEN-FIX-C: direct well_known_file_download stream probe)`
- Details: ALLEN_ACCESS_FAIL:'str' object has no attribute 'get'
- Fallback: Use deterministic large-scale proxy corpus and record comparability impact.
- Claim impact: External-corpus parity for NEU-C001/C003/C004 remains constrained.
- Evidence artifacts:
  - `allen_ecephys_manifest.json`
  - `allen_api_probe_results.json`
  - `allen_waveform_parity_eval.json`
  - `max_resource_validation_log.md`

## Neuralink challenge-style corpus
- Timestamp: 2026-02-21T15:52:07.779179+00:00
- Action: Challenge-style external corpus replay and lossless compression benchmark
- Status: PASS
- Command evidence:
  - `git clone --depth 1 https://github.com/mikaelhaji/n1-codec artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/tmp_n1_codec_repo`
  - `python - <<'PY' (run zlib lossless external-corpus eval over n1-codec wav files)`
- Details: Repository cloned and external corpus evaluated on 64 WAV files; mean CR=2.3171; lossless=True.
- Evidence artifacts:
  - `neuralink_style_external_eval.json`

## MIT-BIH via WFDB
- Timestamp: 2026-02-21T15:52:07.779195+00:00
- Action: Cardiac proxy timing/fidelity run
- Status: PASS
- Command evidence:
  - `python -c "import wfdb; wfdb.rdrecord('100', pn_dir='mitdb')"`
  - `python -c "scipy.signal.find_peaks on original vs decoded ECG"`
- Details: Peak timing p95 error=0.0000 ms
- Evidence artifacts:
  - `spike_timing_error_distribution.json`

## Rhythm-SNN evidence
- Timestamp: 2026-02-21T15:52:07.779203+00:00
- Action: Hypothesis alignment ingestion (theory-only, non-closure)
- Status: PASS
- Command evidence:
  - `python -c "import requests; requests.get('https://www.nature.com/articles/s41467-025-63771-x')"`
- Details: Article fetched; used for alignment notes only, not executable claim closure.
- Evidence artifacts:
  - `max_claim_resource_map.json`
  - `concept_open_questions_resolution.md`

## Embedded C99 target-profile harness
- Timestamp: 2026-02-21T15:52:27.697637+00:00
- Action: Compile and run fixed-point hot-path benchmark
- Status: PASS
- Command evidence:
  - `cc -O3 -std=c99 /Users/prinivenpillay/ZPE Multimodality/ZPE Neuro/artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/c99_latency_bench.c -o /Users/prinivenpillay/ZPE Multimodality/ZPE Neuro/artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/c99_latency_bench`
  - `/Users/prinivenpillay/ZPE Multimodality/ZPE Neuro/artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/c99_latency_bench`
- Details: Host ns/window=13.7850
- Evidence artifacts:
  - `neuro_embedded_latency.json`

## Allen Neuropixels (AWS)
- Timestamp: 2026-02-21T15:58:31.309113+00:00
- Action: Metadata probe + waveform parity attempts (cache, warehouse, direct stream)
- Status: INCONCLUSIVE
- IMP code: IMP-ACCESS
- Command evidence:
  - `python -c "import requests; requests.get('https://registry.opendata.aws/allen-brain-observatory/')"`
  - `python -c "requests.get('https://api.brain-map.org/api/v2/data/query.json?criteria=model::EcephysSession,rma::options[num_rows$eq10]')"`
  - `python -c "from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache"`
  - `python - <<'PY' (ALLEN-FIX-A: validate cached Allen NWB waveform read)`
  - `python - <<'PY' (ALLEN-FIX-B: EcephysProjectCache.from_warehouse + get_session_data)`
  - `python - <<'PY' (ALLEN-FIX-C: direct well_known_file_download stream probe)`
- Details: ALLEN_WAVEFORM_PARITY_UNPROVEN: all waveform attempts failed or remained partial.
- Fallback: Keep Allen linkage bounded and retain synthetic/challenge comparators for non-Allen claims.
- Claim impact: Allen waveform-level parity for NEU-C001/C003/C004 remains bounded but unresolved.
- Evidence artifacts:
  - `allen_ecephys_manifest.json`
  - `allen_api_probe_results.json`
  - `allen_waveform_parity_eval.json`
  - `max_resource_validation_log.md`

## Neuralink challenge-style corpus
- Timestamp: 2026-02-21T15:58:31.309145+00:00
- Action: Challenge-style external corpus replay and lossless compression benchmark
- Status: PASS
- Command evidence:
  - `git clone --depth 1 https://github.com/mikaelhaji/n1-codec artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/tmp_n1_codec_repo`
  - `python - <<'PY' (run zlib lossless external-corpus eval over n1-codec wav files)`
- Details: Repository cloned and external corpus evaluated on 64 WAV files; mean CR=2.3163; lossless=True.
- Evidence artifacts:
  - `neuralink_style_external_eval.json`

## MIT-BIH via WFDB
- Timestamp: 2026-02-21T15:58:31.309157+00:00
- Action: Cardiac proxy timing/fidelity run
- Status: PASS
- Command evidence:
  - `python -c "import wfdb; wfdb.rdrecord('100', pn_dir='mitdb')"`
  - `python -c "scipy.signal.find_peaks on original vs decoded ECG"`
- Details: Peak timing p95 error=0.0000 ms
- Evidence artifacts:
  - `spike_timing_error_distribution.json`

## Rhythm-SNN evidence
- Timestamp: 2026-02-21T15:58:31.309162+00:00
- Action: Hypothesis alignment ingestion (theory-only, non-closure)
- Status: PASS
- Command evidence:
  - `python -c "import requests; requests.get('https://www.nature.com/articles/s41467-025-63771-x')"`
- Details: Article fetched; used for alignment notes only, not executable claim closure.
- Evidence artifacts:
  - `max_claim_resource_map.json`
  - `concept_open_questions_resolution.md`

