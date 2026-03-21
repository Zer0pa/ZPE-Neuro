# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-20)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can ZPE-Neuro close `AM-NEU-01` honestly by replacing fixed-slice probing with reproducible public-corpus selection and by adding a second in-family extracellular breadth target, without regressing the existing DANDI Tier 1 authority anchor?
**Current focus:** Phase 6 complete: a fresh `.[gate,dev]` baseline now replays the unit slice plus Gate C and Gate D sequentially, while true blind-clone, Allen, and release-boundary gates remain open

## Current Position

**Current Phase:** 06
**Current Phase Name:** Blind-Clone Authority Pack Baseline
**Total Phases:** 6
**Current Plan:** 1
**Total Plans in Phase:** 1
**Status:** Complete
**Last Activity:** 2026-03-21
**Last Activity Description:** Phase 6 repaired hidden clean-env Gate C dependencies, added a minimal `gate` extra, and validated 12 tests plus Gate C/Gate D sequentially in fresh environments while keeping blind-clone closure explicitly open

**Progress:** [██████████] 100%

## Active Calculations

- What isolated artifact-root policy the true cold-clone authority pack must use so Gate C and Gate D can replay without HDF5 lock collisions
- Whether the heavier public-corpus and IBL replay surface should be split further beyond `.[gate]` before any stronger blind-clone claim
- Which Allen and release-boundary gates remain hard-blocking after the new clean-env baseline

## Intermediate Results

- DANDI `000034` remains `PASS` under the deterministic scan policy
- AJILE12 is now explicitly marked `OUT_OF_FAMILY` for the current Lane 1 spike-oriented codec
- IBL KS014/probe00 now passes as a counted second extracellular public target under bounded chunk, channel-window, and representative-slice search
- The rerun public breadth summary is now `PASS` for the narrowed extracellular lane while broader public-claim and commercialization gates remain open
- A fresh `.[gate,dev]` install now passes the 12-test Phase 1-5 unit slice plus Gate C and Gate D when run sequentially
- The Gate C spikeinterface probe no longer depends on the hidden simple-sorter numba path

## Open Questions

- What exact cold-clone workflow and isolated artifact-root layout turn the new sequential baseline into a real blind-clone authority pack?
- Should `proof` split further to separate public-corpus replay from Gate C/D clean-env validation?
- Which Allen and release-boundary gates remain hard-blocking after the new clean-env baseline?

## Performance Metrics

| Label | Duration | Tasks | Files |
| --- | --- | --- | --- |
| Phase 01 selected-window rerun | 24 min | 3 | 4 |
| Phase 02 IBL waveform execution | 33 min | 3 | 5 |
| Phase 03 breadth adjudication | 19 min | 4 | 8 |
| Phase 05 bounded IBL refinement | pod-bound | 6 | 10 |
| Phase 06 clean-env gate baseline | local env | 5 | 8 |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [Repo realignment]: keep the inner repo as the source of truth for code and evidence
- [Breadth discipline]: reject quiet-slice compression wins as breadth evidence
- [Resource policy]: stay on local hardware until a real RunPod trigger exists
- [Window policy]: use deterministic candidate-window scanning rather than a fixed first window for public reruns
- [AJILE interpretation]: treat the selected-window AJILE fail as real evidence, not as breadth progress
- [IBL route]: prefer the unsigned public S3 raw-byte path over the fragile authenticated ONE route for Phase 2
- [Execution split]: keep waveform existence separate from downstream evaluation so Phase 2 does not narrate a full pass
- [Family boundary]: classify AJILE12 as out-of-family for Lane 1 rather than treating it as a hidden breadth near-miss
- [Breadth counting]: count only real waveform breadth targets and preserve DANDI strictly as the authority anchor
- [Lane 1 wedge]: lock the first lane to extracellular authority and keep broader neural coverage outside Lane 1 unless a second representation mode is added
- [IBL breadth rescue]: allow bounded chunk, channel-window, and representative-slice search for IBL so long as the downstream contract does not drift
- [Phase 06]: Added Phase 6: Blind-Clone Authority Pack Baseline — Extends the current milestone from public-breadth closure into clean-env authority-pack validation and dependency-boundary repair

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| Selected-window public probe | `C = 8`, `W = 9`, short reruns with deterministic window ranking | selected channels, candidate count, and window policy | active baseline | Valid for the current narrowed public packet |
| Bounded IBL refinement | bounded chunk grid, fixed `8`-channel windows, deterministic representative windows | search-grid breadth and unchanged downstream contract | passing second-target candidate at chunk `732`, channels `128:136`, window `12000` | Valid for Phase 5 only |
| Evidence-bound Lane 1 recommendation | carried-forward DANDI, AJILE, IBL, and breadth packet only | scope drift beyond executed artifacts | extracellular wedge with counted public breadth support | Valid but still below blind-clone and release thresholds |
| Sequential clean-env gate baseline | fresh `.[gate,dev]` env, sequential gate writes, repo-local artifact root | artifact-root isolation and extra split beyond the gate slice | fresh Gate C/Gate D baseline plus 12-test unit slice | Valid for Phase 6 baseline only |

**Convention Lock:**

- Metric signature: not set
- Fourier convention: not set
- Natural units: not set
- Gauge choice: not set
- Regularization scheme: not set
- Renormalization scheme: not set
- Coordinate system: sample index with channel-major decoded arrays
- Spin basis: not set
- State normalization: waveform amplitudes tracked in microvolts after any conversion
- Coupling convention: not set
- Index positioning: windows use zero-based half-open sample ranges `[start, start + sample_limit)`
- Time ordering: candidate windows are evaluated in deterministic ascending start order
- Commutation convention: not set
- Levi-Civita sign: not set
- Generator normalization: not set
- Covariant derivative sign: not set
- Gamma matrix convention: not set
- Creation/annihilation order: not set

### Propagated Uncertainties

| Quantity | Current Value | Uncertainty | Last Updated (Phase) | Method |
| --- | --- | --- | --- | --- |
| Public breadth verdict | PASS for narrowed extracellular lane | Breadth now closes for DANDI anchor plus counted IBL second-target support, but this does not imply blind-clone or public-release readiness | Phase 05 | Phase 5 bounded IBL search packet and rerun breadth adjudication |
| Lane 1 wedge scope | extracellular-only with counted public breadth support | Broader human or intracranial coverage still requires a second representation mode or separate lane | Phase 05 | Phase 4 wedge memo plus Phase 5 bounded IBL refinement |
| Blind-clone gate baseline | PASS for `.[gate,dev]` unit slice plus sequential Gate C/Gate D replay | Full cold-clone replay, parallel artifact isolation, and heavier proof/public replay remain open | Phase 06 | Fresh `.[gate,dev]` validation with sequential Gate C and Gate D reruns |

### Pending Todos

None yet.

### Blockers/Concerns

- True blind-clone replay and release-boundary work remain open.
- Parallel gate runs still collide on the shared artifact root unless outputs are isolated.
- Allen parity and broader commercialization risk remain open.

## Session Continuity

**Last session:** 2026-03-21
**Stopped at:** Phase 6 established the `.[gate,dev]` clean-env baseline; next work should run a true cold-clone authority-pack replay with isolated artifact roots
**Resume file:** .gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md
