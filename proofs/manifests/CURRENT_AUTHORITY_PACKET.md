<p>
  <img src="../../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

# Current Authority Packet

Snapshot date: `2026-03-21`

This manifest is the canonical routing layer for the live shipped ZPE-Neuro
proof surface. Use it before treating any packet, receipt, or dated artifact as
current authority.

## Current Authority Stack

| Claim layer | Current authority | Notes |
|---|---|---|
| Front-door repo posture | [README.md](../../README.md) | current authority block and routing only |
| Current technical release surface | [proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/](../selected_artifacts/2026-03-21_zpe_neuro_release_alignment/README.md) | March 21 package/install/gate alignment packet |
| Current bounded lane evidence | [proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/](../selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/README.md) | self-contained March 21 bounded extracellular packet |
| Current positive Tier 1 anchor | [DANDI anchor eval](../selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json) | DANDI `000034` remains the strongest positive public anchor |
| Current counted second-target authority | [IBL waveform eval](../selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json) | bounded IBL second-target `PASS` within scope |
| Current lane boundary | [public_corpus_summary.json](../selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json) | AJILE12 is out-of-family and the lane remains extracellular |
| Current release boundary | [docs/LEGAL_BOUNDARIES.md](../../docs/LEGAL_BOUNDARIES.md) | blind-clone and public release remain open |
| Current legal/commercial boundary | [docs/LEGAL_BOUNDARIES.md](../../docs/LEGAL_BOUNDARIES.md) | commercialization remains open |

## Retired Legacy Surfaces

| Surface | Current reading |
|---|---|
| February 21 and March 20/21 bridge packets | removed from the live proof surface on `2026-03-22` after the current March 21 packets were made self-contained |
| `docs/team_packet/` | removed from the current documentation surface; chronology now routes through [CHANGELOG.md](../../CHANGELOG.md) |

## Drift Closed In The Current Surface

- the current March 21 refinement packet now carries its own DANDI and AJILE
  selection artifacts instead of depending on March 20 bridge folders
- the default breadth-adjudication code path now points at the current March 21
  refinement packet
- the family-boundary memo inside the current packet now matches the
  machine-readable `PASS` verdict for the counted IBL second target

## Reading Order

1. [README.md](../../README.md)
2. [docs/LEGAL_BOUNDARIES.md](../../docs/LEGAL_BOUNDARIES.md)
3. [docs/ARCHITECTURE.md](../../docs/ARCHITECTURE.md)
4. [proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/](../selected_artifacts/2026-03-21_zpe_neuro_release_alignment/README.md)
5. [proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/](../selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/README.md)
6. [CHANGELOG.md](../../CHANGELOG.md)
