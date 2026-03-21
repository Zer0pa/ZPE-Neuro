<p>
  <img src="../../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

# Current Authority Packet

Snapshot date: `2026-03-21`

This manifest is the canonical routing layer for the current ZPE-Neuro proof
surface. Use it before treating any dated packet as current authority.

## Current Authority Stack

| Claim layer | Current authority | Notes |
|---|---|---|
| Front-door repo posture | `README.md` | current authority block and routing only |
| Current technical release surface | `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/` | March 21 package/install/gate alignment packet |
| Current bounded lane evidence | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` | latest machine-readable lane verdict |
| Current positive Tier 1 anchor | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` | DANDI `000034` remains sovereign positive anchor |
| Current counted second-target authority | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_ibl_waveform_eval.json` | bounded IBL second-target `PASS` within scope |
| Current lane boundary | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` | AJILE12 is out-of-family and the lane remains extracellular |
| Current release boundary | `RELEASING.md` | blind-clone and public release remain open |
| Current legal/commercial boundary | `docs/LEGAL_BOUNDARIES.md` | commercialization remains open |

## Historical Packets

| Packet | How to read it now |
|---|---|
| `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/` | historical-only lineage and contradiction context |
| `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/` | historical bridge packet |
| `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/` | historical bridge packet |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_breadth_adjudication/` | early same-day pre-refinement fail packet |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_lane1_wedge_decision/` | supporting scope-rationale packet; not the latest breadth verdict |

## Known Drift Resolved By This Manifest

- Some older docs still route readers to the February 21 closure packet. That
  packet is historical-only for front-door status.
- The default breadth-adjudication code path still points at a pre-refinement
  fail bundle. That is a lagging runtime default, not the front-door authority
  surface.
- One prose family-boundary note inside the March 21 refinement bundle still
  contains pre-refinement wording about IBL failure. The machine-readable
  `public_corpus_summary.json` and `public_corpus_ibl_waveform_eval.json` are
  the authoritative lane verdict within that bundle.

## Reading Order

1. `README.md`
2. `RELEASING.md`
3. `docs/ARCHITECTURE.md`
4. `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/`
5. `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/`
6. `PUBLIC_AUDIT_LIMITS.md`
