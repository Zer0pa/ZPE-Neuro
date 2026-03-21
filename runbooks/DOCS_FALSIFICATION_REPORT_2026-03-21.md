# Docs Falsification Report

Date: `2026-03-21`
Repo: `https://github.com/Zer0pa/ZPE-Neuro`

## Unsupported Claims Removed Or Downgraded

- downgraded the February 21 closure packet from front-door authority to `HISTORICAL_ONLY`
- stopped using ignored local `artifacts/2026-03-21_*` paths as README or docs proof anchors
- kept IBL chunked-waveform and Allen parity surfaces as `OPERATOR_ONLY` rather than packaged extras
- marked the `docs/team_packet/` handoff set as historical/internal so it no longer competes with the front door

## Path And Render Issues Found

- the repo had no local `.github/assets/readme/` tree, so the ZPE-IMC masthead/nav/section-bar assets were copied in
- root and nested doc asset paths were normalized to the correct relative depth
- README in-page anchor links were validated against explicit `<a id>` targets
- file-link and image-path checks passed after the rewrite

## Remaining Owner Inputs

- whether the default breadth-adjudication code path should be retargeted from the pre-refinement fail bundle to the later bounded-IBL pass bundle
- whether the operator-only IBL path should ever be promoted to a shipped extra after dependency and blind-clone closure

## Live-Vs-Local Drift Found And Resolved

- local docs and proof routing disagreed about whether February 21 or March 21 was current; resolved by adding `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- the current technical alignment evidence existed only under ignored local artifacts; resolved by promoting a tracked March 21 release-alignment packet under `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/`
- the private remote was in sync with `origin/main` before this docs pass; after commit and push, the remote should match the rewritten local doc surface
