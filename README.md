<h1 align="center">ZPE-Neuro</h1>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-SAL%20v6.0-e5e7eb?labelColor=111111" alt="License: SAL v6.0"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/python-3.11-e5e7eb?labelColor=111111" alt="Python 3.11"></a>
  <a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><img src="https://img.shields.io/badge/authority-2026--03--21%20repo%20snapshot-e5e7eb?labelColor=111111" alt="Authority: 2026-03-21 repo snapshot"></a>
  <a href="RELEASING.md"><img src="https://img.shields.io/badge/release-private%20staged-e5e7eb?labelColor=111111" alt="Release: private staged"></a>
  <a href="docs/LEGAL_BOUNDARIES.md"><img src="https://img.shields.io/badge/lane-extracellular%20recording-e5e7eb?labelColor=111111" alt="Lane: extracellular recording"></a>
</p>
<p align="center">
  <a href="AUDITOR_PLAYBOOK.md"><img src="https://img.shields.io/badge/quick%20verify-audit%20path-e5e7eb?labelColor=111111" alt="Quick verify"></a>
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/architecture-runtime%20map-e5e7eb?labelColor=111111" alt="Architecture runtime map"></a>
  <a href="PUBLIC_AUDIT_LIMITS.md"><img src="https://img.shields.io/badge/limits-honest%20reading-e5e7eb?labelColor=111111" alt="Honest reading limits"></a>
  <a href="docs/README.md"><img src="https://img.shields.io/badge/docs-canonical%20registry-e5e7eb?labelColor=111111" alt="Canonical docs registry"></a>
</p>

<table align="center" width="100%" cellpadding="0" cellspacing="0">
  <tr>
    <td width="25%"><a href="#what-this-is"><img src=".github/assets/readme/nav/what-this-is.svg" alt="What This Is" width="100%"></a></td>
    <td width="25%"><a href="#current-authority"><img src=".github/assets/readme/nav/current-authority.svg" alt="Current Authority" width="100%"></a></td>
    <td width="25%"><a href="#runtime-proof-wave-1"><img src=".github/assets/readme/nav/runtime-proof.svg" alt="Runtime Proof" width="100%"></a></td>
    <td width="25%"><a href="#quickstart-and-license"><img src=".github/assets/readme/nav/quickstart-and-license.svg" alt="Quickstart and License" width="100%"></a></td>
  </tr>
  <tr>
    <td width="25%"><a href="#proof-corpus"><img src=".github/assets/readme/nav/proof-corpus.svg" alt="Proof Corpus" width="100%"></a></td>
    <td width="25%"><a href="#open-risks"><img src=".github/assets/readme/nav/open-gaps.svg" alt="Open Risks" width="100%"></a></td>
    <td width="25%"><a href="#go-next"><img src=".github/assets/readme/nav/go-next.svg" alt="Go Next" width="100%"></a></td>
    <td width="25%"><a href="docs/README.md"><img src=".github/assets/readme/nav/docs-registry.svg" alt="Docs Registry" width="100%"></a></td>
  </tr>
</table>

---

<a id="commercial-front-door"></a>

## What This Is

ZPE-Neuro applies the ZPE deterministic 8-primitive encoding architecture to extracellular neural recordings. It is the neuro-signal lane of the Zer0pa family — scoped strictly to extracellular data, not broad neural generality.

The strongest current evidence: **DANDI 000034 extracellular validation** with deterministic round-trip fidelity, plus an **IBL second-target PASS** under bounded refinement conditions. Both are real public datasets with auditable lineage tracked in `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`. AJILE12 out-of-family handling is explicitly documented rather than silently excluded.

For neurotech research-infrastructure teams evaluating deterministic encoding for reproducible signal pipelines, this is the only codec in the family validated against public neuroscience archives. The proof corpus under `proofs/` carries full manifest lineage.

**Readiness: private-stage.** No blind-clone verification completed, no commercialization-safe closure gate passed, no tagged release. Extracellular lane only.

