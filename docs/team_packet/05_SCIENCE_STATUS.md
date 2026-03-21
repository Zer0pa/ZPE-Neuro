# Science Status

## What The Evidence Now Supports

### Supported

- the codec is not confined to synthetic data anymore
- NWB remains a strong insertion anchor
- the SpikeInterface lane is supportable on at least one real public Tier 1 slice

### Not Supported

- real-corpus breadth closure
- the claim that the same current codec surface preserves all frozen breadth targets
- public standardization or release-boundary language

## The Important Scientific Tension

The DANDI `000034` Tier 1 slice behaves like the current codec family expects: spike-like activity, high sampling rate, meaningful event extraction, clean insertion results.

AJILE12 does not.

On the tested AJILE12 slice:

- sampling rate is much lower
- the current spike-template surface extracts no events
- NWB preservation still works
- SpikeInterface insertion does not

That matters because it suggests one of two things:

1. the codec family is still real, but its current first implementation is narrower than the frozen breadth suite
2. the current breadth suite contains at least one scientifically different signal family that the present codec should not be expected to handle without a new mode

## My Scientific Read

My read is that the second interpretation is more likely.

The current codec is fundamentally spike-template oriented. AJILE12 is a human intracranial recording surface with very different statistical structure from the high-rate extracellular spike-like data that the codec currently exploits. That does not make AJILE12 irrelevant, but it does mean the team should not interpret this as the codec almost worked and just needs a minor tweak. It may need a genuinely different representation mode for low-rate, broader-band human neural signals.

## Consequence

The team now has enough evidence to stop treating breadth as a vague follow-on. Breadth is the main scientific design question.
