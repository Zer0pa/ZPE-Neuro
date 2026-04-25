# ZPE-Neuro Next-Phase Plan

Date: `2026-04-23`

Status note:
- This is a standalone review plan for the repo at `/Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro`.
- It is not an official GPD `PLAN.md`, because this checkout does not contain an active `.gpd/ROADMAP.md` or project contract.

## Current status baseline

- Current authority surface: March 21, 2026 bounded extracellular packet.
- Current positive anchors:
  - `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_c_summary.json` -> `PASS`
  - `proofs/selected_artifacts/2026-03-21_zpe_neuro_release_alignment/gate_d_summary.json` -> `PASS`
  - `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` -> `PASS`
- Current lane interpretation:
  - bounded extracellular spike-event extraction
  - not full-waveform compression
  - not broad neural generality
- Open gates that still block a stronger review/commercial posture:
  - no blind-clone authority pack
  - no commercialization-safe closure gate
  - no broader in-family breadth target beyond the present DANDI `000034` + bounded IBL packet

## Sovereign gate

The next phase should not optimize for front-door prose or minor repo hygiene.
The sovereign gate is:

1. Produce a clean independent replay pack from current `origin/main` truth.
2. Extend the in-family public breadth surface with one new honest extracellular target.
3. Update authority routing only after those two gates succeed or fail decisively.

If those do not happen, the workstream remains a staged bounded proof surface.

## Recommended phase

Title: `Authority replay closure + next in-family breadth target`

Primary objective:
Convert ZPE-Neuro from a narrow bounded proof packet into a stronger review/grant posture by closing a minimal blind-clone replay pack and adding one new streamed DANDI breadth target without widening claims beyond the extracellular lane.

## Acceptance criteria

### A. Blind-clone authority pack

- Fresh clone from `origin/main`.
- Clean environment build from declared package surface.
- Successful rerun of:
  - repo-local test slice
  - Gate C
  - Gate D
  - current DANDI `000034` streamed or fixture-backed evaluation
- New tracked receipt packet written under `proofs/selected_artifacts/` or equivalent promoted proof surface.
- Packet must record exact commit SHA, environment, commands, artifact paths, and observed verdicts.

### B. New breadth target

- Add one new in-family public target, with `DANDI 000003` as first choice.
- Run the target through the existing public-corpus pipeline using the same bounded-window contract.
- Return an honest `PASS` or `FAIL`.
- Do not count an operator-only or out-of-lane target as breadth closure.

### C. Authority routing update

- Update `README.md`, `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`, and `docs/market_surface.json` only after A and B land.
- Do not narrate commercialization readiness unless the commercialization gate itself is closed.

## Execution waves

### Wave 0: Repo reconciliation

Goal:
Start from actual live truth before new evidence work.

Tasks:
- Move the working checkout to `origin/main` truth before running authority work.
- Decide whether the local `README.md` wording change should be kept, rebased, or discarded.
- Record current repo drift that affects review surfaces:
  - `README.md` and `CURRENT_AUTHORITY_PACKET.md` still point to `RELEASING.md`, but that file was removed.
  - the GitHub issue tracker still references `.gpd` and `runbooks` paths that no longer exist in this checkout.

Output:
- clean execution branch from current `origin/main`
- short drift ledger

### Wave 1: Minimal blind-clone authority pack

Goal:
Prove that the repo can be replayed from declared surfaces, not only from historical local state.

Tasks:
- Create a clean environment using the declared extras.
- Run unit/regression slice.
- Run Gate C and Gate D on a clean artifact root.
- Run current public-corpus DANDI anchor path.
- Promote decisive outputs into a new dated proof packet.

Expected files:
- `proofs/selected_artifacts/<date>_zpe_neuro_blind_clone_replay/README.md`
- command log
- environment manifest
- test summary
- Gate C summary
- Gate D summary
- DANDI `000034` replay summary
- one top-level verification summary

