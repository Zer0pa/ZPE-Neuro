<p>
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/what-this-is.svg" alt="WHAT THIS IS" width="100%">
</p>

This document defines the public documentation and evidence-governance boundary
for ZPE-Neuro.

Canonical anchors:
- Repository: private GitHub repo `https://github.com/Zer0pa/ZPE-Neuro` for authorized readers
- Contact: `architects@zer0pa.ai`

<p>
  <img src=".github/assets/readme/section-bars/evidence-and-claims.svg" alt="EVIDENCE AND CLAIMS" width="100%">
</p>

Governance baseline:
- runtime and tracked artifact truth outrank prose
- contradictions are retained, not averaged away
- a later tracked authority packet outranks an earlier historical packet
- ignored local-only artifacts may inform current operator work, but they do
  not become shipped GitHub proof anchors until promoted into a tracked surface
- private staging is the default unless the release gate says otherwise

Authority classes:

| Class | Meaning |
|---|---|
| `CURRENT` | The latest shipped repo authority surface for the named claim layer. |
| `SUPPORTING` | Reinforces the current claim layer but does not outrank the canonical current packet. |
| `HISTORICAL_ONLY` | Preserved for lineage, contradiction review, or chronology. |
| `OPERATOR_ONLY` | Real local work surface, but not a shipped GitHub proof anchor. |

<p>
  <img src=".github/assets/readme/section-bars/status-semantics.svg" alt="STATUS SEMANTICS" width="100%">
</p>

| Token | Meaning |
|---|---|
| `PASS` | The cited artifact supports the stated gate or measurement within explicit scope. |
| `BOUNDED_PASS` | The cited artifact passes inside an explicit bounded lane or narrow claim surface. |
| `INCONCLUSIVE` | Evidence conflict or missing support remains. |
| `FAIL` | The named gate or claim is not met within scope. |
| `OPEN` | The required release, commercialization, or acceptance condition is not closed. |
| `PRIVATE_STAGED` | Current repo posture: real tracked work, not a public release. |
| `NO_PUBLIC_RELEASE` | No public release verdict is claimed from the current repo state. |
| `OUT_OF_FAMILY` | A dataset or modality is intentionally outside the current supported lane. |
| `PARKED_BY_SCOPE` | Deferred intentionally because it is outside the current lane lock. |
| `KNOWN_RESIDUE` | A remaining non-authoritative imperfection is explicitly documented. |
| `HISTORICAL_ONLY` | The artifact remains in the repo for lineage and contradiction review, not as current authority. |
| `OPERATOR_ONLY` | The surface exists locally but is not part of the current shipped GitHub proof surface. |

Current governance locks:
- sovereign acceptance gate: fresh clean-clone authority-packet verification
- current lane scope: narrow extracellular recording lane
- current clean packaged baseline: base package plus `gate`, `public`, and
  `proof` extras only
- current open commercial boundary: Allen parity/commercialization closure

<p>
  <img src=".github/assets/readme/section-bars/escalation-path.svg" alt="ESCALATION PATH" width="100%">
</p>

Escalate when:
- a doc and a tracked artifact disagree
- a later packet silently contradicts the current authority manifest
- a claim upgrade lacks a tracked path in the repo
- a local-only artifact is about to be promoted without a shipped summary

If a difference is intentional, the reason must be explicit in the doc that
differs. Silent drift is failure.
