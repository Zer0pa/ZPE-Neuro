# RUNBOOK: Gate A (Runbook + Resource Lock + Schema Freeze)

## Objective
Create execution scaffolding before implementation: runbooks, locked artifact schema, dataset/comparator provenance plan, and gate preconditions.

## Preconditions
1. Startup prompt and PRD are read.
2. Concept anchor and quality rubric are read.
3. Lane boundary confirmed.

## Commands
1. `python3.11 tools/validate_runbook_contract.py`
2. `python3.11 tools/run_full_wave1.py --gate A --seed 20260220`

## Expected Outputs
- `runbooks/RUNBOOK_ZPE_NEURO_MASTER.md`
- `runbooks/RUNBOOK_GATE_A.md` through `runbooks/RUNBOOK_GATE_E.md`
- `runbooks/RUNBOOK_GATE_M1.md` through `runbooks/RUNBOOK_GATE_M4.md`
- `runbooks/RUNBOOK_GATE_E_APPENDIX_NETNEW.md`
- `runbooks/RUNBOOK_GATE_F_APPENDIX_GAP_CLOSURE.md`
- `runbooks/SCHEMA_FREEZE_ZPE_NEURO_WAVE1.md`
- `runbooks/RESOURCE_LOCK_ZPE_NEURO_WAVE1.md`
- Artifact root prepared with command log initialization.

## Fail Signatures
- `RUNBOOK_MISSING`
- `SCHEMA_FREEZE_MISSING`
- `RESOURCE_LOCK_INCOMPLETE`

## Rollback
- Patch runbooks only; no production code changes allowed in Gate A.

## Falsification Declaration
- No claim upgrades allowed in Gate A.
- Only verify readiness; claims remain `UNTESTED`.
