---
phase: 02-ibl-waveform-slice-execution
plan: 01
depth: full
one-liner: "A public unsigned S3 raw AP path for IBL KS014/probe00 was reduced to a one-chunk local workflow that fits on the M1 and reaches real waveform bytes."
subsystem: [analysis, validation, computation]
tags: [ibl, spikeglx, s3, public-corpus, feasibility]
requires: [01-public-corpus-window-policy]
provides:
  - a concrete public IBL raw AP object trio for KS014 2019-12-03 probe00
  - measured chunk bounds and byte counts for the smallest honest local waveform path
  - a code-level path that preserves waveform existence separately from downstream evaluation
affects: [02-ibl-waveform-slice-execution, 03-breadth-adjudication-and-public-rerun, lane-1-authority]
methods:
  added: [unsigned public S3 raw-byte discovery, single-chunk metadata rebasing, bounded local AP chunk materialization]
  patterns: [reject metadata-only success proxies, keep waveform existence distinct from downstream insertion quality]
key-files:
  created:
    - .gpd/phases/02-ibl-waveform-slice-execution/02-01-SUMMARY.md
    - .gpd/phases/02-ibl-waveform-slice-execution/02-CONTEXT.md
    - .gpd/phases/02-ibl-waveform-slice-execution/02-RESEARCH.md
    - .gpd/phases/02-ibl-waveform-slice-execution/02-01-PLAN.md
  modified:
    - src/zpe_neuro/ibl_public.py
key-decisions:
  - "Prefer the public unsigned S3 bucket over the fragile authenticated ONE path once raw AP bytes are confirmed there."
  - "Treat one compressed AP chunk plus the `.meta` and `.ch` files as the smallest honest local waveform path."
  - "Preserve a separate downstream evaluation status so the second-target milestone does not pretend to be a full insertion pass."
patterns-established:
  - "IBL public feasibility must cite exact object keys, byte ranges, and materialized bytes."
  - "A bounded chunk path is acceptable for Phase 2 only if it reaches real waveform samples locally."
conventions:
  - "Signal amplitudes remain tracked in microvolts after source-unit conversion."
  - "Chunk-local sample windows use zero-based half-open ranges [start, start + sample_limit)."
  - "Trimmed `.ch` metadata is rebased so the chopped local `.cbin` starts at byte 0 and sample 0."
plan_contract_ref: ".gpd/phases/02-ibl-waveform-slice-execution/02-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-ibl-local-path:
      status: passed
      summary: "A concrete KS014/probe00 public AP target, chunk index, and bounded byte range were identified and encoded for local execution."
      linked_ids: [deliv-ibl-path-note, test-ibl-local-path, ref-ibl-probe, ref-way-forward]
      evidence:
        - verifier: codex
          method: public bucket discovery plus packaged artifact inspection
          confidence: high
          claim_id: claim-ibl-local-path
          deliverable_id: deliv-ibl-path-note
          acceptance_test_id: test-ibl-local-path
          reference_id: ref-ibl-probe
          evidence_path: proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json
  deliverables:
    deliv-ibl-path-note:
      status: passed
      path: .gpd/phases/02-ibl-waveform-slice-execution/02-01-SUMMARY.md
      summary: "The chosen IBL target, chunk bounds, and local byte budget are explicit and audit-ready."
      linked_ids: [claim-ibl-local-path, test-ibl-local-path]
  acceptance_tests:
    test-ibl-local-path:
      status: passed
      summary: "The Phase 2 path now points to a real public raw AP object trio with explicit chunk bounds and no metadata-only shortcut."
      linked_ids: [claim-ibl-local-path, deliv-ibl-path-note, ref-ibl-probe, ref-way-forward]
  references:
    ref-ibl-probe:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Compared the new raw-byte path against the earlier metadata-only IBL probe and confirmed the phase moved beyond metadata."
    ref-way-forward:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Used the Way Forward packet to keep the phase focused on real waveform execution or an honest measured block."
  forbidden_proxies:
    fp-ibl-metadata:
      status: rejected
      notes: "The chosen path now cites real `.meta`, `.ch`, and `.cbin` objects plus a byte-range fetch; metadata visibility alone was not treated as success."
  uncertainty_markers:
    weakest_anchors:
      - "Whether the bounded chunk path would survive full package integration without widening scope."
    unvalidated_assumptions:
      - "Chunk 0 is representative enough for the first honest IBL existence attempt."
    competing_explanations:
      - "A richer IBL chunk may later change downstream peak detection even though the existence milestone is already met."
    disconfirming_observations:
      - "If future reruns require whole-file downloads or auth-only flows, this feasibility claim would need revision."
