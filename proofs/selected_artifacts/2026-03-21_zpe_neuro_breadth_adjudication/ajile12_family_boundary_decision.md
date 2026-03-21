# AJILE12 Family Boundary Decision

- Decision: `OUT_OF_FAMILY`
- Confidence: `medium`
- Status: `PASS`

## Verdict
AJILE12 is out-of-family for the current Lane 1 spike-oriented codec; the lane should narrow around extracellular-style authority rather than narrate broad support.

## Evidence Basis
- DANDI remains the sovereign positive anchor: the selected-window rerun stayed PASS with 41 codec events and 34 detected peaks.
- AJILE no longer hides behind a quiet first window: the scan policy promoted an informative slice at sample 20889595 where the first window ranked 9.
- That informative AJILE slice still produced only 3 codec events at 500 Hz, with 0 detected peaks and final status FAIL.
- IBL now proves a second extracellular-style waveform path exists locally, but the first bounded slice still failed downstream with 0 detected peaks, so breadth remains open even though the family is better aligned than AJILE.

## Source Artifacts
- DANDI selected-window eval: `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- AJILE selected-window eval: `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`
- AJILE selection artifact: `proofs/selected_artifacts/2026-03-20_zpe_neuro_window_policy_rerun/public_corpus_window_selection_ajile12_sub01_ses7_ecephys.json`
- IBL waveform eval: `proofs/selected_artifacts/2026-03-20_zpe_neuro_ibl_waveform_probe/public_corpus_ibl_waveform_eval.json`

## Next-Lane Implication
Treat Lane 1 as a narrower extracellular wedge. Human intracranial breadth should be a separate lane or a later second-mode effort, not a hidden requirement for the current codec.
