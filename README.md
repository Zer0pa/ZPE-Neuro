<h1 align="center">ZPE-Neuro</h1>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-SAL%20v7.0-e5e7eb?labelColor=111111" alt="License: SAL v7.1"></a>
  <a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><img src="https://img.shields.io/badge/authority-2026--04--24%20repo%20snapshot-e5e7eb?labelColor=111111" alt="Authority: 2026-04-24 repo snapshot"></a>
  <a href="docs/RELEASE_STATUS.md"><img src="https://img.shields.io/badge/release-private%20staged-e5e7eb?labelColor=111111" alt="Release: private staged"></a>
  <a href="docs/LEGAL_BOUNDARIES.md"><img src="https://img.shields.io/badge/lane-extracellular%20recording-e5e7eb?labelColor=111111" alt="Lane: extracellular recording"></a>
</p>

## What This Is

Extracellular recording codec. Bounded spike-event extraction for electrophysiology signals, independent of other portfolio lanes. Install from PyPI: `pip install zpe-neuro`

The strongest CI-anchored result to date: deterministic encode-decode round-trip on DANDI `000034` with a **401x event ratio**, **78.44 µV RMSE**, and Gate C + Gate D both `PASS` on blind-clone replay from the current `origin/main` snapshot. No comparison baseline exists for this lane; the numbers stand on their own terms.

This front door promotes only claims backed by a tracked proof artifact and exercised in CI. Treat [CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md) as the April 24 routing layer; the full proof archive goes deeper.

## Codec Mechanics

<p>
  <img src=".github/assets/readme/lane-mechanics/NEURO.gif" alt="ZPE-Neuro Codec Mechanics animation" width="100%">
</p>

| Field | Value |
| ------- | ------- |
| Architecture | SPIKE_STREAM |
| Encoding | NEURO_DELTA_V1 |
| Mechanics Asset | `.github/assets/readme/lane-mechanics/NEURO.gif` |

## Key Metrics

| Metric | Value | Baseline |
| -------- | ------- | ---------- |
| DANDI 000034 event ratio (window-scoped) | 401x |  |
| DANDI 000034 RMSE | 78.44 µV |  |
| Gate D embedded latency (p99) | 850 ns |  |
| Determinism (identical-hash runs) | 5 / 5 seeds |  |

> Source: April 24 blind-clone replay from `origin/main`. All four rows are CI-anchored or artifact-anchored per the proof packets in `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/`. Window-scoped metrics (6000-sample, 8-channel window at 30 kHz). Embedded latency uses a hardware-proxy cycle model at 80 MHz ARM-class clock; not a measured on-silicon result.

## Repo Identity

| Field | Value |
| ------- | ------- |
| Identifier | ZPE-Neuro |
| Repository | https://github.com/Zer0pa/ZPE-Neuro |
| Section | encoding |
| Visibility | PUBLIC |
| Architecture | SPIKE_STREAM |
| Encoding | NEURO_DELTA_V1 |
| Commit SHA | 7d30d52d704e |
| License | SAL-7.0 |
| Authority Source | proofs/manifests/CURRENT_AUTHORITY_PACKET.md |

## Readiness

| Field | Value |
| ------- | ------- |
| Verdict | PARTIAL |
| Checks | 6/6 |
| Anchors | 6 display anchors |
| Commit | 7d30d52d704e |
| Authority | proofs/manifests/CURRENT_AUTHORITY_PACKET.md |

### Honest Blocker

Blind-clone authority replay remains INC; no claim of lossless signal reconstruction; no claim beyond the extracellular lane.

## What We Prove

