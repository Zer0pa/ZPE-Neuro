# Key Data And Evidence

## Core Baseline

| Metric | Value | Interpretation |
| --- | --- | --- |
| Dense synthetic compression headline | `209.31x` | Strong internal baseline, not sovereign real-corpus closure |
| Worst-case local waveform RMSE | `0.4037 uV` | Strong internal waveform anchor |

## Repo-Local Gate Repair Evidence

| Item | Current Status | Source |
| --- | --- | --- |
| Gate C summary | PASS | `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/gate_c_summary.json` |
| Gate D summary | PASS | `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/gate_d_summary.json` |
| `DT-NEU-5` falsification fail count | `0` | `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/gate_d_summary.json` |

## Tier 1 Public Slice: DANDI `000034`

Source artifact:

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`

Key numbers:

| Field | Value |
| --- | --- |
| Asset size | `13,411,878,072` bytes |
| Series shape | `27,000,000 x 248` |
| Evaluated slice | `6000 x 8` |
| Sampling rate | `30,000 Hz` |
| Codec event count | `28` |
| Compression ratio | `486.08x` |
| RMSE | `66.01 uV` |
| NWB roundtrip | `PASS` |
| SpikeInterface insertion | `PASS` |

## Tier 2 Breadth Slice: AJILE12

Source artifact:

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`

Key numbers:

| Field | Value |
| --- | --- |
| Asset size | `10,273,614,013` bytes |
| Series shape | `27,858,793 x 94` |
| Evaluated slice | `6000 x 8` |
| Sampling rate | `500 Hz` |
| Codec event count | `0` |
| Compression ratio | `864.86x` |
| RMSE | `0.0 uV` |
| NWB roundtrip | `PASS` |
| SpikeInterface insertion | `FAIL` |
| Failure reasons | `NO_CODEC_EVENTS_DETECTED`, `SPIKEINTERFACE_FAIL` |

Important interpretation:

- the high compression ratio and zero RMSE are not a win here
- they mostly reflect a quiet slice that the current spike-template codec does not engage with
- this is exactly the kind of false positive the team must reject

## IBL Public Access

Source artifact:

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_ibl_probe.json`

Key data:

| Field | Value |
| --- | --- |
| Public metadata access | `PASS` |
| Returned session ID | `ba892860-149e-4bff-9961-aa6583d96661` |
| Returned dataset count | `42` |
| Waveform slice executed | `false` |

## Public-Corpus Summary

Source artifact:

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_summary.json`

Result:

- overall status: `FAIL`
- DANDI `000034`: `PASS`
- AJILE12: `FAIL`
- IBL metadata probe: `PASS`
