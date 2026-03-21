# Engineering Status

## Code Changes That Matter

### `src/zpe_neuro/wave1.py`

- added deterministic probe geometry before SpikeInterface sorter execution
- changed Gate C so peak detection alone cannot produce `PASS`
- changed NWB falsification corruption to a deterministic truncated-copy path
- changed Gate D so falsification failures block `PASS`
- changed regression subprocesses to use `sys.executable`
- changed SpikeInterface bandpass selection to respect the recording sample rate

### `src/zpe_neuro/public_corpus.py`

- new streamed public-corpus harness
- DANDI remote NWB streaming
- target-level evaluation artifacts
- IBL public metadata probe
- honest target-level pass/fail logic

### `tools/log_comet_run.py`

- new run logger for the current repo-local proof packet
- logs key JSON summaries and the team packet into Comet
- writes a local `comet_run_manifest.json` artifact for traceability

## Environment Changes

Installed into the shared workspace `.venv`:

- `hdbscan`
- `dandi`
- `ONE-api`
- `remfile`
- `comet-ml`

## Stable Commands From The Inner Repo

- `env ZPE_NEURO_ARTIFACT_ROOT=proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment ../.venv/bin/python tools/run_gate_c.py`
- `env ZPE_NEURO_ARTIFACT_ROOT=proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment ../.venv/bin/python tools/run_gate_d.py`
- `env ZPE_NEURO_ARTIFACT_ROOT=proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment ../.venv/bin/python tools/run_public_corpus_eval.py`

## Operational Assessment

The important operational correction is that the GitHub-linked inner repo is now carrying the working code, the active proof surface, and the team packet. The outer workspace should remain a lane wrapper, not the authority surface.
