<p>
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/changelog.svg" alt="CHANGELOG" width="100%">
</p>

This changelog tracks repo-surface changes for ZPE-Neuro. It is not a full
scientific chronology and it does not replace the proof packets.

Canonical anchors:
- Repository: `https://github.com/Zer0pa/ZPE-Neuro`
- Contact: `architects@zer0pa.ai`

<p>
  <img src=".github/assets/readme/section-bars/unreleased.svg" alt="UNRELEASED" width="100%">
</p>

## Unreleased

### 2026-03-22
- collapsed the live proof surface onto the current March 21 release-alignment
  and IBL-refinement packets
- made the March 21 IBL refinement packet self-contained by folding forward the
  DANDI and AJILE support artifacts it still depended on
- removed superseded bridge proof folders and the historical `docs/team_packet/`
  handoff set from the live repo surface
- updated the breadth-adjudication defaults so runtime defaults match the
  current authority packet
- tightened status semantics, section-bar labeling, and root README navigation
  around the actual current repo truth

### 2026-03-21
- aligned package metadata and dependency truth to the clean install surface
  that actually builds and imports
- added explicit artifact-root handling to repo-local gate and replay runners
- added `.github/workflows/verify-package.yml` for build/import/test/gate truth
  checks without adding a publish step
- promoted a tracked March 21 release-alignment proof packet and a current
  authority manifest so the docs do not point at ignored local artifacts
- rewrote the root doc surface to the ZPE-IMC structural standard while
  keeping ZPE-Neuro-specific truth, scope limits, and open gaps
- created canonical release, FAQ, support, and doc-registry surfaces

### Notes
- no public release is declared by this changelog entry
- blind-clone closure and commercialization remain open
