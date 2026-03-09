# Proof Selection 2026-03-09

Source bundle:

`artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated`

Repo target:

`proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated`

## Selection Rule

Copied into the repo:

- files listed in `handoff_manifest.json`
- limited to machine-readable and text artifacts with extensions `.json`, `.md`, `.txt`, `.c`

Left outside the repo:

- heavyweight binary/runtime outputs
- raw session trees
- sorter scratch folders
- `.nwb` and other large binary artifacts

## Reason

This keeps the private repo inspectable while preserving the decision-critical proof trail.

## Known Historical Residue

Some copied proof files still contain machine-absolute path strings from the original workspace. Those strings are preserved as historical evidence only.
