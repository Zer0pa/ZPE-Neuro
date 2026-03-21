---
phase: 02-ibl-waveform-slice-execution
plan: 02
depth: full
one-liner: "The packaged IBL KS014 public AP chunk executed locally into a real waveform artifact; waveform existence passed while downstream SpikeInterface failed with zero detected peaks."
subsystem: [analysis, validation, computation]
tags: [ibl, spikeglx, spikeinterface, nwb, public-corpus]
requires: [02-01-ibl-local-path]
provides:
  - a repo-local `public_corpus_ibl_waveform_eval.json` artifact for the IBL second target
  - a focused unit test for chunk metadata rebasing and invalid chunk rejection
  - a local waveform execution result that preserves existence evidence separately from downstream evaluation
affects: [03-breadth-adjudication-and-public-rerun, 04-lane-1-wedge-decision, lane-1-authority]
methods:
  added: [single-chunk public IBL waveform execution, explicit waveform-versus-evaluation status split, focused chunk-rebasing test coverage]
  patterns: [reject metadata-only success proxies, reject waveform-equals-pass narratives]
key-files:
  created:
    - .gpd/phases/02-ibl-waveform-slice-execution/02-02-SUMMARY.md
    - proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json
  modified:
    - pyproject.toml
    - src/zpe_neuro/ibl_public.py
    - tools/run_ibl_public_waveform_eval.py
    - tests/test_ibl_public.py
key-decisions:
  - "Treat real waveform execution as the Phase 2 acceptance gate even when downstream insertion still fails."
  - "Preserve `status = PASS` for waveform existence while surfacing `evaluation_status = FAIL` and explicit failure reasons."
  - "Keep the dependency surface minimal with `ibl-neuropixel` plus `mtscomp` rather than the heavier `ibllib` stack."
patterns-established:
  - "Second-target artifacts must report waveform existence, resource notes, and downstream evaluation separately."
  - "Phase 2 closes on executed waveform evidence, not on a narratable insertion win."
conventions:
  - "Signal amplitudes remain tracked in microvolts after source-unit conversion."
  - "Chunk-local sample windows use zero-based half-open ranges [start, start + sample_limit)."
  - "The second-target artifact distinguishes `status` from `evaluation_status`."
plan_contract_ref: ".gpd/phases/02-ibl-waveform-slice-execution/02-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-second-target:
      status: passed
      summary: "A real public IBL waveform slice was executed locally, producing a durable second-target artifact without relying on the metadata-only proxy."
      linked_ids: [deliv-second-target, test-second-target, test-chunk-trimming, ref-ibl-probe, ref-way-forward]
      evidence:
        - verifier: codex
          method: targeted local test plus live public IBL waveform eval
          confidence: high
          claim_id: claim-second-target
          deliverable_id: deliv-second-target
          acceptance_test_id: test-second-target
          reference_id: ref-ibl-probe
          evidence_path: proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json
  deliverables:
    deliv-second-target:
      status: passed
      path: proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json
      summary: "The artifact records a real IBL waveform slice, materialized byte counts, target keys, NWB roundtrip PASS, and downstream SpikeInterface FAIL."
      linked_ids: [claim-second-target, test-second-target]
  acceptance_tests:
    test-second-target:
      status: passed
      summary: "The local command produced a real second-target waveform artifact with `waveform_slice_executed = true` and no metadata-only shortcut."
      linked_ids: [claim-second-target, deliv-second-target, ref-ibl-probe, ref-way-forward]
    test-chunk-trimming:
      status: passed
      summary: "The focused unit test confirmed that the chunk metadata helper rebases offsets and bounds correctly and rejects invalid chunk indices."
      linked_ids: [claim-second-target, deliv-second-target]
  references:
    ref-ibl-probe:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Compared the executed waveform artifact against the earlier metadata-only IBL probe and verified that the existence gap is now closed."
    ref-way-forward:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Used the Way Forward packet to keep the closeout focused on real execution rather than a pass narrative."
  forbidden_proxies:
    fp-ibl-metadata:
      status: rejected
      notes: "The artifact includes a real waveform slice, local cached files, and byte-range details; metadata-only access was not counted."
    fp-waveform-equals-pass:
      status: rejected
      notes: "The artifact kept `evaluation_status = FAIL` with `SPIKEINTERFACE_FAIL` even though waveform existence passed."
  uncertainty_markers:
    weakest_anchors:
      - "Whether this first IBL chunk is representative enough for downstream sorter conclusions."
    unvalidated_assumptions:
      - "A zero-peak SpikeInterface failure on this slice may reflect chunk choice rather than a hard family-boundary conclusion."
    competing_explanations:
      - "The IBL slice may be genuinely too weak for the current insertion path, or the 6000 x 8 bounded view may be too narrow for downstream peak detection."
    disconfirming_observations:
      - "If rerunning the same command stops producing a real waveform artifact, the second-target execution claim would regress."
comparison_verdicts:
  - subject_id: claim-second-target
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ibl-probe
    comparison_kind: baseline
    metric: "waveform execution versus metadata-only IBL baseline"
    threshold: "must produce a real waveform artifact locally"
    verdict: pass
    recommended_action: "Carry the executed IBL target into Phase 3 breadth adjudication without pretending downstream insertion has passed."
    notes: "The new artifact records `waveform_slice_executed = true`, `event_count = 8`, and `disk_bytes_materialized = 9036119`."
