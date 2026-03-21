# Phase Context: Public Corpus Window Policy

**Phase:** 01
**Status:** Ready for planning

## Objective

Replace the current fixed first-window public probe with a reproducible candidate-window policy that improves truthfulness without weakening the existing DANDI Tier 1 authority anchor.

## Hard Constraints

- The DANDI `000034` pass is sovereign and must not regress.
- Quiet-slice compression or zero-RMSE wins must not count as evidence.
- Work stays local on the M1 for this phase.
- Disk headroom is tight, so candidate scanning must avoid large downloads or persistent caches.

## Inputs That Must Stay Visible

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_summary.json`
- `docs/team_packet/07_WAY_FORWARD.md`

## Decision Points

1. Candidate windows should be selected deterministically from the source series rather than by hand.
2. The scoring policy should prefer signal engagement and explicit eventfulness, not only compression.
3. The phase succeeds if it makes the public verdict more trustworthy, even if AJILE12 still fails.
