# ZPE-Neuro

Private staged repo for the ZPE Neuro Wave-1 package and curated proof surface.

This repo is the clean inner boundary for the Neuro sector as of 2026-03-09. It was extracted from a larger outer workspace so that code, docs, and selected proofs can be staged to a private GitHub repo without dragging operator residue and 2 GB of raw artifacts into git.

## What This Repo Is

- A standalone Python package surface for `zpe_neuro`
- A curated proof subset from the adjudicated `2026-02-21_zpe_neuro_wave1_closure_push_adjudicated` bundle
- A private staging repo for later Phase 4.5 and Phase 5 work

## What This Repo Is Not

- Not a public release
- Not a blind-clone verified snapshot yet
- Not a claim that all contradictions are resolved
- Not a commercialization-clear repo

## Current Reality

- Local unit tests in the source workspace passed before extraction
- Runbook-contract and artifact-schema validators passed before extraction
- The package surface is now explicitly dependency-declared for `numpy` and `scipy`
- Full proof reruns, comparator reruns, and cold-clone verification are deferred

## Active Contradictions Kept Explicit

1. `NEU-C007` is still mixed evidence. The shipped `neuro_spikeinterface_e2e.json` records `sorter_probe_status=INCONCLUSIVE` and a sorter error even though higher-level summaries mark the claim `PASS`.
2. Gate D still coexists with `DT-NEU-5 - FAIL` in the shipped falsification record.
3. Commercialization is not cleanly closed. The shipped risk material still records Allen external parity as `ADJUDICATED_FAIL` / `RISK`.
4. Some preserved proof artifacts still contain historical machine-absolute paths from the original workspace. Those artifacts are retained as historical evidence, not as current path truth.

## Quickstart

Core package path:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

Optional proof-stack dependencies for heavier replay work:

```bash
python -m pip install -e '.[proof]'
```

This private staging repo does not claim that `.[proof]` replay is already validated on a clean clone. That belongs to Phase 5.

## Repo Map

- `src/zpe_neuro/`: package code
- `tests/`: lightweight unit tests
- `tools/`: gate runners and validators
- `runbooks/`: sector runbooks carried into the repo boundary
- `docs/`: front-door docs, architecture, and legal boundary notes
- `proofs/`: curated proof subset and selection notes

## Proof Anchors

- `proofs/README.md`
- `proofs/manifests/PROOF_SELECTION_2026-03-09.md`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/claim_status_delta.md`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/quality_gate_scorecard.json`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/handoff_manifest.json`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/falsification_results.md`

## Public vs Operator Boundary

This repo intentionally excludes:

- outer-workspace orchestrator reports
- agent startup material
- local `.env` and `.venv`
- raw historical bundle trees
- scratch outputs and quarantine residue

If you need the outer workspace lineage, use the outer reports rather than trying to reconstruct it from the repo.

## Where To Go Next

- Audit path: `AUDITOR_PLAYBOOK.md`
- Limits and honesty constraints: `PUBLIC_AUDIT_LIMITS.md`
- Support routing: `SUPPORT.md`
- Architecture and package boundaries: `docs/ARCHITECTURE.md`, `docs/LEGAL_BOUNDARIES.md`
