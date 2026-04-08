# Benchmarks

## Methodology

- Source artifacts: `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/`.
- Window policy: scan. Slice size: 8 channels x 6000 samples unless noted.
- Metrics: compression ratio, RMSE (uV), roundtrip bit-consistency when recorded.
- Speed: not recorded in the March 21 artifacts.
- Reproduction scripts:
  - `tools/run_public_corpus_benchmark.py --dandiset 000034 --artifact-root <dir>`
  - `tools/run_ibl_public_waveform_eval.py --artifact-root <dir>`
  - `tools/run_nwb_benchmark.py --nwb-path <file> --dataset-id <id> --asset-path <path>`

## Published Benchmarks

| dataset | modality | channels | duration (s) | ratio | fidelity | speed |
|---|---|---|---|---|---|---|
| DANDI 000034 (mouse412804) | extracellular ecephys | 8 | 0.2 | 401.044 | RMSE 78.441 uV; bit-consistent | not recorded |
| IBL KS014 2019-12-03 probe00 AP | extracellular ecephys | 8 | 0.2 | 224.299 | RMSE 38.159 uV; bit-consistent | not recorded |
| DANDI 000055 AJILE12 (out-of-family control) | intracranial ecephys | 8 | 12.0 | 796.680 | RMSE 28.353 uV; bit-consistent; spikeinterface FAIL | not recorded |

Sources:
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`

## Pending / Blocked

| dataset | status | requirement | script |
|---|---|---|---|
| DANDI 000003 | not run | `dandi download https://dandiarchive.org/dandiset/000003/draft --output-dir data/dandi000003/` | `tools/run_nwb_benchmark.py` |
| DANDI 000005 | not run (out-of-lane) | `dandi download https://dandiarchive.org/dandiset/000005/draft --output-dir data/dandi000005/` | `tools/run_nwb_benchmark.py` |
| DANDI 000016 | not run | `dandi download https://dandiarchive.org/dandiset/000016/draft --output-dir data/dandi000016/` | `tools/run_nwb_benchmark.py` |
| Allen Brain Observatory | not run | `allensdk` cache with local NWB files | `tools/run_nwb_benchmark.py` |
| IBL 100+ sessions | not run | ONE API + extended storage budget | `tools/run_ibl_public_waveform_eval.py` |
