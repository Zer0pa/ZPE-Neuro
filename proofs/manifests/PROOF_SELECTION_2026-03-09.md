# Proof Selection 2026-03-09

Historical note:
- this file is the original March 9 selection record for the initial curated
  proof subset
- it is not the current authority-routing manifest
- current routing now lives in `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- the original live target selected by this note was retired from the shipped
  proof surface on `2026-03-22`

Source bundle:

retired local handoff bundle from the February 21 adjudicated closure push

Repo target:

retired February 21 proof packet (no longer part of the live shipped proof surface)

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
