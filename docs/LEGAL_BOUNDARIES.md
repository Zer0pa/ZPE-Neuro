# Legal Boundaries

This note is a repo-surface summary only. `LICENSE` at the repository root is the legal source of truth.

## Package Surface

- `pyproject.toml` governs the Python package boundary for this repo
- `src/zpe_neuro/` is the package code
- `tests/`, `tools/`, `runbooks/`, and `proofs/` are shipped as repository materials, not separately published packages

## Comparator And Corpus Boundaries

- MountainSort5 comparator: treated as allowed comparator evidence with the current Apache-2.0 boundary reflected in the carried risk material
- Kilosort4 comparator: treated as benchmark-only and not as commercialization-clear evidence
- Allen external corpus parity: still open risk; shipped artifacts record `ADJUDICATED_FAIL` / `RISK`
- SpikeInterface and NWB proof paths exist as evidence surfaces, but not all optional proof dependencies are part of the minimal install path

## Historical Proof Artifacts

Some preserved proof files contain historical machine-specific paths. Those strings are retained because they are part of the original evidence record. They are not current filesystem instructions for this repo.

## Release Posture

This is a private staged repo. No public-release legal conclusion is implied by the existence of this repo boundary.