- DANDI 000034 remains the positive public anchor with 41 events, 401.04x event ratio, and 78.44 µV RMSE. Artifact: public_corpus_eval_dandi_000034_mouse412804_ecephys.json. CI: tests/test_dandi_offline.py.
- Blind-clone replay from current repo truth closed with Gate C and Gate D both PASS. Artifacts: verification_summary.md, gate_c_summary.json, gate_d_summary.json. CI: Verify Package Surface / proof-import-smoke, gate-slice, tests/test_roundtrip.py, tests/test_wave1_determinism.py.
- Breadth adjudication records IBL as the counted second extracellular target and does not count the Tier 1 DANDI anchor as breadth closure. Artifacts: public_corpus_summary.json, public_corpus_ibl_waveform_eval.json. CI: tests/test_breadth_adjudication.py.
- DANDI 000003 was executed as the first next-family DANDI breadth probe and recorded FAIL. Artifacts: public_corpus_eval_dandi_000003_yutamouse20_ecephys.json, dandi000003_decision.md. CI: tests/test_breadth_adjudication.py.
- AJILE12 remains explicitly out of family and is excluded from counted breadth. Artifacts: ajile12_family_boundary_decision.md, public_corpus_summary.json. CI: tests/test_breadth_adjudication.py.

## What We Don't Claim

- No claim of lossless signal reconstruction.
- No claim that the window-scoped event-encoding ratios are whole-recording compression results.
- No claim that DANDI 000003 closed new breadth.
- No claim of commercialization-safe closure or tagged public release.
- No claim beyond the bounded extracellular lane.

## Verification Status

| Code | Check | Verdict |
| ------ | ------- | --------- |
| T_01 | tests/test_dandi_offline.py::test_fixture_reproduces_benchmark_metrics — DANDI 000034 event ratio and RMSE match proof artifact | PASS |
| T_02 | tests/test_roundtrip.py — Encode-decode NWB roundtrip SHA256 bit-consistency | PASS |
| T_03 | tests/test_wave1_determinism.py — 5/5 seed determinism across blind-clone replay | PASS |
| T_04 | tests/test_breadth_adjudication.py — IBL counted breadth logic; DANDI 000003 FAIL recorded | PASS |
| T_05 | CI gate-slice — Gate D embedded latency p99 < 900 ns; drift cliff at 20 µm | PASS |
| T_06 | CI Verify Package Surface / proof-import-smoke — Package importable; proof artifacts present | PASS |

## Proof Anchors

| Path | State |
| ------ | ------- |
| `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` | VERIFIED |
| `proofs/artifacts/dandi000034_benchmark/benchmark_summary.json` | VERIFIED |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/verification_summary.md` | VERIFIED |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/gate_c_summary.json` | VERIFIED |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/gate_d_summary.json` | VERIFIED |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/determinism_replay_results.json` | VERIFIED |

## Repo Shape

| Field | Value |
| ------- | ------- |
| Proof Anchors | 6 display anchors |
| Modality Lanes | 1 |
| Architecture | SPIKE_STREAM |
| Encoding | NEURO_DELTA_V1 |
| Verification | 6/6 checks |
| Authority Source | proofs/manifests/CURRENT_AUTHORITY_PACKET.md |

- `src/zpe_neuro/`: installable extractor package.
- `tests/`: repo-local verification slice.
- `tools/`: gate runners and operator scripts.
- `proofs/`: current authority packet plus April 24 replay and breadth packets.
- `docs/`: architecture, legal boundaries, release status, and dataset-scope notes.

## Extended Metrics

Detailed metric rows retained from the previous `## Key Metrics` section. The public product page uses the four-row summary above.

### DANDI `000034` Tier-1 Authority Anchor

| Metric | Value | Proof artifact | CI test |
|--------|-------|----------------|---------|
| Event ratio (window-scoped) | 401x | [`benchmark_summary.json`](proofs/artifacts/dandi000034_benchmark/benchmark_summary.json) | `tests/test_dandi_offline.py::test_fixture_reproduces_benchmark_metrics` |
| RMSE | 78.44 µV | [`benchmark_summary.json`](proofs/artifacts/dandi000034_benchmark/benchmark_summary.json) | `tests/test_dandi_offline.py::test_fixture_reproduces_benchmark_metrics` |
| Encode latency (mean / max) | 0.089 ms / 0.208 ms | [`benchmark_summary.json`](proofs/artifacts/dandi000034_benchmark/benchmark_summary.json) | artifact only — no pytest bound asserted |
| Decode latency (mean / max) | 0.474 ms / 0.686 ms | [`benchmark_summary.json`](proofs/artifacts/dandi000034_benchmark/benchmark_summary.json) | artifact only — no pytest bound asserted |