Disconfirming path:
- If clean replay cannot be completed from declared dependencies, freeze the failure as the result. Do not backfill by leaning on historical local artifacts.

### Wave 2: DANDI `000003` breadth probe

Goal:
Add the strongest next in-family breadth target named by the repo's own dataset register.

Tasks:
- Extend `src/zpe_neuro/public_corpus.py` target registry or make the runner configurable for a new DANDI target.
- Use streamed access first. Do not require full dandiset download unless streaming fails for a documented reason.
- Select a bounded extracellular window under the existing scan policy.
- Run the same codec/eval path used for current public targets.
- Write a machine-readable result and a short decision memo.

Expected files:
- new target result JSON
- window-selection summary
- updated breadth adjudication summary if the target is countable
- decision memo describing whether the target is counted

Disconfirming path:
- If `000003` fails to yield a compatible extracellular slice or breaks the loader assumptions, record `FAIL` and preserve that as the truthful next-boundary result.

### Wave 3: Only-if-needed operator lane

Goal:
Use operator-only compute only if Waves 1-2 expose a real blocker that local CPU work cannot clear.

Allowed escalations:
- CPU pod:
  - only for cleaner isolation or faster repeated replay loops
  - not required for the planned blind-clone pack or streamed DANDI breadth probe
- GPU pod:
  - only if the work explicitly expands to benchmark-only KiloSort4 comparator closure
  - not needed for the immediate next phase

## Compute recommendation

Immediate recommendation:
- `CPU / local laptop is sufficient` for the next decisive phase.

Why:
- Current shipped gates are Python/NWB/SpikeInterface-driven and already have successful recorded runs.
- The codebase uses streamed DANDI access and bounded windows, so the next breadth target is primarily network and dependency management work, not accelerator work.
- The only explicit GPU-dependent path in the repo is the benchmark-only KiloSort4 operator lane.

## Wall-clock estimate

Observed evidence from current repo:
- GitHub `Offline Verify` on `main`: about `58s` on 2026-04-23.
- GitHub `Verify Package Surface` on `main`: about `1m23s` on 2026-04-23.
- Historical local Gate C rerun spacing: about `3m`.
- Historical local Gate D rerun spacing: about `3m`.

Planning estimate:
- Wave 0 repo reconciliation: `30-60 min`
- Wave 1 blind-clone replay pack: `0.5-1.5 days`
- Wave 2 DANDI `000003` breadth probe: `0.5-1 day`
- Optional Wave 3 operator-only escalation: `1-2 days` if Allen or KiloSort4 becomes necessary

Practical total:
- `1-3 focused days` for the recommended next phase without GPU work
- `2-5 days` if the phase expands into Allen dependency isolation or GPU comparator work

## Commercial / grant advantage assessment

Current state:
- There is a real but narrow research-infrastructure wedge.
- There is not yet a disproportionate commercial advantage.

Why:
- The repo already shows a credible bounded extracellular spike-event extraction story with proof lineage.
- That is useful for grant narratives around reproducibility, auditability, and deterministic replay.
- It is not yet a strong commercial moat because the repo itself says:
  - no blind-clone verification
  - no commercialization-safe closure
  - no broad incumbent benchmark displacement story

What would change that:
- a clean blind-clone replay pack
- one more independent in-family public target
- a tighter release/legal routing surface with no dead links or stale management references

## Files likely touched during execution

- `src/zpe_neuro/public_corpus.py`
- `tools/run_public_corpus_eval.py`
- `tools/run_public_corpus_benchmark.py`
- `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- `proofs/selected_artifacts/<new packet>/...`
- `README.md`
- `docs/market_surface.json`

## Explicit non-goals

- Do not spend the phase on front-door prose alone.
- Do not widen claims beyond extracellular spike-event extraction.
- Do not treat KiloSort4 or Allen operator-only work as mandatory unless the primary gate proves insufficient.
- Do not narrate commercialization closure before the evidence exists.
