---
phase: 01-public-corpus-window-policy
plan: 01
depth: full
one-liner: "Deterministic candidate-window scanning preserved the DANDI anchor and showed AJILE remains an informative-window failure rather than a fixed-window artifact."
subsystem: [analysis, validation, computation]
tags: [public-corpus, dandi, ajile12, spikeinterface, window-selection]
requires: []
provides:
  - deterministic candidate-window selection artifacts for public-corpus targets
  - DANDI rerun under the scan policy with the Tier 1 PASS preserved
  - AJILE rerun on an informative window with a persistent SpikeInterface failure
affects: [02-ibl-waveform-slice-execution, 03-breadth-adjudication-and-public-rerun, lane-1-authority]
methods:
  added: [deterministic candidate-window scanning, per-target selection artifacts, eventfulness-first ranking]
  patterns: [preserve anchor-vs-breadth separation, reject quiet-window compression proxies]
key-files:
  created:
    - .gpd/phases/01-public-corpus-window-policy/01-01-SUMMARY.md
    - proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_window_selection_summary.json
    - proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_summary.json
  modified:
    - src/zpe_neuro/public_corpus.py
    - tools/run_public_corpus_eval.py
    - src/zpe_neuro/__init__.py
    - tests/test_public_corpus_window_selection.py
key-decisions:
  - "Keep the public selection policy deterministic, cheap, and auditable with evenly spaced candidate starts."
  - "Treat a preserved DANDI PASS as anchor preservation only, not as breadth closure."
  - "Carry AJILE forward as a family-boundary question because the informative-window rerun still fails."
patterns-established:
  - "Selection artifacts must record first-window rank, selected start sample, and quiet-window visibility per target."
  - "Eventfulness and active-channel engagement outrank compression-only wins."
conventions:
  - "Signal amplitudes remain tracked in microvolts after source-unit conversion."
  - "Windows use zero-based half-open sample ranges [start, start + sample_limit)."
  - "Candidate windows are evaluated in deterministic ascending start order."
plan_contract_ref: ".gpd/phases/01-public-corpus-window-policy/01-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-window-policy:
      status: passed
      summary: "The harness now scans nine deterministic candidate windows, records ranking artifacts, and evaluates the selected slice instead of the implicit first window."
      linked_ids: [deliv-window-selection, deliv-rerun-summary, test-window-selection, test-dandi-anchor, ref-dandi, ref-ajile, ref-way-forward]
      evidence:
        - verifier: codex
          method: deterministic rerun and artifact inspection
          confidence: high
          claim_id: claim-window-policy
          deliverable_id: deliv-window-selection
          acceptance_test_id: test-window-selection
          reference_id: ref-ajile
          evidence_path: proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_window_selection_summary.json
        - verifier: codex
          method: anchor stability rerun
          confidence: high
          claim_id: claim-window-policy
          deliverable_id: deliv-rerun-summary
          acceptance_test_id: test-dandi-anchor
          reference_id: ref-dandi
          evidence_path: proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_summary.json
  deliverables:
    deliv-window-selection:
      status: passed
      path: proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_window_selection_summary.json
      summary: "Aggregate and per-target selection artifacts exist with candidate starts, first-window rank, and selected windows for DANDI and AJILE."
      linked_ids: [claim-window-policy, test-window-selection]
    deliv-rerun-summary:
      status: passed
      path: proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_summary.json
      summary: "The rerun summary records DANDI PASS, AJILE FAIL, IBL probe FAIL, and keeps breadth as FAIL under the scan policy."
      linked_ids: [claim-window-policy, test-dandi-anchor]
  acceptance_tests:
    test-window-selection:
      status: passed
      summary: "Deterministic scan-mode rerun produced stable candidate-window artifacts and the harness no longer relied on the first window implicitly."
      linked_ids: [claim-window-policy, deliv-window-selection, ref-dandi, ref-ajile, ref-way-forward]
    test-dandi-anchor:
      status: passed
      summary: "The DANDI Tier 1 target remained PASS under the new scan policy, so the anchor did not regress."
      linked_ids: [claim-window-policy, deliv-rerun-summary, ref-dandi]
  references:
    ref-dandi:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Compared the scan-policy DANDI rerun against the March 20 PASS anchor and verified verdict stability."
    ref-ajile:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Compared the fixed-window AJILE baseline against the selected-window rerun to confirm the new window was informative rather than quiet."
    ref-way-forward:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Used the Way Forward packet to keep quiet-window rejection and representative-slice selection explicit."
  forbidden_proxies:
    fp-quiet-compression:
      status: rejected
      notes: "AJILE was not upgraded on compression alone; the selected window still had to show engagement, and the final verdict stayed FAIL because insertion still failed."
    fp-dandi-breadth:
      status: rejected
      notes: "The preserved DANDI PASS was recorded only as anchor preservation; breadth remained FAIL in the rerun summary."
  uncertainty_markers:
    weakest_anchors:
      - "Whether a nine-window scan is sufficient for every future public target."
    unvalidated_assumptions:
      - "The current ranking metric will remain robust against noise-heavy windows outside the two tested targets."
    competing_explanations:
      - "AJILE may be genuinely out-of-family for the first-lane codec, or the remaining failure may still sit in the sorter/insertion path rather than the representation family boundary."
    disconfirming_observations:
      - "AJILE still failed after the selected informative window, now with event_count=3 and all_candidates_quiet=false."
