<h1 align="center">ZPE-Neuro</h1>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-SAL%20v7.0-e5e7eb?labelColor=111111" alt="License: SAL v7.0"></a>
  <a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><img src="https://img.shields.io/badge/authority-2026--03--21%20repo%20snapshot-e5e7eb?labelColor=111111" alt="Authority: 2026-03-21 repo snapshot"></a>
  <a href="RELEASING.md"><img src="https://img.shields.io/badge/release-private%20staged-e5e7eb?labelColor=111111" alt="Release: private staged"></a>
  <a href="docs/LEGAL_BOUNDARIES.md"><img src="https://img.shields.io/badge/lane-extracellular%20recording-e5e7eb?labelColor=111111" alt="Lane: extracellular recording"></a>
</p>

## What This Is

Deterministic spike-event extraction for extracellular neuroscience pipelines. The honest wedge is reproducibility for bounded public datasets, not broad neural compression and not full-signal reconstruction.

ZPE-Neuro is aimed at neurotech research-infrastructure teams and academic neuroscience platforms that need stable spike-event encoding, replay, and audit lineage across runs. The current authority packet is real and narrow: DANDI `000034` plus a bounded IBL second-target pass. It does not close blind-clone replay, commercialization-safe closure, or broader neural scope.

| Field | Value |
|-------|-------|
| Architecture | SPIKE_STREAM |
| Encoding | NEURO_DELTA_V1 |

## Key Metrics

| Metric | Value | Baseline |
|--------|-------|----------|
| DANDI_EVENT_BR | 401× | — |
| IBL_EVENT_BR | 224× | — |
| DANDI_RMSE | 78.44 µV | — |
| IBL_RMSE | 38.16 µV | — |

Source: [`public_corpus_eval_dandi_000034_mouse412804_ecephys.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json), [`public_corpus_ibl_waveform_eval.json`](proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json)

## Competitive Benchmarks

No promoted incumbent-comparator table is live on the current authority surface. The honest reading is narrower: this repo proves a reproducible spike-event extractor on bounded extracellular slices, not a general neural-codec displacement story.

| Comparator Surface | Current Reading | Notes |
|--------------------|-----------------|-------|
| Public incumbent benchmark | Not promoted | The current packet is about bounded reproducibility and lineage, not market-wide comparator closure |

## What We Prove

- Deterministic spike-event extraction and encoding on DANDI `000034` extracellular data.
- A bounded IBL second-target pass under the March 21 refinement packet.
- NWB-compatible packaging and auditable lineage for the current public dataset slice.
- Explicit family-boundary handling: AJILE12 is documented as out of family for the current lane rather than quietly dropped.

## What We Don't Claim

- No claim of lossless signal reconstruction.
- No claim that the window-scoped event-encoding ratios are whole-recording compression results.
- No claim of blind-clone authority replay.
- No claim of commercialization-safe closure or tagged public release.
- No claim beyond the extracellular lane.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | STAGED |
| Commit SHA | 7d30d52d704e |
| Confidence | 100% |
| Source | proofs/manifests/CURRENT_AUTHORITY_PACKET.md |

## Tests and Verification

| Code | Check | Verdict |
|------|-------|---------|
| V_01 | DANDI public anchor | PASS |
| V_02 | IBL bounded refinement | PASS |
| V_03 | NWB-compatible package surface | PASS |
| V_04 | Family-boundary adjudication | PASS |
| V_05 | Blind-clone authority replay | INC |

## Proof Anchors

| Path | State |
|------|-------|
| `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/verification_summary.md` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_c_summary.json` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_d_summary.json` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json` | VERIFIED |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` | VERIFIED |

## Repo Shape

| Field | Value |
|-------|-------|
| Proof Anchors | 7 |
| Modality Lanes | 1 |
| Authority Source | `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` |

- `src/zpe_neuro/`: installable extractor package.
- `tests/`: repo-local verification slice.
- `tools/`: gate runners and operator scripts.
- `proofs/`: current authority packet plus retained March 21 evidence.
- `docs/`: architecture, legal boundaries, and dataset-scope notes.

## Quick Start

```bash
# Install from PyPI
pip install zpe-neuro
```

Or install from source for the repo-local verification path:

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