**Not claimed:** broad neural generality, intracellular support, public release readiness.

| Proof anchor | Location |
|---|---|
| DANDI 000034 validation | `proofs/` corpus |
| IBL second-target PASS | bounded refinement conditions |
| Authority routing | `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` |

Part of the [Zer0pa](https://github.com/zer0-point-energy) family. Platform layer: [ZPE-IMC](https://github.com/zer0-point-energy/ZPE-IMC).

---

<p>
  <img src=".github/assets/readme/section-bars/what-this-is.svg" alt="WHAT THIS IS" width="100%">
</p>

<a id="what-this-is"></a>
<h2 align="center">What This Is</h2>

ZPE-Neuro is the inner repository for the Wave-1 neural signal package, the
current curated proof corpus, and the release-surface documentation for the
Neuro workstream. It is a private staged repo, not a tagged public release.

The current scope lock is a narrower extracellular lane. The strongest honest
repo claim is not broad neural generality; it is a truthful Python package
surface plus a bounded evidence surface anchored on DANDI `000034`, a counted
IBL second-target `PASS` under bounded refinement, explicit AJILE12
out-of-family handling, and unresolved blind-clone/commercialization gates.

<p>
  <img src=".github/assets/readme/section-bars/current-authority.svg" alt="CURRENT AUTHORITY" width="100%">
</p>

<a id="current-authority"></a>
<h2 align="center">Current Authority</h2>

Use this table as the single canonical authority block for the repo front door.

<table width="100%" border="1" bordercolor="#111111" cellpadding="14" cellspacing="0">
  <thead>
    <tr>
      <th align="left" width="26%">Field</th>
      <th align="left" width="49%">Current truth</th>
      <th align="left" width="25%">Authority</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">Authority snapshot date</td>
      <td valign="top"><code>2026-03-21</code></td>
      <td valign="top"><a href="proofs/manifests/CURRENT_AUTHORITY_PACKET.md"><code>proofs/manifests/CURRENT_AUTHORITY_PACKET.md</code></a></td>
    </tr>
    <tr>
      <td valign="top">Repository / acquisition surface</td>
      <td valign="top">Canonical GitHub repo: <code>https://github.com/Zer0pa/ZPE-Neuro</code> for authorized readers. Clone surface for authorized readers: <code>git clone https://github.com/Zer0pa/ZPE-Neuro.git</code>.</td>
      <td valign="top"><code>AUDITOR_PLAYBOOK.md</code>, <code>docs/ARCHITECTURE.md</code></td>
    </tr>
    <tr>
      <td valign="top">Repo posture</td>
      <td valign="top"><code>PRIVATE_STAGED</code>. Package, install, docs, and proof surfaces are aligned for the current repo state, but this is not a public release and not a clean-clone-closed authority packet.</td>
      <td valign="top"><code>RELEASING.md</code>, <code>PUBLIC_AUDIT_LIMITS.md</code></td>
    </tr>
    <tr>
      <td valign="top">Top unresolved gate</td>
      <td valign="top">A fresh clean-clone replay of the authority packet remains the top unresolved acceptance gate.</td>
      <td valign="top"><code>RELEASING.md</code></td>
    </tr>
    <tr>
      <td valign="top">Gate status</td>
      <td valign="top"><code>OPEN</code> for blind-clone and public-release gates. <code>PASS</code> for the current clean packaged baseline and the tracked release-alignment gate slice.</td>
      <td valign="top"><a href="proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/README.md"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/</code></a></td>
    </tr>
    <tr>
      <td valign="top">Current lane / scope lock</td>
      <td valign="top">Lane 1 is a narrow extracellular recording lane. AJILE12 is explicitly <code>OUT_OF_FAMILY</code> for the current codec; broader human/intracranial coverage is not claimed here.</td>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json</code></td>
    </tr>
    <tr>
      <td valign="top">Primary positive public anchor</td>
      <td valign="top">DANDI <code>000034</code> remains the strongest positive public waveform anchor in the current repo surface.</td>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json</code></td>
    </tr>
    <tr>
      <td valign="top">Counted breadth verdict</td>
      <td valign="top"><code>PASS</code> in the current bounded local evidence packet after the March 21 IBL refinement. This does not upgrade blind-clone status or broader release claims.</td>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json</code></td>
    </tr>
    <tr>
      <td valign="top">Family-boundary decision</td>
      <td valign="top"><code>OUT_OF_FAMILY</code> for AJILE12 in the current lane.</td>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json</code></td>
    </tr>
    <tr>
      <td valign="top">Packaged clean baseline</td>
      <td valign="top"><code>PASS</code> for the packaged <code>.</code>, <code>.[gate]</code>, <code>.[public]</code>, and <code>.[proof]</code> surfaces that are actually declared for clean install/import. IBL chunked-waveform tooling and Allen parity remain operator-only.</td>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/verification_summary.md</code>, <code>pyproject.toml</code>, <code>docs/ARCHITECTURE.md</code></td>
    </tr>
    <tr>
      <td valign="top">Blind-clone verification status</td>
      <td valign="top"><code>OPEN</code></td>
      <td valign="top"><code>PUBLIC_AUDIT_LIMITS.md</code>, <code>RELEASING.md</code></td>
    </tr>
    <tr>
      <td valign="top">Release status</td>
      <td valign="top"><code>NO_PUBLIC_RELEASE</code>. The current repo surface is documented and internally coherent, but no public-release verdict is claimed.</td>
      <td valign="top"><code>RELEASING.md</code></td>
    </tr>
    <tr>
      <td valign="top">Commercialization status</td>
      <td valign="top"><code>OPEN</code>. Allen parity and commercialization closure remain unresolved.</td>
      <td valign="top"><code>docs/LEGAL_BOUNDARIES.md</code>, <code>RELEASING.md</code></td>
    </tr>
    <tr>
      <td valign="top">Primary authority artifacts</td>
      <td valign="top"><code>proofs/manifests/CURRENT_AUTHORITY_PACKET.md</code>, <code>proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/</code>, <code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/</code></td>
      <td valign="top"><code>proofs/README.md</code></td>
    </tr>
    <tr>
      <td valign="top">Audit route</td>
      <td valign="top">Start with the short replay path, then read the limits note before widening any claim.</td>
      <td valign="top"><code>AUDITOR_PLAYBOOK.md</code>, <code>PUBLIC_AUDIT_LIMITS.md</code></td>
    </tr>
  </tbody>
</table>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead-option-3-2.gif" alt="ZPE-Neuro Mid Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/runtime-proof-wave-1.svg" alt="RUNTIME PROOF (WAVE-1)" width="100%">
</p>

<a id="runtime-proof-wave-1"></a>
<h2 align="center">Runtime Proof And Package Truth</h2>

<table width="100%" border="1" bordercolor="#111111" cellpadding="14" cellspacing="0">
  <thead>
    <tr>
      <th align="left" width="26%">Surface</th>
      <th align="left" width="27%">Current state</th>
      <th align="left" width="47%">Why it matters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">Core package build/import</td>
      <td valign="top"><code>PASS</code></td>
      <td valign="top">The repo now ships a truthful Python package surface rather than relying on undeclared runtime assumptions.</td>
    </tr>
    <tr>
      <td valign="top">Repo-local tests</td>
      <td valign="top"><code>PASS</code> on the current shipped unit slice</td>
      <td valign="top">The staged code surface has a small but real regression check that ships with the repo.</td>
    </tr>
    <tr>
      <td valign="top">Synthetic gate baseline</td>
      <td valign="top"><code>PASS</code> for sequential Gate C and Gate D replay in the current clean packaged gate stack</td>
      <td valign="top">This is the strongest current shipped replay baseline in the repo.</td>
    </tr>
    <tr>
      <td valign="top">Public replay import surface</td>
      <td valign="top"><code>PASS</code> for the declared <code>.[proof]</code> import stack</td>
      <td valign="top">This keeps the docs honest about what the packaged replay stack actually installs cleanly.</td>
    </tr>
    <tr>
      <td valign="top">IBL and Allen operator paths</td>
      <td valign="top"><code>OPERATOR_ONLY</code></td>
      <td valign="top">Those paths currently require manual dependency/toolchain work around <code>ONE-api</code>, <code>ibl-neuropixel</code>, <code>llvmlite</code>/<code>numba</code>, or <code>allensdk</code> conflicts and are intentionally not shipped as clean extras.</td>
    </tr>
    <tr>
      <td valign="top">Release automation</td>
      <td valign="top"><code>PASS</code> for static verification coverage</td>
      <td valign="top">The repo now has a verification workflow that checks package/build/install truth without implying a live publish pipeline or automated publish step.</td>
    </tr>
  </tbody>
</table>

<p>
  <img src=".github/assets/readme/section-bars/quickstart-and-license.svg" alt="QUICKSTART AND LICENSE" width="100%">
</p>

<a id="quickstart-and-license"></a>
<h2 align="center">Quickstart And License</h2>

Acquire from the private GitHub repo if you have authorized access, then verify
the shipped package surface from a checkout.

```bash
git clone https://github.com/Zer0pa/ZPE-Neuro.git
cd ZPE-Neuro

python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -c "import zpe_neuro"
```

Repo-local test slice:

```bash
python -m pip install -e '.[dev]'
python -m pytest tests
```

Repo-local synthetic gate slice:

```bash
python -m pip install -e '.[gate,dev]'
python tools/run_gate_c.py --artifact-root artifacts/manual_gate_c --seed 20260220
python tools/run_gate_d.py --artifact-root artifacts/manual_gate_d --replay-seeds 20260220,20260221,20260222,20260223,20260224
```

Repo-local clean public replay import surface:

```bash
python -m pip install -e '.[proof]'
```

The `tools/` runners are repo-local scripts, not installed console entry
points. `LICENSE` is the legal source of truth. Read
`docs/LEGAL_BOUNDARIES.md` before turning any repo result into a wider legal or
commercial claim.

<p>
  <img src=".github/assets/readme/section-bars/proof-corpus.svg" alt="PROOF CORPUS" width="100%">
</p>

<a id="proof-corpus"></a>
<h2 align="center">Proof Corpus</h2>

<table width="100%" border="1" bordercolor="#111111" cellpadding="14" cellspacing="0">
  <thead>
    <tr>
      <th align="left" width="31%">Packet</th>
      <th align="left" width="21%">Class</th>
      <th align="left" width="48%">How to read it</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top"><code>proofs/manifests/CURRENT_AUTHORITY_PACKET.md</code></td>
      <td valign="top"><code>CURRENT</code></td>
      <td valign="top">The routing manifest for what is current, what is historical, and which packet owns each claim layer.</td>
    </tr>
    <tr>
      <td valign="top"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/</code></td>
      <td valign="top"><code>CURRENT</code></td>
      <td valign="top">Tracked summaries for the March 21 release-alignment technical pass.</td>
    </tr>
    <tr>
      <td valign="top"><a href="proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/README.md"><code>proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/</code></a></td>
      <td valign="top"><code>CURRENT</code></td>
      <td valign="top">Current bounded local extracellular breadth packet, including the counted IBL second-target <code>PASS</code>.</td>
    </tr>
    <tr>
      <td valign="top"><a href="CHANGELOG.md"><code>CHANGELOG.md</code></a> and <a href="runbooks/README.md"><code>runbooks/README.md</code></a></td>
      <td valign="top"><code>SUPPORTING</code></td>
      <td valign="top">Chronology, receipts, and operational history. Use them to understand how the current repo state was reached, not as current proof authority.</td>
    </tr>
  </tbody>
</table>

<p>
  <img src=".github/assets/readme/section-bars/open-risks.svg" alt="OPEN RISKS" width="100%">
</p>

<a id="open-risks"></a>
<h2 align="center">Open Risks</h2>

<table width="100%" border="1" bordercolor="#111111" cellpadding="14" cellspacing="0">
  <thead>
    <tr>
      <th align="left" width="28%">Surface</th>
      <th align="left" width="18%">Class</th>
      <th align="left" width="54%">Current truth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">Blind-clone authority pack</td>
      <td valign="top"><code>OPEN</code></td>
      <td valign="top">The repo does not yet prove a fresh blind-clone authority replay.</td>
    </tr>
    <tr>
      <td valign="top">Public release</td>
      <td valign="top"><code>OPEN</code></td>
      <td valign="top">No tagged/public release readiness is claimed from this repo state.</td>
    </tr>
    <tr>
      <td valign="top">IBL / Allen operator paths</td>
      <td valign="top"><code>OPERATOR_ONLY</code></td>
      <td valign="top">These remain outside the clean packaged release surface because the upstream dependency chains are not currently truthful for a clean install.</td>
    </tr>
    <tr>
      <td valign="top">Commercialization closure</td>
      <td valign="top"><code>OPEN</code></td>
      <td valign="top">Allen parity and commercialization-safe closure remain unresolved.</td>
    </tr>
    <tr>
      <td valign="top">Broader neural scope</td>
      <td valign="top"><code>PARKED_BY_SCOPE</code></td>
      <td valign="top">Broader human/intracranial or second-mode coverage is outside the current lane.</td>
    </tr>
    <tr>
      <td valign="top">Historical path residue</td>
      <td valign="top"><code>KNOWN_RESIDUE</code></td>
      <td valign="top">Some tracked runtime artifacts still contain machine-absolute paths inside captured traces. They are evidence lineage, not current filesystem instructions.</td>
    </tr>
  </tbody>
</table>

<p align="center">
  <img src=".github/assets/readme/zpe-masthead-option-3-3.gif" alt="ZPE-Neuro Lower Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/where-to-go.svg" alt="WHERE TO GO" width="100%">
</p>

<a id="go-next"></a>
<h2 align="center">Where To Go</h2>

<table width="100%" border="1" bordercolor="#111111" cellpadding="14" cellspacing="0">
  <thead>
    <tr>
      <th align="left">Need</th>
      <th align="left">Start here</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Shortest honest audit path</td>
      <td><code>AUDITOR_PLAYBOOK.md</code></td>
    </tr>
    <tr>
      <td>Current authority routing</td>
      <td><code>proofs/manifests/CURRENT_AUTHORITY_PACKET.md</code></td>
    </tr>
    <tr>
      <td>Architecture and package boundaries</td>
      <td><code>docs/ARCHITECTURE.md</code></td>
    </tr>
    <tr>
      <td>Limits and caveats</td>
      <td><code>PUBLIC_AUDIT_LIMITS.md</code>, <code>docs/LEGAL_BOUNDARIES.md</code></td>
    </tr>
    <tr>
      <td>Release gate</td>
      <td><code>RELEASING.md</code></td>
    </tr>
    <tr>
      <td>Support and contact routing</td>
      <td><code>docs/SUPPORT.md</code></td>
    </tr>
    <tr>
      <td>Canonical doc registry</td>
      <td><code>docs/README.md</code></td>
    </tr>
  </tbody>
</table>

## Ecosystem Cross-Links

| Surface | Link | Role |
|---|---|---|
| ZPE-IMC reference repo | `https://github.com/Zer0pa/ZPE-IMC` | Shared docs/readme reference line for structure and quality, not for inherited proof claims |
| Reproducing guide | `REPRODUCING.md` | Offline verify, public DANDI download, and benchmark replay commands for this repo |
| Open dataset surfaces | `docs/OPEN_DATASET_SURFACES.md` | Verified next-step public breadth targets without widening the current extracellular lane claim |
| KiloSort4 operator note | `docs/KILOSORT4.md` | Benchmark-only comparator guidance and current operator install posture |
