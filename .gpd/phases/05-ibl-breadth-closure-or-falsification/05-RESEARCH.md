# Phase 05 Research: IBL Breadth Closure Or Falsification

## Objective

Determine whether the open IBL breadth failure is a real codec-family limit or an artifact of the current bounded probe (`chunk_index = 0`, `channel_start = 0`, `sample_limit = 6000`, first window only).

## Current Evidence

- The IBL public S3 raw-byte path is real and locally executable.
- The current IBL artifact proves waveform existence but only for one `6000 x 8` slice.
- That slice produced codec events and an NWB roundtrip `PASS`, but SpikeInterface peak detection returned `0` peaks and the sorter probe failed.
- The current failure therefore combines three possible explanations:
  1. the current codec genuinely does not preserve a second extracellular breadth target well enough,
  2. the chosen chunk or channel span is unrepresentative,
  3. the representative window inside the chosen chunk is too quiet or unhelpful.

## Scientific Interpretation

The present IBL failure is too narrow to be the final scientific verdict on the second extracellular target. The current search space has three hard constraints that likely dominate the outcome:

1. **Chunk choice**
   The recording contains thousands of `30000`-sample chunks. Using only chunk `0` effectively assumes the start of the recording is representative.

2. **Channel-window choice**
   The IBL probe has `385` channels. Using only channels `0:8` effectively assumes the first eight channels carry useful spike-bearing signal. That is a weak assumption for a Neuropixels-style probe.

3. **Representative slice choice**
   Even inside a chosen chunk and channel span, a single first window can be quiet or uninformative. Phase 1 already demonstrated that fixed first-window probing is not acceptable as a closure surface.

## Ratified Next Move

The highest-leverage next phase is **bounded IBL downstream refinement**, not second-mode lane design.

Why:

- It is the only near-term path that can still advance the sovereign Lane 1 metric without redefining the lane.
- It stays in-family: extracellular public waveform evaluation remains the governing object.
- It produces a real bifurcation:
  - if bounded search finds a passing second extracellular target, `AM-NEU-01` advances honestly;
  - if bounded search still fails, the IBL rescue route is materially weaker and Lane 1 fail-forward hardens.

## Execution Strategy

Use a staged search that preserves the existing downstream contract:

1. **Coarse search**
   Evaluate a bounded grid of chunk indices, `8`-channel windows, and representative windows inside each chunk.
   Rank candidates by codec eventfulness and signal magnitude.

2. **Peak-probe shortlist**
   Run SpikeInterface peak detection on the highest-value coarse candidates without full sorter fanout.
   Use actual `peak_count` to rank which candidates deserve the expensive full evaluation.

3. **Full evaluation**
   For the best shortlist candidates only, rerun:
   - codec metrics
   - NWB roundtrip
   - SpikeInterface sorter probe

4. **Decision**
   - If any candidate passes unchanged downstream criteria, rerun breadth adjudication with the new IBL artifact.
   - If no candidate passes, write a falsification-grade decision note and rerun breadth adjudication with the stronger failure evidence.

## Invariants

- Do not lower the downstream contract threshold to force a pass.
- Do not use the DANDI anchor to imply breadth closure.
- Do not retain large temporary search caches when the result is already logged in repo artifacts or Comet.
- Prefer RunPod `/workspace` for execution because the local proof environment was intentionally stripped to preserve Mac disk health.

## Kill Criteria

Treat the bounded IBL rescue route as **falsified for the current lane** if:

- no searched candidate produces a meaningful SpikeInterface peak population, or
- the best candidates still fail the unchanged sorter probe after bounded chunk/channel/window search.

That would not kill the whole sector. It would kill the idea that the current Lane 1 codec can quietly rescue the second extracellular breadth target through small local adjustments.
