# Way Forward

## My View

The right move is not to chase a better narrative. The right move is to keep the inner repo as the source-of-truth lane and make the public-corpus harness the center of gravity while answering one hard question:

`Is ZPE-Neuro’s first real product a spike-oriented extracellular codec with narrower but stronger authority, or a broader neural-signal codec that needs a second representation mode?`

Right now the evidence says:

- Tier 1 extracellular-style public insertion is real
- breadth across a human low-rate corpus is not real on the current codec

That is the real fork.

## Recommended Next Sequence

### 1. Keep All New Evidence In The Inner Repo

- route future receipts, proof artifacts, and status docs into the GitHub-linked inner repo
- treat the outer folder as a workspace wrapper only

### 2. Resolve The AJILE12 Meaning, Not Just The AJILE12 Error

Do a focused scientific determination:

- either confirm AJILE12 is in-family and build a representation that can engage it
- or explicitly amend the breadth suite and replace it with a more appropriate extracellular breadth target

My recommendation is to treat this as a science decision first, not just an implementation task.

### 3. Add A Slice-Selection And Activity-Scanning Pass

The current public-corpus harness uses a fixed first-window slice. That is acceptable for an initial honest probe, but not for final breadth adjudication.

Next change should:

- scan candidate windows
- measure signal activity and eventfulness
- select representative slices reproducibly
- record the selection policy as an artifact

### 4. Implement IBL Waveform Slice Execution

Metadata access is already solved. The next engineering step is a real IBL waveform slice path.

This matters because it provides a second extracellular-style public breadth test that may be more aligned with the present codec than AJILE12.

### 5. Keep NWB As The Primary Insertion Anchor

NWB is the cleanest insertion surface today.

SpikeInterface should remain active, but only as a target-level claim:

- DANDI `000034`: supported
- AJILE12: unsupported

### 6. Delay GPU/RunPod Escalation Until A Clear Local Block Exists

Only escalate off the M1 when one of these is true:

- IBL waveform slicing is implemented but too slow or memory-heavy locally
- breadth window scanning becomes too large for local turnaround
- a clearly defined external sorter campaign requires GPU

Do not escalate just because the local path is now respectable.

## Concrete Near-Term Deliverables

The next sprint should produce:

1. a window-selection artifact for AJILE12 and DANDI
2. a real IBL waveform slice runner
3. a decision memo on whether AJILE12 is in-family or out-of-family for the first-lane codec
4. a rerun of the public-corpus packet with those changes

## Bottom-Line Recommendation

Treat the project as a real but still narrowing scientific program, not as a nearly finished product. The strongest next step is to sharpen the family boundary scientifically and then let engineering follow that boundary precisely.
