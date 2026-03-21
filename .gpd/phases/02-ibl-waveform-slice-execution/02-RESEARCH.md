# Phase 02 Research: IBL Waveform Slice Execution

## Objective

Research the most defensible local method for turning the IBL public probe into a real waveform-slice execution path on the M1.

## Current Evidence

- The earlier public IBL probe established metadata visibility but did not reach waveform bytes.
- The public AWS bucket `ibl-brain-wide-map-public` is reachable anonymously and exposes real raw ephys prefixes under `data/cortexlab/Subjects/`.
- A concrete KS014 raw AP trio exists for `2019-12-03/001/probe00`: one `.meta`, one `.ch`, and one `.cbin`.
- The corresponding `.ch` metadata reports `2927` chunks and `30000` samples in the first chunk.
- A range request against the `.cbin` succeeds, and a one-off local prototype opened the first chopped chunk with `spikeglx.Reader` and read a real `6000 x 8` slice.
- The prototype produced plausible microvolt-scale extrema, which is strong evidence that a local M1 execution path exists now without RunPod.

## Mathematical / Signal Framework

IBL AP data arrives as compressed SpikeGLX streams with chunk metadata in the `.ch` sidecar. The minimal honest execution path is:

1. Fetch the small `.meta` and `.ch` files.
2. Use the `.ch` sidecar to select one compressed chunk and its sample bounds.
3. Range-fetch only that byte span from the `.cbin`.
4. Rebase the chunk metadata so `spikeglx.Reader` can open the chopped local files.
5. Read a bounded `samples x channels` slice and convert volts to microvolts before passing it into the existing evaluation harness.

The current codec and insertion path operate on waveform slices, not metadata. Phase 2 therefore succeeds only when the artifact records real waveform execution or an explicit measured block.

## Known Good / Known Bad Limits

### Known Good

- Unsigned access to the public IBL S3 bucket.
- One-second AP chunks with companion metadata.
- Small local slices such as `6000 x 8` sampled from a single chunk.
- `ibl-neuropixel` and `mtscomp` as the lightest dependency path to `spikeglx.Reader`.

### Known Bad Or Suspicious

- Treating ONE metadata discovery alone as waveform success.
- Pulling full `.cbin` files or wide channel counts on the current disk budget.
- Installing the full `ibllib` stack when only `spikeglx.Reader` is needed.
- Conflating downstream SpikeInterface failures with failure to execute the waveform slice itself.

## Limiting Cases To Preserve

- If the public bucket or a byte range fails, the artifact should record a measured block, not a narrative success.
- If the waveform slice executes but downstream insertion fails, the artifact should say "waveform slice executed" while keeping `evaluation_status` separate.
- If the slice requires a whole-file download, the phase should treat that as a local-feasibility regression rather than silently widening scope.

## Computational Methods

### Recommended

- Use an unsigned `boto3` client with explicit byte ranges.
- Trim the `.ch` metadata to a single chunk and mark it as chopped.
- Open the local chunk with `spikeglx.Reader` from `ibl-neuropixel`.
- Convert the returned volts to microvolts with `sample2volts`.
- Reuse the existing codec and insertion harness so the new target is judged by the same lane criteria as the prior public targets.

### Rejected For Phase 2

- Auth-dependent or hanging ONE download flows when a public raw-byte route already exists.
- Full-file local staging of the `.cbin`.
- RunPod escalation before a real local block is measured.

## Potential Pitfalls

- Leaking sensitive local auth material while investigating ONE behavior.
- Writing artifacts that imply a full-target pass when only waveform existence has been proven.
- Allowing transient cache growth to erase the recovered `2.3Gi` local headroom.
- Breaking the existing package import path by introducing new heavy dependencies into the default environment.

## Recommended Phase 2 Plan

1. Encode one concrete public AP target and the bounded chunk-materialization path in the codebase.
2. Add a focused unit test around chunk-metadata rebasing so the single-chunk path is not purely manual.
3. Run the local waveform eval into a dedicated proof root and inspect the resulting artifact.
4. Record materialized byte counts, target keys, and any remaining escalation criteria explicitly.

## Next Phase Dependency

If Phase 2 yields a real IBL waveform artifact, Phase 3 can decide breadth using executed targets only. If it ends in a measured block, Phase 3 must treat IBL as unresolved rather than narrating closure.
