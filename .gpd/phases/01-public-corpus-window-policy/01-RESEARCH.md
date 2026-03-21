# Phase 01 Research: Public Corpus Window Policy

## Objective

Research the most defensible local method for replacing fixed first-window probing with a reproducible candidate-window policy in the public-corpus harness.

## Current Evidence

- DANDI `000034` passes on the current fixed `6000 x 8` slice and is the existing positive public anchor.
- AJILE12 fails on the tested fixed `6000 x 8` slice with zero codec events and a failed SpikeInterface insertion.
- The March 20 packet already identifies fixed-window probing as acceptable for an initial honest probe but insufficient for final breadth adjudication.

## Mathematical / Signal Framework

The current codec is event-oriented and spike-template biased. A window policy therefore has to optimize for informative extracellular activity rather than generic energy alone. Useful candidate-window signals are:

- codec event count from the current template extractor
- per-channel robust amplitude spread
- active-channel count
- negative excursion counts or other sparse-event indicators

The selection policy must remain deterministic and cheap. This phase should not add learned ranking or any policy that depends on prior favorable outcomes.

## Known Good / Known Bad Limits

### Known Good

- High-rate extracellular slices similar to the DANDI `000034` anchor.
- Small-channel, short-duration windows that fit comfortably in memory.

### Known Bad Or Suspicious

- Low-rate quiet windows where compression rises because the codec barely engages.
- Any policy that requires downloading or caching large public corpora locally.
- Any ranking metric that can be gamed by noise spikes without preserving insertion behavior.

## Limiting Cases To Preserve

- If all candidate windows for a target are quiet, the selected window should still say so explicitly rather than manufacturing success.
- If a target has multiple informative windows, deterministic start ordering should make the same winner reproducible across reruns.
- If DANDI remains healthy while AJILE still fails on informative windows, that should strengthen a family-boundary conclusion rather than count as a regression.

## Computational Methods

### Recommended

- Evenly spaced candidate starts across each source recording, constrained to a small count so the M1 path remains cheap.
- Stream only the candidate slices needed for scoring instead of reading entire recordings.
- Score windows with a combination of eventfulness and robust amplitude statistics.
- Emit a dedicated selection artifact per target plus a summary artifact across targets.

### Rejected For Phase 1

- Full-file activity scans.
- Learned policies or non-deterministic ranking.
- GPU or RunPod escalation.
- IBL execution in this phase. Keep it as Phase 2 so Phase 1 stays local and decisive.

## Potential Pitfalls

- Picking a window solely by compression ratio will recreate the AJILE false-positive problem in a different form.
- Ranking solely by amplitude can over-select noise.
- Hidden cache writes from remote libraries can consume scarce disk space.
- Changing the selected slice without surfacing the comparison against the old fixed-window result would reduce auditability.

## Recommended Phase 1 Plan

1. Add start-offset support and deterministic candidate-window generation to the public corpus harness.
2. Compute simple, auditable candidate metrics per window.
3. Persist per-target and summary selection artifacts.
4. Rerun DANDI and AJILE using the selected windows.
5. Preserve explicit rejection of quiet-slice success proxies in the output payload.

## Next Phase Dependency

If Phase 1 succeeds, Phase 2 can use the same selection machinery to scope an M1-friendly IBL waveform path without introducing a second selection system.