These are window-scoped metrics (6000-sample, 8-channel window at 30 kHz). They are not whole-recording compression results.

### IBL Second-Target (Tier-2 Breadth, Counted PASS)

| Metric | Value | Proof artifact | CI test |
|--------|-------|----------------|---------|
| Event ratio (window-scoped) | 224x | [`public_corpus_ibl_waveform_eval.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_ibl_waveform_eval.json) | artifact only — `tests/test_breadth_adjudication.py` tests logic, not this metric value |
| RMSE | 38.16 µV | [`public_corpus_ibl_waveform_eval.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_ibl_waveform_eval.json) | artifact only — `tests/test_breadth_adjudication.py` tests logic, not this metric value |

### Gate D: Embedded Latency and Drift Resilience

| Metric | Value | Proof artifact | CI test |
|--------|-------|----------------|---------|
| Modeled latency (mean / p99) | 612.5 ns / 850 ns | [`neuro_embedded_latency.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/neuro_embedded_latency.json) | CI `gate-slice` |
| Latency threshold | < 900 ns | [`neuro_embedded_latency.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/neuro_embedded_latency.json) | CI `gate-slice` |
| Drift accuracy at 0–15 µm | 100% | [`neuro_drift_resilience.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/neuro_drift_resilience.json) | CI `gate-slice` |
| Drift cliff | at 20 µm | [`neuro_drift_resilience.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/neuro_drift_resilience.json) | CI `gate-slice` |

Embedded latency uses a hardware-proxy cycle model at 80 MHz ARM-class clock plus Python reference timing. It is not a measured on-silicon result.

### Determinism

| Metric | Value | Proof artifact | CI test |
|--------|-------|----------------|---------|
| Identical-hash runs | 5 / 5 seeds | [`determinism_replay_results.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/determinism_replay_results.json) | `tests/test_wave1_determinism.py`, `tests/test_roundtrip.py` |
| NWB roundtrip SHA256 | bit-consistent | [`neuro_nwb_roundtrip.json`](proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/neuro_nwb_roundtrip.json) | `tests/test_roundtrip.py` |

## Competitive Benchmarks

Two non-commensurable metrics, reported in two separate sections so they cannot be conflated. Reproduce with `python scripts/comp_benchmark/run_neuro_comparison.py`. Full numbers in [`proofs/artifacts/comp_benchmarks/neuro_codec_comparison.json`](proofs/artifacts/comp_benchmarks/neuro_codec_comparison.json).

### Lossless raw-channel comparison

Operating on the raw int16 samples in `tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz` (8 channels x 6000 samples = 96000 bytes), with no information loss.

| Codec | CR on int16 fixture | Notes |
|-------|---------------------|-------|
| gzip (level 6) | 2.20x | stdlib `gzip.compress` |
| lz4 (frame, default) | 1.42x | `lz4.frame.compress` |
| zstd (level 3) | 2.17x | `zstandard.ZstdCompressor(level=3)` |

ZPE-Neuro is not in this table. It is not a lossless general-purpose compressor and is not commensurable with these baselines.

### ZPE event-extraction ratio (lossy by design)

ZPE-Neuro's 401x ratio is a LOSSY event-extraction operation: it drops non-event samples and retains spike events (41 events kept from 48000 input samples; 768000 raw bits -> 1915 encoded bits on the same window). Window-scoped fidelity at this operating point is RMSE 78.44 µV with `roundtrip_exact=False` and `roundtrip_fidelity=0.0792` per [`benchmark_summary.json`](proofs/artifacts/dandi000034_benchmark/benchmark_summary.json). This is not comparable to the lossless CRs above; reading "401x vs gzip 2.2x" as "ZPE is ~180x better than gzip" is a category error - they are different operations on different outputs. For lossless raw-channel storage, gzip/lz4/zstd remain the appropriate baselines.

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

## Upcoming Workstreams

This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **Second passing DANDI corpus** — Active Engineering. Pure data-ingestion work; closes the breadth gap (currently 1 passing corpus) and unlocks the commercialization-safe release gate.
- **DANDI 000003 FAIL diagnosis** — Research-Deferred — Investigation Underway. Determine whether the failure is a corpus property (announce out-of-scope) or a primitive gap (close it).
