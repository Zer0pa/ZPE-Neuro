<p>
  <img src="../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src="../.github/assets/readme/section-bars/what-this-is.svg" alt="WHAT THIS IS" width="100%">
</p>

This document is the canonical architecture index for the current ZPE-Neuro
repo surface. It defines where package truth, proof truth, and release truth
live.

Canonical anchors:
- Repository: private GitHub repo `https://github.com/Zer0pa/ZPE-Neuro` for authorized readers
- Contact: `architects@zer0pa.ai`
- Current authority routing: `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- Current technical proof packet: `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/`
- Current lane evidence packet: `proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/`

<p>
  <img src="../.github/assets/readme/section-bars/repo-shape.svg" alt="REPO SHAPE" width="100%">
</p>

| Surface | Role | Canonical path |
|---|---|---|
| Package metadata | install and dependency truth | `pyproject.toml` |
| Package code | import surface and gate logic | `src/zpe_neuro/` |
| Tests | shipped regression slice | `tests/` |
| Repo-local runners | gate, replay, and validation scripts | `tools/` |
| Docs | front door, release, governance, support | `README.md`, `docs/` |
| Proof corpus | current authority packets and proof manifests | `proofs/` |

<p>
  <img src="../.github/assets/readme/section-bars/packaged-surface.svg" alt="PACKAGED SURFACE" width="100%">
</p>

| Install surface | Current truth | Notes |
|---|---|---|
| `pip install -e .` | clean packaged baseline | core package only |
| `pip install -e '.[dev]'` | shipped test slice | unit tests only |
| `pip install -e '.[gate,dev]'` | shipped synthetic gate baseline | current strongest clean packaged replay path |
| `pip install -e '.[public]'` | clean public replay dependency surface | DANDI/AJILE stack only |
| `pip install -e '.[proof]'` | alias of the current clean public replay stack | import/replay helper surface |

The `tools/` runners are repo-local scripts. No installed console entry point
is claimed.

<p>
  <img src="../.github/assets/readme/section-bars/evidence.svg" alt="AUTHORITY PACKETS" width="100%">
</p>

| Packet | Class | What it owns |
|---|---|---|
| `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` | current routing anchor | current versus historical packet ownership |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/` | current technical authority | clean blind-clone replay, tests, Gate C, Gate D, and DANDI `000034` replay receipts |
| `proofs/selected_artifacts/2026-04-24_zpe_neuro_dandi000003_breadth/` | current lane evidence authority | bounded extracellular breadth verdict with the first DANDI `000003` attempt |
| `CHANGELOG.md` | chronology only | how the current surface was reached |

<p>
  <img src="../.github/assets/readme/section-bars/optional-dependency-groups.svg" alt="OPERATOR-ONLY SURFACES" width="100%">
</p>

| Surface | Why it is operator-only today |
|---|---|
| IBL chunked-waveform tooling | depends on manual setup around `ONE-api`, `ibl-neuropixel`, and the upstream `llvmlite` / `numba` toolchain |
| Allen parity | depends on `allensdk`, which conflicts with `numpy>=1.26` |
| Ignored local `artifacts/` tree | useful for reruns, but not a shipped GitHub proof anchor until promoted into `proofs/selected_artifacts/` |

<p>
  <img src="../.github/assets/readme/section-bars/open-risks-non-blocking.svg" alt="KNOWN DRIFT AND LAG" width="100%">
</p>

Known lagging defaults:
- some tracked runtime artifacts still contain machine-absolute paths captured
  during execution
- operator-only IBL and Allen paths remain outside the declared packaged
  install surface

The docs resolve this by keeping the live proof surface small and routing
chronology through `CHANGELOG.md` instead of through shipped
bridge packets.
