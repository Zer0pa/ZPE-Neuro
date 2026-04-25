<h1 align="center">ZPE-Neuro</h1>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-SAL%20v7.0-e5e7eb?labelColor=111111" alt="License: SAL v7.0"></a>
  <a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><img src="https://img.shields.io/badge/authority-2026--03--21%20repo%20snapshot-e5e7eb?labelColor=111111" alt="Authority: 2026-03-21 repo snapshot"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/release-current%20surface-e5e7eb?labelColor=111111" alt="Release: current surface"></a>
  <a href="docs/LEGAL_BOUNDARIES.md"><img src="https://img.shields.io/badge/lane-extracellular%20recording-e5e7eb?labelColor=111111" alt="Lane: extracellular recording"></a>
</p>

## What This Is

ZPE-Neuro is a bounded extracellular spike-event extraction surface. The live README only promotes claims that are backed by a tracked proof artifact and exercised in CI. Treat [CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md) as the broader March 21 routing layer; this front door stays narrower on purpose.

## Current Verified Surface

| Claim | Proof artifact | CI coverage |
|-------|----------------|-------------|
| DANDI `000034` bounded slice reproduces `41` events, `401.04x` event ratio, and `78.44 uV` RMSE. | [`public_corpus_eval_dandi_000034_mouse412804_ecephys.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json) | `tests/test_dandi_offline.py` |
| Gate C remains `PASS` for NWB and SpikeInterface compatibility on the tracked release-alignment packet. | [`gate_c_summary.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_c_summary.json) | `Verify Package Surface / proof-import-smoke` and `gate-slice` |
| Gate D remains `PASS` for determinism, drift, and latency on the tracked release-alignment packet. | [`gate_d_summary.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_d_summary.json) | `tests/test_roundtrip.py`, `tests/test_wave1_determinism.py` |
| AJILE12 remains explicitly out of family and is excluded from counted breadth. | [`public_corpus_summary.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json) | `tests/test_breadth_adjudication.py` |

## Current Metrics

| Metric | Value |
|--------|-------|
| DANDI_EVENT_BR | 401x |
| DANDI_RMSE | 78.44 uV |

## What We Don't Claim

- No claim of lossless signal reconstruction.
- No claim that the window-scoped event-encoding ratios are whole-recording compression results.
- No claim of blind-clone authority replay.
- No claim of commercialization-safe closure or tagged public release.
- No promoted claim of second-target breadth closure from this README surface.
- No claim beyond the bounded extracellular lane.

## Repo Shape

| Field | Value |
|-------|-------|
| Proof Anchors | 4 |
| Modality Lanes | 1 |
| Authority Source | `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` |

- `src/zpe_neuro/`: installable extractor package.
- `tests/`: repo-local verification slice.
- `tools/`: gate runners and operator scripts.
- `proofs/`: current authority packet plus retained March 21 evidence.
- `docs/`: architecture, legal boundaries, and dataset-scope notes.

## Quick Start

```bash
git clone https://github.com/Zer0pa/ZPE-Neuro.git
cd ZPE-Neuro
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest tests
```

For the bounded gate slice:

```bash
python -m pip install -e '.[gate,proof]'
python tools/run_gate_c.py --artifact-root artifacts/manual_gate_c --seed 20260220
python tools/run_gate_d.py --artifact-root artifacts/manual_gate_d --replay-seeds 20260220,20260221,20260222,20260223,20260224
```

Read [docs/LEGAL_BOUNDARIES.md](docs/LEGAL_BOUNDARIES.md) before widening any claim from this repo state.
