# SCHEMA FREEZE: ZPE Neuro Wave-1

## Version
- Schema version: `wave1-2026-02-20`
- Frozen on: `2026-02-21`

## Core Field Requirements

### Metric JSON Files (`neuro_*`, `determinism_replay_results.json`)
Required top-level fields:
1. `schema_version` (string)
2. `generated_at_utc` (ISO-8601 string)
3. `gate` (string)
4. `claim_id` (string or array for multi-claim files)
5. `status` (`PASS` | `FAIL` | `INCONCLUSIVE` | `UNTESTED`)
6. `thresholds` (object)
7. `measurements` (object)
8. `evidence` (array of relative artifact paths)
9. `seed_policy` (object with `global_seed` and `replay_seeds`)
10. `notes` (array of strings)

### `before_after_metrics.json`
1. `schema_version`
2. `baseline`
3. `after`
4. `delta`
5. `metric_units`
6. `scope_notes`

### `quality_gate_scorecard.json`
1. `schema_version`
2. `non_negotiable_gate` (PASS/FAIL map)
3. `dimension_scores` (10 dimensions, 0-5)
4. `total_score`
5. `minimum_passing_standard`
6. `lane_status` (`GO` | `NO-GO` | `PARTIAL`)
7. `evidence_paths`

### `integration_readiness_contract.json`
1. `schema_version`
2. `interfaces` (NWB, SpikeInterface)
3. `compatibility_matrix`
4. `known_limitations`
5. `versioning`
6. `evidence_paths`

### `concept_resource_traceability.json`
1. `schema_version`
2. `appendix_b_items` (1-8)
3. Per item: `source_reference`, `planned_usage`, `execution_status`, `substitution`, `comparability_impact`, `evidence_artifact`

### Markdown/TXT outputs
- Must include explicit section with evidence file paths.
- Any uncertainty must be marked as `UNTESTED` or `INCONCLUSIVE`.

### Appendix E Max-Wave JSON files

#### `max_resource_lock.json`
1. `schema_version`
2. `generated_at_utc`
3. `resource_catalog`
4. `env_bootstrap`
5. `seed_policy`

#### `max_claim_resource_map.json`
1. `schema_version`
2. `generated_at_utc`
3. `claim_to_resources`
4. `closure_state`
5. `evidence_paths`

#### `impracticality_decisions.json`
1. `schema_version`
2. `generated_at_utc`
3. `decisions` (array)
4. Per decision: `resource`, `imp_code`, `command_evidence`, `error_signature`, `fallback`, `claim_impact`
5. `allowed_codes`

#### `spike_timing_error_distribution.json`
1. `schema_version`
2. `generated_at_utc`
3. `dataset`
4. `measurements`
5. `distribution_ms`
6. `evidence_paths`

#### `net_new_gap_closure_matrix.json`
1. `schema_version`
2. `generated_at_utc`
3. `gates` (`M1`,`M2`,`M3`,`M4`,`E-G1..E-G5`)
4. `status`
5. `blocking_items`
6. `evidence_paths`

#### `runpod_readiness_manifest.json` (conditional)
1. `schema_version`
2. `generated_at_utc`
3. `trigger`
4. `deferred_paths`
5. `environment_spec`
6. `execution_plan_artifact`

#### `runpod_requirements_lock.txt` (conditional)
1. newline-delimited pinned requirements (`package==version`)
2. generated from in-lane runtime used for retry/escalation

#### `runpod_expected_artifacts.json` (conditional)
1. `schema_version`
2. `generated_at_utc`
3. `expected_outputs`
4. `required_for_gate`

## Change Control
- No schema field removal after Gate A.
- Additive fields allowed only if backward-compatible.
