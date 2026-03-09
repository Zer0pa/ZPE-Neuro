# Architecture

## Repo Shape

This repo uses a standard Python package layout:

```text
pyproject.toml
src/zpe_neuro/
tests/
tools/
runbooks/
docs/
proofs/
```

## Code Surfaces

- `src/zpe_neuro/wave1.py`
  - core wave1 generation, encoding, gate A-E logic, and proof writing
- `src/zpe_neuro/max_wave.py`
  - extended gate logic and comparator/external-corpus orchestration
- `src/zpe_neuro/__init__.py`
  - package export surface

## Tooling Surfaces

- `tools/run_gate_*.py`
  - lane gate entry points
- `tools/run_full_wave1.py`
  - aggregated execution entry point
- `tools/validate_runbook_contract.py`
  - runbook completeness check
- `tools/validate_artifact_schema.py`
  - artifact file/schema check

## Artifact Strategy

- runtime-generated outputs belong under the ignored local `artifacts/` directory
- shipped evidence belongs under `proofs/selected_artifacts/`
- proof-selection rationale lives under `proofs/manifests/`

This split keeps local reruns out of git while preserving the adjudicated evidence needed for inspection.

## Public vs Operator Boundary

Kept in repo:

- code
- tests
- tools
- runbooks
- curated proof subset

Kept outside repo:

- outer orchestrator reports
- agent startup/runbook records
- local virtualenvs and secrets
- full historical artifact trees

## Dependency Boundary

Core install:

- `numpy`
- `scipy`

Optional proof install:

- `pynwb`
- `spikeinterface`
- `allensdk`
- `wfdb`

Those optional dependencies are declared for later replay work, not as proof that the replay path is already clean on a fresh clone.
