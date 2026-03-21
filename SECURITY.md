<p>
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/reporting-a-vulnerability.svg" alt="REPORTING A VULNERABILITY" width="100%">
</p>

This policy covers the `zpe_neuro` package surface, the shipped GitHub
workflow logic, and the tracked proof/documentation corpus in this repository.

Canonical anchors:
- Repository: `https://github.com/Zer0pa/ZPE-Neuro`
- Contact: `architects@zer0pa.ai`

Do not open a public issue for a security vulnerability.

Report privately to:
- `architects@zer0pa.ai`

<p>
  <img src=".github/assets/readme/section-bars/scope.svg" alt="SCOPE" width="100%">
</p>

In scope:
- arbitrary code execution or unsafe deserialization paths
- secret exposure in tracked files or workflows
- dependency or supply-chain risks in declared install surfaces
- release-process or CI flaws that could publish private material

Out of scope for this policy:
- ordinary codec or regression failures
- evidence disputes backed by proof review
- inconclusive scientific or commercialization status

Those are engineering, governance, or evidence issues and should be routed
through the normal repo workflows instead.

<p>
  <img src=".github/assets/readme/section-bars/response-commitment.svg" alt="RESPONSE COMMITMENT" width="100%">
</p>

Target response windows:
- acknowledgement within 48 hours
- initial assessment within 7 days
- remediation plan for confirmed issues within 30 days

This is still a private staged repo. No public-release security posture is
implied beyond the currently shipped package and workflow surface.
