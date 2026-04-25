<h1 align="center">ZPE-Neuro</h1>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-SAL%20v7.0-e5e7eb?labelColor=111111" alt="License: SAL v7.0"></a>
  <a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><img src="https://img.shields.io/badge/authority-2026--04--24%20repo%20snapshot-e5e7eb?labelColor=111111" alt="Authority: 2026-04-24 repo snapshot"></a>
  <a href="docs/RELEASE_STATUS.md"><img src="https://img.shields.io/badge/release-private%20staged-e5e7eb?labelColor=111111" alt="Release: private staged"></a>
  <a href="docs/LEGAL_BOUNDARIES.md"><img src="https://img.shields.io/badge/lane-extracellular%20recording-e5e7eb?labelColor=111111" alt="Lane: extracellular recording"></a>
</p>

## What This Is

ZPE-Neuro is a bounded extracellular spike-event extraction surface. The live README only promotes claims that are backed by a tracked proof artifact and exercised in CI. Treat [CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md) as the April 24 routing layer; this front door stays narrower than the full proof archive on purpose.

## Current Verified Surface

| Claim | Proof artifact | CI coverage |
|-------|----------------|-------------|
| DANDI `000034` remains the positive public anchor with `41` events, `401.04x` event ratio, and `78.44 uV` RMSE. | [`public_corpus_eval_dandi_000034_mouse412804_ecephys.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_eval_dandi_000034_mouse412804_ecephys.json) | `tests/test_dandi_offline.py` |
| Blind-clone replay from current repo truth closed with Gate C and Gate D both `PASS`. | [`verification_summary.md`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/verification_summary.md), [`gate_c_summary.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/gate_c_summary.json), [`gate_d_summary.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/gate_d_summary.json) | `Verify Package Surface / proof-import-smoke`, `gate-slice`, `tests/test_roundtrip.py`, `tests/test_wave1_determinism.py` |
| Breadth adjudication records IBL as the counted second extracellular target and does not count the Tier 1 DANDI anchor as breadth closure. | [`public_corpus_summary.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_summary.json), [`public_corpus_ibl_waveform_eval.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_ibl_waveform_eval.json) | `tests/test_breadth_adjudication.py` |
| DANDI `000003` was executed as the first next-family DANDI breadth probe and recorded `FAIL`. | [`public_corpus_eval_dandi_000003_yutamouse20_ecephys.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_eval_dandi_000003_yutamouse20_ecephys.json), [`dandi000003_decision.md`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/dandi000003_decision.md) | `tests/test_breadth_adjudication.py` |
| AJILE12 remains explicitly out of family and is excluded from counted breadth. | [`ajile12_family_boundary_decision.md`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/ajile12_family_boundary_decision.md), [`public_corpus_summary.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_summary.json) | `tests/test_breadth_adjudication.py` |

## Current Metrics

| Metric | Value |
|--------|-------|
| DANDI_EVENT_BR | 401x |
| DANDI_RMSE | 78.44 uV |

## What We Don't Claim

- No claim of lossless signal reconstruction.
- No claim that the window-scoped event-encoding ratios are whole-recording compression results.
- No claim that DANDI `000003` closed new breadth.
- No claim of commercialization-safe closure or tagged public release.
- No claim beyond the bounded extracellular lane.

## Repo Shape

| Field | Value |
|-------|-------|
| Proof Anchors | 5 |
| Modality Lanes | 1 |
| Authority Source | `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` |

- `src/zpe_neuro/`: installable extractor package.
- `tests/`: repo-local verification slice.
- `tools/`: gate runners and operator scripts.
- `proofs/`: current authority packet plus April 24 replay and breadth packets.
- `docs/`: architecture, legal boundaries, release status, and dataset-scope notes.

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
