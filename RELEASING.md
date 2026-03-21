<p>
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/release-gate.svg" alt="RELEASE GATE" width="100%">
</p>

This document defines the release gate and decision boundary for ZPE-Neuro.

Canonical anchors:
- Repository: private GitHub repo `https://github.com/Zer0pa/ZPE-Neuro` for authorized readers
- Contact: `architects@zer0pa.ai`

<p>
  <img src=".github/assets/readme/section-bars/scope.svg" alt="SCOPE" width="100%">
</p>

Release statements in this repository are bounded to evidence-backed technical
claims and the current shipped proof surface.

Current release posture:
- package, install, docs, and proof surfaces are aligned for the current
  private staged repo
- not blind-clone closed
- not a public-release verdict

<p>
  <img src=".github/assets/readme/section-bars/verification.svg" alt="VERIFICATION" width="100%">
</p>

| Gate | Required state | Current state |
|---|---|---|
| Packaged install truth | declared extras build and import cleanly | `PASS` |
| Shipped test truth | shipped test slice runs from a checkout | `PASS` |
| Shipped gate truth | sequential Gate C and Gate D replay from the declared gate stack | `PASS` |
| Proof-surface truth | current shipped proof packet and authority manifest are coherent | `PASS` |
| Blind-clone authority pack | fresh clean-clone authority replay | `OPEN` |
| Public-release boundary | owner ratification that public-release gate is closed | `OPEN` |
| Commercialization boundary | Allen/comparator/licensing closure | `OPEN` |

<p>
  <img src=".github/assets/readme/section-bars/release-consequences.svg" alt="RELEASE CONSEQUENCES" width="100%">
</p>

Until the open gates close:
- keep release language private-staged
- do not claim public-release readiness
- do not treat operator-only extras as shipped install surfaces
- keep commercialization posture explicit

The current docs pass closes documentation drift around the shipped repo
surface. It does not override the blind-clone, public-release, or
commercialization gates.