comparison_verdicts:
  - subject_id: claim-window-policy
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-dandi
    comparison_kind: benchmark
    metric: "public anchor verdict stability"
    threshold: "must remain PASS"
    verdict: pass
    recommended_action: "Carry the preserved DANDI anchor into Phase 2 while keeping the overall gate open."
    notes: "DANDI stayed PASS under scan policy and selected a richer window with 41 codec events at start_sample 16871250; the old first window ranked 5/9."
  - subject_id: claim-window-policy
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-ajile
    comparison_kind: baseline
    metric: "informative-window engagement versus fixed-window baseline"
    threshold: "selected window should not remain obviously quiet"
    verdict: pass
    recommended_action: "Use the informative-window AJILE result for Phase 3 family-boundary adjudication, not as a breadth win."
    notes: "AJILE first window ranked 9/9, the selected window had event_count=3, and the rerun still ended in SPIKEINTERFACE_FAIL."
duration: 24min
completed: 2026-03-20
---

# Phase 01: Public Corpus Window Policy Summary

**Deterministic candidate-window scanning preserved the DANDI anchor and showed AJILE remains an informative-window failure rather than a fixed-window artifact.**

## Performance

- **Duration:** 24 min
- **Started:** 2026-03-20T17:28:03Z
- **Completed:** 2026-03-20T17:51:44Z
- **Tasks:** 3
- **Files modified:** 4

## Key Results

- Implemented a deterministic `scan` policy over nine candidate windows with explicit per-target and aggregate selection artifacts.
- DANDI `000034` remained `PASS` and moved from an implicit first window to a selected window at `start_sample = 16871250` with `41` codec events; the original first window ranked `5/9`.
- AJILE12 selected an informative window at `start_sample = 20889595` with `3` codec events and `3` active channels, yet still failed on `SPIKEINTERFACE_FAIL`, making the failure more trustworthy than the fixed-window baseline.

## Task Commits

No atomic commit was created during this run. The work remains uncommitted in the existing dirty lane repo.

## Files Created/Modified

- `.gpd/phases/01-public-corpus-window-policy/01-01-SUMMARY.md` - contract-backed closeout for the plan
- `src/zpe_neuro/public_corpus.py` - deterministic candidate-window selection and artifact emission
- `tools/run_public_corpus_eval.py` - CLI flags for window policy and candidate-window count
- `src/zpe_neuro/__init__.py` - lazy exports to avoid heavy imports during focused tests
- `tests/test_public_corpus_window_selection.py` - deterministic candidate-window selection coverage
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_window_selection_summary.json` - aggregate selection artifact
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_summary.json` - rerun authority summary

## Next Phase Readiness

Phase 2 can reuse the selection machinery directly. The next decisive question is now narrower: find a real IBL waveform slice path on the M1, without counting metadata access or quiet-window behavior as execution success.

## Contract Coverage

- Claim IDs advanced: `claim-window-policy -> passed`
- Deliverable IDs produced: `deliv-window-selection -> passed`, `deliv-rerun-summary -> passed`
- Acceptance test IDs run: `test-window-selection -> passed`, `test-dandi-anchor -> passed`
- Reference IDs surfaced: `ref-dandi -> read, compare`; `ref-ajile -> read, compare`; `ref-way-forward -> read, use`
- Forbidden proxies rejected or violated: `fp-quiet-compression -> rejected`; `fp-dandi-breadth -> rejected`
- Decisive comparison verdicts: `claim-window-policy vs ref-dandi -> pass`; `claim-window-policy vs ref-ajile -> pass`

## Validations Completed

- Ran `/Users/Zer0pa/ZPE/ZPE Neuro/.venv/bin/python -m unittest tests.test_public_corpus_window_selection tests.test_wave1_codec tests.test_wave1_metrics tests.test_wave1_determinism` and all five tests passed.
- Reran the public corpus harness with `--window-policy scan --candidate-windows 9` and verified that explicit selection artifacts were written for DANDI and AJILE.
- Compared the new DANDI result against the March 20 Tier 1 anchor and confirmed the verdict remained `PASS`.

## Decisions & Deviations

Kept IBL waveform execution out of Phase 1, matching the research recommendation to keep this phase local and decisive on slice selection first.

Minor deviation: the rerun IBL probe returned an external `503` from `openalyx.internationalbrainlab.org`, so the project-level public summary remained `FAIL` even though the Phase 1 plan contract passed.

## Open Questions

- Is AJILE still failing because it is out-of-family for the first lane, or because the insertion/sorter path still needs a narrower diagnosis?
- What is the smallest honest IBL waveform path that fits within the M1 and local disk budget?
- Should nine candidate windows remain the default, or should the candidate count become target-specific once Phase 2 evidence exists?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| DANDI selected start sample | `s_D` | `16871250` | limited to current nine-window scan | DANDI selection artifact | `sample_limit = 6000`, `channel_limit = 8` |
| DANDI codec event count | `N_D` | `41` | depends on the current ranking policy and selected window | DANDI rerun artifact | selected DANDI scan window |
| AJILE selected start sample | `s_A` | `20889595` | limited to current nine-window scan | AJILE selection artifact | `sample_limit = 6000`, `channel_limit = 8` |
| AJILE codec event count | `N_A` | `3` | insufficient to distinguish family-boundary from sorter-path failure yet | AJILE rerun artifact | selected AJILE scan window |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Nine evenly spaced candidate windows | Streaming a small number of short windows is cheaper than a full-file scan | Selection may miss a better slice outside the sampled starts | Dense activity varies on a finer timescale than the sampled windows capture |
| Eventfulness-first ranking without learned policy | Simple auditable metrics are enough to separate quiet from informative windows | Noise-heavy windows may still score too well on untested targets | Ranking must discriminate among many similarly active windows across larger corpora |

## Issues Encountered

- The rerun IBL probe failed with `IBL_PUBLIC_PROBE_FAIL:503`, which looks external rather than lane-local.
- Local free space fell below `1GiB` during the work session and required safe cache cleanup before Phase 2 can proceed comfortably.