comparison_verdicts:
  - subject_id: claim-ibl-local-path
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ibl-probe
    comparison_kind: baseline
    metric: "waveform-path existence versus metadata-only baseline"
    threshold: "must reach real raw-byte objects with bounded local materialization"
    verdict: pass
    recommended_action: "Proceed to execute the packaged waveform eval harness locally."
    notes: "The KS014 2019-12-03 probe00 AP trio and chunk-0 byte range replaced the earlier metadata-only IBL state."
duration: 25min
completed: 2026-03-20
---

# Phase 02 Plan 01: IBL Local Path Summary

**A public unsigned S3 raw AP path for IBL KS014/probe00 was reduced to a one-chunk local workflow that fits on the M1 and reaches real waveform bytes.**

## Performance

- **Duration:** 25 min
- **Started:** 2026-03-20T18:00:49Z
- **Completed:** 2026-03-20T18:25:59Z
- **Tasks:** 3
- **Files modified:** 4

## Key Results

- Identified one concrete public target in `ibl-brain-wide-map-public`: `KS014 / 2019-12-03 / 001 / probe00` raw AP data.
- Fixed the smallest honest local path to three objects: one `.meta`, one `.ch`, and one `.cbin` fetched by byte range.
- Measured the first chunk as `30000` samples with a compressed byte span of `8,928,919` bytes, which kept the local existence attempt inside the M1 disk budget.
- Encoded the single-chunk rebasing path in `src/zpe_neuro/ibl_public.py` so a later packaged run could open the chopped local files with `spikeglx.Reader`.

## Task Commits

No atomic commit was created during this run. The work remains uncommitted in the existing dirty lane repo.

## Files Created/Modified

- `.gpd/phases/02-ibl-waveform-slice-execution/02-CONTEXT.md` - Phase 2 constraints and decision points
- `.gpd/phases/02-ibl-waveform-slice-execution/02-RESEARCH.md` - feasibility research for the bounded public IBL path
- `.gpd/phases/02-ibl-waveform-slice-execution/02-01-PLAN.md` - contract-backed path-identification plan
- `.gpd/phases/02-ibl-waveform-slice-execution/02-01-SUMMARY.md` - closeout for the path-identification plan
- `src/zpe_neuro/ibl_public.py` - public IBL target definition and single-chunk materialization helpers

## Next Plan Readiness

Plan `02-02` can now execute the real waveform eval harness locally. The phase no longer needs a RunPod-style escalation just to prove second-target waveform existence.

## Contract Coverage

- Claim IDs advanced: `claim-ibl-local-path -> passed`
- Deliverable IDs produced: `deliv-ibl-path-note -> passed`
- Acceptance test IDs run: `test-ibl-local-path -> passed`
- Reference IDs surfaced: `ref-ibl-probe -> read, compare`; `ref-way-forward -> read, use`
- Forbidden proxies rejected or violated: `fp-ibl-metadata -> rejected`
- Decisive comparison verdicts: `claim-ibl-local-path vs ref-ibl-probe -> pass`

## Validations Completed

- Confirmed the public S3 bucket exposed real raw AP objects for the chosen KS014 probe.
- Measured chunk bounds and byte counts from the `.ch` sidecar instead of inferring them from metadata only.
- Verified that the chosen path stayed within a bounded one-chunk local materialization model.

## Decisions & Deviations

Preferred the unsigned public S3 route over the authenticated ONE path once it was clear the latter was adding fragility without supplying a better raw-byte path.

## Open Questions

- Does the packaged single-chunk path still produce a real waveform artifact once it runs through the existing insertion harness?
- Is chunk `0` enough for the decisive existence proof, or will a later breadth analysis need a different IBL window for representativeness?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Chunk sample count | `N_chunk` | `30000` | specific to chunk `0` of the chosen target | `.ch` sidecar | chosen KS014/probe00 AP file |
| Compressed chunk bytes | `B_chunk` | `8928919` | may vary across chunks | range-fetched `.cbin` span | chosen KS014/probe00 AP file |
| Total materialized bytes for the bounded path | `B_local` | `9036119` | excludes later harness byproducts | packaged artifact inspection | one-chunk local existence run |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| One-chunk feasibility model | Phase 2 only needs to prove or disprove a real local waveform path | Later breadth work may need a different or richer chunk | The run needs multi-chunk stitching or whole-file staging |

## Issues Encountered

- The authenticated ONE path remained flaky enough to reject as the primary route for this phase.
- The phase still needed a packaged execution run to prove the code path was not only a one-off prototype.
