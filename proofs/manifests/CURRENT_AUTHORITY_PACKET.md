<p>
  <img src="../../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

# Current Authority Packet

Snapshot date: `2026-04-24`

This manifest is the canonical routing layer for the live shipped ZPE-Neuro
proof surface. Use it before treating any packet, receipt, or dated artifact as
current authority.

## Current Authority Stack

| Claim layer | Current authority | Notes |
|---|---|---|
| Front-door repo posture | [README.md](../../README.md) | current authority block and routing only |
| Current technical release surface | [proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/](../selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/README.md) | April 24 blind-clone replay packet from current `origin/main` truth |
| Current bounded lane evidence | [proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/README.md) | current bounded extracellular packet with first DANDI `000003` breadth result |
| Current positive Tier 1 anchor | [DANDI anchor eval](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_eval_dandi_000034_mouse412804_ecephys.json) | DANDI `000034` remains the strongest positive public anchor |
| Current counted second-target authority | [IBL waveform eval](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_ibl_waveform_eval.json) | bounded IBL second-target `PASS` remains counted within scope |
| Current next in-family breadth attempt | [DANDI `000003` eval](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_eval_dandi_000003_yutamouse20_ecephys.json) | first next-family DANDI breadth probe recorded an honest `FAIL` |
| Current lane boundary | [public_corpus_summary.json](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/public_corpus_summary.json) | AJILE12 remains out of family; DANDI `000003` did not close new breadth |
| Current release boundary | [docs/RELEASE_STATUS.md](../../docs/RELEASE_STATUS.md) | blind-clone replay is closed; commercialization and public release remain open |
| Current legal/commercial boundary | [docs/LEGAL_BOUNDARIES.md](../../docs/LEGAL_BOUNDARIES.md) | commercialization remains open |

## Retired Legacy Surfaces

| Surface | Current reading |
|---|---|
| March 21 packets | retained as historical supporting packets, but superseded by the April 24 replay and breadth packets for live routing |
| `docs/team_packet/` | removed from the current documentation surface; chronology now routes through `CHANGELOG.md` and retained proof packets |

## Drift Closed In The Current Surface

- the live surface now carries a clean blind-clone replay packet from current
  `origin/main` truth
- the live bounded lane packet now records the first DANDI `000003` breadth
  attempt instead of leaving that target only in planning docs
- dead `RELEASING.md` routing is replaced by `docs/RELEASE_STATUS.md`

## Reading Order

1. [README.md](../../README.md)
2. [docs/RELEASE_STATUS.md](../../docs/RELEASE_STATUS.md)
3. [docs/ARCHITECTURE.md](../../docs/ARCHITECTURE.md)
4. [proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/](../selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/README.md)
5. [proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/](../selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/README.md)
6. [CHANGELOG.md](../../CHANGELOG.md)
