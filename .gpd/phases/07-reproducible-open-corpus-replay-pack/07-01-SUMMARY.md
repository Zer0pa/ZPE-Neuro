# Phase 07-01 Summary: Offline Replay Surface

## Objective

Land the first honest reproducibility-hardening slice for the public replay surface: committed offline fixture, fixture-backed tests, explicit reproduction commands, and CI coverage.

## What Landed

- Added fixture serialization and loading helpers to `src/zpe_neuro/public_corpus.py`.
- Added `tools/create_public_corpus_fixture.py` to refresh the committed DANDI-derived fixture from the existing streaming replay path.
- Added the committed fixture `tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz`.
- Added offline tests for codec roundtrip, edge cases, DANDI fixture replay, and scaling behavior.
- Added `Makefile` and `REPRODUCING.md` as the stable operator surface.
- Extended `.github/workflows/verify-package.yml` with an explicit fixture-backed offline replay job.
- Replaced the slow DANDI asset scan with `get_asset_by_path()` so fixture generation and replay do not brute-force the full asset list.

## Evidence

- Fixture refresh succeeded from the live DANDI stream:
  - target: `dandi_000034_mouse412804_ecephys`
  - path: `tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz`
  - size: `52,274` bytes
  - sha256: `0dbd7cee679e70dc8f7c3495eaf63726a2c3d92dbe5267e694685545e07ee99f`
  - selected start sample: `16871250`
  - codec event count in fixture slice: `41`
- Offline replay slice:
  - `12` fixture/roundtrip/scaling tests passed
- Full current suite:
  - `22` tests passed locally

## What This Does Not Prove

- It does not replace a fresh full public rerun packet.
- It does not convert AJILE12 into a counted in-family authority target.
- It does not close the GPU-only KiloSort4 / RunPod path.

## Remaining Phase 7 Work

- `07-02`: clarify or slightly refine the sanctioned replay entrypoint and produce a bounded fresh replay packet without drifting the current counting policy.
- `07-03`: document and probe the RunPod KiloSort4 path with provenance while keeping it supplemental.
