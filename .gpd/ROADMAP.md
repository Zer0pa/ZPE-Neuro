# Roadmap: ZPE-Neuro Lane 1 Public-Corpus Authority

## Lane 1 Milestone v1.0: Local Public-Corpus Authority Sharpening

## Phases

- [x] **Phase 1: Public Corpus Window Policy** - replace fixed first-window probing with reproducible selection and preserve the DANDI anchor
- [x] **Phase 2: IBL Waveform Slice Execution** - reduce IBL to a real local waveform path or measure the local block honestly
- [x] **Phase 3: Breadth Adjudication And Public Rerun** - decide the AJILE family boundary and rerun the public-corpus packet
- [x] **Phase 4: Lane 1 Wedge Decision** - turn the evidence into an honest first-lane product recommendation
- [x] **Phase 5: IBL Breadth Closure Or Falsification** - run a bounded IBL refinement that either closes the counted extracellular breadth target or falsifies that route more strongly
- [x] **Phase 6: Blind-Clone Authority Pack Baseline** - establish a minimal clean-env gate baseline and surface the remaining cold-clone gap honestly

## Phase Details

### Phase 1: Public Corpus Window Policy

**Goal:** Replace fixed-slice probing with reproducible candidate-window selection and preserve the DANDI Tier 1 public anchor.
**Depends on:** None
- Advances: claim-window-policy, claim-dandi-anchor
- Anchor coverage: Ref-DANDI-000034, Ref-AJILE12, Ref-WAY-FORWARD
- Forbidden proxies: fp-quiet-compression, fp-dandi-breadth
**Success Criteria:**

1. A deterministic candidate-window policy exists for DANDI and AJILE12.
2. Selection artifacts record candidate starts, scores, and the chosen window.
3. Quiet-window false positives are visible and rejected.
4. DANDI remains a pass under the selected-window policy.

Plans:

- [x] 01-01: implement candidate-window scoring, selection artifacts, and rerun DANDI plus AJILE under the new policy

### Phase 2: IBL Waveform Slice Execution

**Goal:** Turn IBL from metadata-only access into a real local waveform-slice execution path or a measured local-feasibility limit.
**Depends on:** Phase 1
- Advances: claim-second-target
- Anchor coverage: Ref-IBL-PROBE, Ref-WAY-FORWARD
- Forbidden proxies: fp-ibl-metadata
**Success Criteria:**

1. A concrete IBL dataset path for waveform access is identified.
2. The local path either yields a real waveform slice artifact or a measured block.
3. Any escalation criteria are explicit and evidence-backed.

Plans:

- [x] 02-01: identify an M1-local IBL waveform path and record feasibility constraints
- [x] 02-02: run an IBL waveform slice through the codec and insertion harness when locally viable

### Phase 3: Breadth Adjudication And Public Rerun

**Goal:** Decide whether AJILE12 is inside the first-lane family and rerun the public-corpus packet accordingly.
**Depends on:** Phase 2
- Advances: claim-family-boundary
- Anchor coverage: Ref-AJILE12, Ref-DANDI-000034, Ref-IBL-PROBE
- Forbidden proxies: fp-ajile-almost, fp-dandi-breadth
**Success Criteria:**

1. AJILE12 is either supported with evidence or explicitly marked out-of-family.
2. The rerun summary only counts real waveform targets.
3. The public-corpus summary no longer depends on a fixed first-window probe.

Plans:

- [x] 03-01: write the AJILE family-boundary memo from informative-slice evidence
- [x] 03-02: rerun the public-corpus packet and update the breadth summary

### Phase 4: Lane 1 Wedge Decision

**Goal:** Convert the validated evidence into an honest first-lane wedge recommendation.
**Depends on:** Phase 3
- Advances: claim-lane-decision
- Anchor coverage: Ref-DANDI-000034, Ref-AJILE12, Ref-IBL-PROBE, Ref-WAY-FORWARD
- Forbidden proxies: fp-readiness-narrative
**Success Criteria:**

1. The first commercial wedge recommendation matches the evidence.
2. Any need for a second representation mode is explicit.
3. No public-readiness claim is made unless the gate is genuinely closed.

Plans:

- [x] 04-01: produce the lane recommendation and residual decision register

### Phase 5: IBL Breadth Closure Or Falsification

**Goal:** Test the only remaining near-term route to `AM-NEU-01` closure by searching the public IBL target across chunk, channel-window, and representative slice choice without weakening the downstream contract.
**Depends on:** Phase 4
- Advances: claim-second-target, claim-public-summary
- Anchor coverage: Ref-IBL-PROBE, Ref-DANDI-000034, Ref-WAY-FORWARD
- Forbidden proxies: fp-dandi-breadth, fp-threshold-drift, fp-temp-artifact-proof
**Success Criteria:**

1. A bounded IBL search is executed with explicit chunk, channel-window, and representative-slice policy.
2. The best candidate is rerun through the unchanged codec, NWB roundtrip, and SpikeInterface path.
3. The phase ends with either a real counted second-target `PASS` or an evidence-backed falsification of bounded IBL rescue on the current lane.
4. The breadth summary and lane state surfaces are updated from the new IBL evidence without proxy language.

Plans:

- [x] 05-01: execute the bounded IBL refinement, rerun breadth adjudication, and update the lane state from the result

### Phase 6: Blind-Clone Authority Pack Baseline

**Goal:** Establish the minimal clean-env authority-pack boundary by repairing hidden Gate C dependency assumptions and validating the Phase 1-5 unit slice plus Gate C/Gate D sequentially in a fresh environment.
**Depends on:** Phase 5
- Advances: claim-clean-env-gate-baseline, claim-blind-clone-gap-visibility
- Anchor coverage: repo-local Gate C and Gate D reruns, Phase 5 summary
- Forbidden proxies: fp-ambient-env-pass, fp-sequential-is-blind-clone
**Success Criteria:**

1. A repo-declared minimal gate-validation dependency surface exists.
2. The Phase 1-5 unit slice passes in a fresh clean environment.
3. Gate C and Gate D pass sequentially in that fresh environment.
4. The remaining gap between the sequential baseline and a true blind-clone authority pack remains explicit.

Plans:
- [x] 06-01: repair clean-env Gate C dependency assumptions, codify a `gate` extra, and validate sequential Gate C/Gate D plus the unit slice in a fresh environment

## Milestone Outcome

- Lane 1 is now explicitly narrowed to an extracellular authority wedge anchored on the DANDI Tier 1 pass and a counted IBL second-target pass.
- The public breadth packet for the narrowed extracellular lane now passes under the unchanged downstream contract.
- A fresh `.[gate,dev]` baseline now replays the 12-test unit slice plus Gate C and Gate D sequentially without ambient workspace dependencies.
- Broader human or intracranial coverage still requires a second representation mode or a separate lane.
- True blind-clone replay, Allen-risk handling, and release-boundary gates remain open, so the repo is scientifically stronger but still not public-release ready.
