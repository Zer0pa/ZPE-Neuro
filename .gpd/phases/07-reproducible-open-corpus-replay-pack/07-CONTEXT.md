# Phase 07 Context

## Decisions

- Treat Phase 7 as reproducibility and replay-surface hardening, not as new authority closure.
- Do not count DANDI `000055`, AJILE12, Allen, or any other downloadable corpus as a new in-family authority pass unless executed proof artifacts land in `proofs/` and overturn the current boundary honestly.
- Prefer existing repo proof artifacts as the source for the offline fixture; avoid large new downloads on this Mac for the first execution slice.
- Public replay commands must be explicit and reusable, but command availability alone does not count as evidence.
- GPU-only KiloSort4 work is optional and must stay separate from the CPU/offline verification baseline.

## Agent's Discretion

- Whether to add a thin `PublicCorpusRunner` wrapper or equivalent target-selection surface on top of the current public-corpus functions.
- How to package fixture metadata and which fixture-backed tests best capture codec, roundtrip, and scaling behavior.
- How to structure Make targets and CI so the offline verify path is obvious and durable.
- Whether bounded `000055` diagnostics belong in this phase at all, or should remain documented-but-deferred after the fixture/repro surface lands.

## Deferred Ideas

- Full DANDI `000034` or `000055` downloads on this Mac.
- Allen or broader open-neuro expansion runs.
- Long-form KiloSort4 remote debugging if it would dominate the phase.
- Any README, release, or commercialization-language upgrade from the improved surface alone.

## Must Read

- `/Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro_ACTION_BRIEF.md`
- `/Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro/.gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md`
- `/Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro/proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/dandi_000034_mouse412804_ecephys/gate_c_roundtrip.nwb`
