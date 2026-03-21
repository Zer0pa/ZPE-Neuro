# Phase Context: IBL Waveform Slice Execution

**Phase:** 02
**Status:** Ready for planning

## Objective

Turn IBL from a metadata-only public probe into a real local waveform-slice execution path on the M1, or record a measured local block honestly enough to justify any later escalation.

## Hard Constraints

- The DANDI `000034` anchor remains sovereign and must not be traded away for breadth theater.
- Metadata-only IBL access does not count as second-target waveform execution.
- Work stays local on the M1 unless a measured local block is recorded and the user explicitly approves escalation.
- Disk headroom is still limited, so the IBL path must minimize bytes materialized and cache growth.
- Sensitive local auth material may inform debugging, but it must not appear in artifacts, receipts, or user-facing summaries.

## Inputs That Must Stay Visible

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_ibl_probe.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `docs/team_packet/07_WAY_FORWARD.md`
- `runbooks/20260320T180048Z_codex_receipt.md`

## Decision Points

1. Prefer the public unsigned S3 route if it yields raw AP bytes without depending on a fragile authenticated ONE session.
2. Treat one compressed AP chunk plus the companion `.meta` and `.ch` files as the smallest honest local waveform path.
3. Keep waveform execution status separate from downstream insertion success so the artifact does not collapse existence evidence into a pass narrative.