duration: 8min
completed: 2026-03-20
---

# Phase 02 Plan 02: IBL Waveform Execution Summary

**The packaged IBL KS014 public AP chunk executed locally into a real waveform artifact; waveform existence passed while downstream SpikeInterface failed with zero detected peaks.**

## Performance

- **Duration:** 8 min
- **Started:** 2026-03-20T18:25:59Z
- **Completed:** 2026-03-20T18:33:37Z
- **Tasks:** 3
- **Files modified:** 4

## Key Results

- Ran `tools/run_ibl_public_waveform_eval.py` locally against the public KS014/probe00 AP chunk and produced `public_corpus_ibl_waveform_eval.json`.
- Confirmed `waveform_slice_executed = true` and `status = PASS` for the existence milestone while preserving `evaluation_status = FAIL`.
- The executed slice was `6000 x 8` at `30000 Hz` with `8` codec events, `compression_ratio = 718.43`, and `rmse_uv = 13.37`.
- The NWB roundtrip passed bit-consistency, while SpikeInterface failed after detecting zero peaks and handing an empty array to `TruncatedSVD`.
- Total bounded public materialization for the execution path was `9,036,119` bytes, which stayed within the local disk discipline.

## Task Commits

No atomic commit was created during this run. The work remains uncommitted in the existing dirty lane repo.

## Files Created/Modified

- `.gpd/phases/02-ibl-waveform-slice-execution/02-02-SUMMARY.md` - contract-backed closeout for the live IBL execution run
- `pyproject.toml` - proof dependency entry for `ibl-neuropixel`
- `src/zpe_neuro/ibl_public.py` - packaged single-chunk IBL waveform execution path
- `tools/run_ibl_public_waveform_eval.py` - executable CLI for the Phase 2 second-target run
- `tests/test_ibl_public.py` - focused chunk metadata coverage
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json` - second-target execution artifact

## Phase Readiness

Phase 2 is complete. Phase 3 can now adjudicate breadth using three executed public targets: DANDI as the preserved positive anchor, AJILE as an informative-window failure, and IBL as a real waveform execution that still fails in downstream SpikeInterface analysis.

## Contract Coverage

- Claim IDs advanced: `claim-second-target -> passed`
- Deliverable IDs produced: `deliv-second-target -> passed`
- Acceptance test IDs run: `test-second-target -> passed`, `test-chunk-trimming -> passed`
- Reference IDs surfaced: `ref-ibl-probe -> read, compare`; `ref-way-forward -> read, use`
- Forbidden proxies rejected or violated: `fp-ibl-metadata -> rejected`; `fp-waveform-equals-pass -> rejected`
- Decisive comparison verdicts: `claim-second-target vs ref-ibl-probe -> pass`

## Validations Completed

- Ran `env PYTHONPATH=src '/Users/Zer0pa/ZPE/ZPE Neuro/.venv/bin/python' -m unittest tests.test_ibl_public tests.test_public_corpus_window_selection` and all four tests passed.
- Ran `env PYTHONPATH=src ZPE_NEURO_ARTIFACT_ROOT=proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe '/Users/Zer0pa/ZPE/ZPE Neuro/.venv/bin/python' tools/run_ibl_public_waveform_eval.py --sample-limit 6000 --channel-limit 8 --chunk-index 0` and produced the second-target artifact with exit code `0`.
- Inspected the artifact to confirm that waveform existence, resource notes, and downstream evaluation stayed separated.

## Decisions & Deviations

Kept the top-level artifact `status` tied to waveform existence rather than downstream insertion success. This is a deliberate deviation from a simpler single-verdict payload because Phase 2 closes on existence while Phase 3 still needs the downstream interpretation.

## Open Questions

- Does the zero-peak SpikeInterface failure reflect a representative IBL family-boundary signal, or just a too-thin `6000 x 8` slice for the sorter path?
- How should the executed-but-failing IBL target be counted alongside DANDI and AJILE in the Phase 3 breadth memo?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Executed waveform samples | `N_exec` | `6000` | bounded intentionally for local existence | second-target artifact | `sample_limit = 6000` |
| Executed channels | `C_exec` | `8` | bounded intentionally for local existence | second-target artifact | `channel_limit = 8` |
| Codec event count | `E_ibl` | `8` | may change under a different chunk or wider slice | second-target artifact | chunk `0`, current bounded path |
| Materialized bytes | `B_exec` | `9036119` | excludes later Phase 3 rerun surfaces | second-target artifact | current bounded execution path |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Single-chunk `6000 x 8` execution slice | Phase 2 only needs an honest waveform-existence proof | Downstream sorter conclusions may be slice-sensitive | Phase 3 needs broader evidence about representativeness or family boundary |

## Issues Encountered

- SpikeInterface failed because peak detection returned zero peaks, which left the internal sorter with an empty waveform matrix for `TruncatedSVD`.
- SpikeInterface also warned that the temporary extractor was not serializable to file, though the serialized recording and log artifacts were still written.
