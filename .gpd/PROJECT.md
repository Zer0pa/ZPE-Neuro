# ZPE-Neuro Lane 1 Public-Corpus Authority

## What This Is

This project turns the current repo-local ZPE-Neuro evidence into a disciplined Lane 1 research program around public-corpus authority. The immediate focus is not broad marketing coverage; it is determining whether the first durable commercial wedge is a spike-oriented extracellular codec with real authority, or whether breadth requires a second representation mode that should be treated as a separate lane.

## Core Research Question

Can ZPE-Neuro close `AM-NEU-01` honestly by replacing fixed-slice probing with reproducible public-corpus selection and by adding a second in-family extracellular breadth target, without regressing the existing DANDI Tier 1 authority anchor?

## Scoping Contract Summary

### Contract Coverage

- `claim-window-policy`: success means the public harness no longer relies on a fixed first-window probe and emits reproducible selection evidence.
- `claim-second-target`: success means a second in-family public target is evaluated through a real waveform path, not metadata only.
- `claim-family-boundary`: success means AJILE12 is either supported with informative-slice evidence or explicitly documented as out-of-family for the first lane.

### User Guidance To Preserve

- **User-stated observables:** public-corpus verdicts, informative-slice activity, IBL waveform execution, AJILE family meaning.
- **User-stated deliverables:** window-selection artifact, IBL waveform slice runner, family-boundary memo, rerun public-corpus packet.
- **Must-have references / prior outputs:** repo-local March 20 rerun artifacts, [07_WAY_FORWARD](./phases/01-public-corpus-window-policy/../..//../docs/team_packet/07_WAY_FORWARD.md), Comet run, DANDI `000034`, AJILE12, IBL public probe.
- **Stop / rethink conditions:** do not escalate to RunPod without a measured local block; do not let quiet-slice wins count as success; do not accept any regression on the DANDI Tier 1 anchor.

### Scope Boundaries

**In scope**

- reproducible public-corpus slice selection
- DANDI and AJILE public reruns on informative windows
- IBL waveform-slice feasibility on local hardware
- explicit first-lane family-boundary decisions

**Out of scope**

- public-release positioning
- README or product-claim upgrades
- RunPod execution before a local failure threshold is demonstrated
- a generalized human-signal codec without first-lane evidence

### Active Anchor Registry

- `Ref-DANDI-000034`: DANDI `000034` public Tier 1 insertion artifact
  - Why it matters: current sovereign positive anchor for the lane
  - Carry forward: planning, execution, verification, writing
  - Required action: read, compare, cite
- `Ref-AJILE12`: AJILE12 rerun artifact
  - Why it matters: current breadth failure that defines the family-boundary question
  - Carry forward: planning, execution, verification, writing
  - Required action: read, compare, cite
- `Ref-IBL-PROBE`: repo-local IBL metadata probe artifact
  - Why it matters: shows public access works but waveform execution is still open
  - Carry forward: planning, execution, verification
  - Required action: read, use, compare
- `Ref-WAY-FORWARD`: `docs/team_packet/07_WAY_FORWARD.md`
  - Why it matters: defines the next truthful work sequence
  - Carry forward: planning, execution, verification
  - Required action: read, use

### Carry-Forward Inputs

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_summary.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_ibl_probe.json`
- `docs/team_packet/07_WAY_FORWARD.md`

### Skeptical Review

- **Weakest anchor:** whether an M1-local IBL waveform path can be reduced without hidden large-file cost.
- **Unvalidated assumptions:** that the current AJILE12 failure is dominated by fixed-window quiet-slice bias rather than a real family mismatch.
- **Competing explanation:** the first lane may already be intrinsically extracellular-only and should not spend major scope on low-rate intracranial breadth.
- **Disconfirming observation:** informative-window reruns still show no meaningful codec engagement on AJILE12 or a second extracellular corpus.
- **False progress to reject:** high compression on quiet windows, metadata-only probes, or DANDI-only success being narrated as broad public closure.

### Open Contract Questions

- Which IBL dataset path yields the smallest honest local waveform slice path on the M1?
- Does informative-window selection materially change the AJILE12 conclusion, or only make the existing failure more trustworthy?
- Is the correct commercial wedge a narrowed extracellular product with stronger authority instead of broader neural coverage?

## Research Questions

### Answered

- The repo-local DANDI `000034` Tier 1 path is real and currently passes.

### Active

- [ ] Can window selection be made reproducible and decision-grade instead of fixed-slice?
- [ ] Can a second extracellular-style public corpus execute locally through a real waveform path?
- [ ] Does AJILE12 belong inside the first-lane authority family?

### Out of Scope

- General human-neural breadth without first-lane evidence — would require a different representation mode and larger scope.

## Research Context

### Physical System

Extracellular-style electrophysiology slices and adjacent public neural recordings evaluated through a spike-template oriented codec plus insertion harness.

### Theoretical Framework

Sparse event-driven neural signal coding, waveform-template matching, and public corpus validation under reproducibility and local-compute constraints.

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --- | --- | --- | --- |
| window length | `N_w` | `6000` samples baseline | subject to reproducible selection policy |
| channel count | `C` | `8` current probe slice | held small for M1-local evaluation |
| DANDI sampling rate | `f_s^D` | `30000 Hz` | current positive anchor |
| AJILE sampling rate | `f_s^A` | `500 Hz` | current breadth mismatch candidate |

### Known Results

- DANDI `000034` currently passes the repo-local public insertion path.
- AJILE12 currently fails on the tested fixed window with zero codec events.
- IBL public access is solved at metadata level only.

### What Is New

This project formalizes the authority question as a contract-backed research program inside `.gpd`, with reproducible slice selection and explicit family-boundary decisions instead of ad hoc reruns.

### Target Venue

Internal authority program and commercialization wedge definition. No public venue is in scope until `AM-NEU-01` is honestly closed or redefined.

### Computational Environment

MacBook Air M1, Red Magic 10 Pro+ via ADB, existing workspace `.venv`, optional RunPod only after user-confirmed local blockage.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for project conventions.

## Unit System

Microvolts for waveform amplitudes, samples for indices, seconds and hertz for timing and rate.

## Requirements

See `.gpd/REQUIREMENTS.md`.

## Key References

- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_eval_ajile12_sub01_ses7_ecephys.json`
- `proofs/selected_artifacts/2026-03-20_zpe_neuro_repo_realignment/public_corpus_ibl_probe.json`
- `docs/team_packet/07_WAY_FORWARD.md`

## Constraints

- **Authority:** the repo-local proof surface is sovereign.
- **Compute:** start on M1 and Red Magic only.
- **Disk:** keep large transient outputs off disk unless they are required evidence.
- **Operational:** Comet and GitHub support the proof chain but do not replace it.

## Key Decisions

| Decision | Rationale | Outcome |
| --- | --- | --- |
| Keep the inner repo as source of truth | Avoid status drift across outer and inner git surfaces | Active |
| Reject quiet-slice wins as breadth evidence | Compression without events is a false proxy | Active |
| Delay RunPod until a local block is measured | Preserve honest local feasibility and avoid premature escalation | Active |

---

_Last updated: 2026-03-20 after GPD bootstrap from the Lane 1 brief_
