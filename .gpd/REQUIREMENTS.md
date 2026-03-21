# Requirements: ZPE-Neuro Lane 1 Public-Corpus Authority

**Defined:** 2026-03-20
**Core Research Question:** Can ZPE-Neuro close `AM-NEU-01` honestly by replacing fixed-slice probing with reproducible public-corpus selection and by adding a second in-family extracellular breadth target, without regressing the existing DANDI Tier 1 authority anchor?

## Primary Requirements

### Calculations

- [ ] **CALC-01**: Score reproducible candidate windows for DANDI `000034` and AJILE12 using decision-grade activity metrics instead of fixed first-window selection.
- [ ] **CALC-02**: Emit a durable window-selection artifact that records candidate starts, selection scores, rejected quiet slices, and the chosen evaluation window per target.

### Implementations

- [ ] **IMPL-01**: Refactor the public-corpus harness to accept a reproducible window-selection policy and surface the selected slice metadata in per-target artifacts.
- [ ] **IMPL-02**: Implement an M1-local IBL waveform-slice path or produce a measured local-feasibility record that justifies escalation criteria without narrating closure.

### Validations

- [ ] **VALD-01**: Preserve the current DANDI `000034` public insertion pass under the new selection policy.
- [ ] **VALD-02**: Reject quiet-slice compression wins explicitly when eventfulness or insertion evidence is absent.
- [ ] **VALD-03**: Produce a rerun public-corpus summary whose breadth verdict is grounded in real waveform execution and explicit family-boundary logic.

### Decisions

- [ ] **DECN-01**: Produce an explicit AJILE12 family-boundary decision memo based on informative-slice evidence.
- [ ] **DECN-02**: State whether the first commercial wedge should remain a narrow extracellular codec or whether a broader lane requires a separate representation mode.

## Follow-up Requirements

### Performance

- **PERF-01**: Tune hotspots only after the authority path is stable.
- **PERF-02**: Consider RunPod or broader sorter campaigns only after measured local blockage.

## Out of Scope

| Topic | Reason |
| --- | --- |
| Public-readiness claims | `AM-NEU-01` is still open |
| README/product messaging upgrades | would turn mixed evidence into narrative progress |
| Broad human-neural support claims | not justified until the family boundary is decided |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| --- | --- | --- |
| CALC-01 | deterministic candidate starts and stable ranking inputs | compare repeated selection runs on the same target |
| IMPL-01 | per-target artifacts include selected window metadata and selection evidence | inspect JSON artifact fields and rerun harness |
| VALD-01 | no regression on DANDI pass verdict | rerun DANDI insertion under selected-window policy |
| VALD-02 | false proxies are explicitly rejected in artifacts | inspect failure reasons and selection notes |
| VALD-03 | summary verdict reflects only real executed targets | inspect summary plus linked per-target artifacts |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| --- | --- | --- | --- | --- |
| CALC-02 | window-selection JSON artifact | March 20 rerun artifacts, `07_WAY_FORWARD.md` | fixed-window public corpus outputs | quiet high-compression windows |
| IMPL-02 | IBL waveform execution artifact or measured local-failure note | `public_corpus_ibl_probe.json` | current metadata-only probe | metadata-only access |
| VALD-01 | DANDI rerun artifact | DANDI `000034` pass artifact | current repo-local DANDI pass | any regression hidden by broader wins |
| DECN-01 | AJILE family-boundary memo | AJILE rerun artifact | current AJILE fail artifact | calling AJILE "almost working" without evidence |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| CALC-01 | Phase 1: Public Corpus Window Policy | Pending |
| CALC-02 | Phase 1: Public Corpus Window Policy | Pending |
| IMPL-01 | Phase 1: Public Corpus Window Policy | Pending |
| VALD-01 | Phase 1: Public Corpus Window Policy | Pending |
| VALD-02 | Phase 1: Public Corpus Window Policy | Pending |
| IMPL-02 | Phase 2: IBL Waveform Slice Execution | Pending |
| VALD-03 | Phase 3: Breadth Adjudication And Public Rerun | Pending |
| DECN-01 | Phase 3: Breadth Adjudication And Public Rerun | Pending |
| DECN-02 | Phase 4: Lane 1 Wedge Decision | Completed |

**Coverage:**

- Primary requirements: 8 total
- Mapped to phases: 8
- Unmapped: 0

---

_Requirements defined: 2026-03-20_
_Last updated: 2026-03-21 after Phase 4 wedge decision_
