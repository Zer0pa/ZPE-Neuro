# Phase 07: Reproducible Open-Corpus Replay Pack - Research

**Researched:** 2026-04-05
**Domain:** Reproducible public-corpus replay packaging for a spike-oriented neural codec
**Confidence:** HIGH for the immediate repo-local execution slice; MEDIUM for optional GPU comparator follow-up

## User Constraints

- Honor the locked Phase 07 scope in `07-CONTEXT.md`: this phase hardens reproducibility and replay surface; it does not create new authority closure.
- Treat any `000055` / AJILE12 work as diagnostic unless fresh proof artifacts in this repo overturn the current family boundary.
- Prefer existing repo proof artifacts as the source for the first offline fixture slice; do not make large new downloads on this Mac the default execution path.
- Public replay commands must be explicit and reusable, but command availability by itself is not evidence.
- Keep KiloSort4 separate from the CPU/offline baseline. It is optional, GPU-only, and must not become the default validation path.
- Stay inside the repo surface and its declared contract. Missing anchors or stale reference locators must be surfaced explicitly, not silently hand-waved away.
- Project-level research files `.gpd/research/SUMMARY.md`, `METHODS.md`, and `PITFALLS.md` are absent, so Phase 07 planning has to build directly from repo artifacts, code, and the locked context.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` | benchmark | Current living DANDI Tier 1 positive anchor with selected-window metadata, codec metrics, NWB roundtrip `PASS`, and SpikeInterface `PASS` | read, compare, cite, preserve | plan, offline fixture manifest, bounded remote replay, verification |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_ajile12_sub01_ses7_ecephys.json` | benchmark | Current living AJILE / `000055` diagnostic artifact showing informative-window selection but downstream `FAIL` | read, compare, cite, preserve diagnostic role | plan, optional diagnostic replay, verification |
| `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ajile12_family_boundary_decision.md` | decision artifact | Current explicit `OUT_OF_FAMILY` decision that Phase 07 must not erode by narration | read, preserve, regression-check | plan, docs, optional diagnostic replay, verification |
| `.gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md` | prior phase summary | Defines the clean-env baseline and the still-open blind-clone gap that Phase 07 must not overclaim past | read, carry forward | plan, validation gates, docs |
| `../ZPE-Neuro_ACTION_BRIEF.md` | phase-definition artifact | Expands the workstream into reproducibility docs, fixture work, explicit replay commands, and bounded GPU comparator work | read, use, bound against contract | plan, execution, verification |
| `src/zpe_neuro/public_corpus.py` and `tools/run_public_corpus_eval.py` | implementation surface | Existing public-corpus harness already implements deterministic scan-policy replay; Phase 07 should extend this surface, not replace it | reuse, extend minimally | implementation plan, verification |
| `.github/workflows/verify-package.yml` | CI anchor | Existing workflow already owns package/build/test/gate/proof import verification; Phase 07 should extend it rather than add a redundant new workflow | extend, do not duplicate | implementation plan, verification |

**Missing or weak anchors:**

- `Ref-WAY-FORWARD` points to `docs/team_packet/07_WAY_FORWARD.md`, but that file is missing in this repo. Planning should flag this gap explicitly.
- The exact `state.json` locators for `Ref-DANDI-000034`, `Ref-AJILE12`, and `Ref-IBL-PROBE` still point at a missing `2026-03-20_zpe_neuro_repo_realignment` packet. The living equivalents are in `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/`.
- No project-level research summary exists, so there is no higher-level method memo to inherit from.

## Summary

Phase 07 should be executed as a packaging and honesty phase, not as a discovery phase. The repo already has the crucial ingredients: deterministic scan-policy logic in `src/zpe_neuro/public_corpus.py`, a repo-local CLI in `tools/run_public_corpus_eval.py`, a clean-env gate baseline from Phase 06, and committed proof artifacts from the March 21 refinement packet. What is missing is a durable replay surface that separates three different claims cleanly: offline selected-slice replay, bounded network-backed public replay, and optional GPU comparator work.

The smallest honest execution slice is therefore `07-01`: derive committed offline fixtures from the already-selected proof NWBs, add an offline verification path that reuses the same evaluator surface, and document explicit replay commands and artifact-root policy. That materially increases repo value now, avoids large downloads on this Mac, and makes the public-corpus path testable without pretending that an offline selected slice proves full-corpus scan reproducibility.

`07-02` should then add bounded remote replay ergonomics, mainly target selection and clearer diagnostic labeling, so `000034` can be replayed as the positive anchor while `000055` remains opt-in and diagnostic. `07-03` should remain isolated: a RunPod-only KiloSort4 installation/execution probe with full provenance, no CI integration, and no authority-closure language.

**Primary recommendation:** Reuse the current `run_public_corpus_eval` core, add a thin source/target selection layer plus fixture manifest support, and make offline selected-slice replay the first-class Phase 07 deliverable before any new network or GPU work.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Signal units | microvolts for waveform amplitudes | volts, raw integer counts | `.gpd/PROJECT.md`, `src/zpe_neuro/public_corpus.py` |
| Time indexing | zero-based half-open sample ranges `[start, start + sample_limit)` | closed ranges, one-based ranges | `.gpd/STATE.md`, `src/zpe_neuro/public_corpus.py` |
| Window policy default | `scan` | `first` | `src/zpe_neuro/public_corpus.py` |
| Candidate ranking | `event_count -> active_channels -> p95_abs_uv -> max_abs_uv -> earlier_start` | manual or random selection | `src/zpe_neuro/public_corpus.py` |
| Artifact placement | explicit repo-relative artifact root, usually via `--artifact-root` | implicit shared artifact root | `tools/run_public_corpus_eval.py`, Phase 06 summary |
| Family labeling | DANDI `000034` is the authority anchor; AJILE / `000055` is diagnostic and currently out-of-family | counting AJILE as breadth | `public_corpus_summary.json`, `ajile12_family_boundary_decision.md` |
| Replay claim boundary | offline fixture replay proves selected-slice reproducibility only; full scan-policy reproducibility still requires network-backed replay | treating fixture replay as full-corpus proof | Phase 07 context, current proof artifacts |

**CRITICAL:** All Phase 07 outputs should preserve the distinction between selected-slice fixture replay, network-backed full-corpus scan replay, and GPU comparator diagnostics. Mixing those three would create false progress.

## Mathematical Framework

### Key Equations and Starting Points

| Equation / Rule | Name / Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| `starts = linspace(0, total_samples - sample_limit, candidate_windows)` with edge inclusion and de-duplication | deterministic candidate start generation | `_candidate_window_starts` in `src/zpe_neuro/public_corpus.py` | defines how full-corpus remote scan replay chooses candidate windows |
| `rank_key = (event_count, active_channels, p95_abs_uv, max_abs_uv, -start_sample)` | deterministic candidate ranking tuple | `_window_candidate_payload`, `_candidate_rank_key` | defines selection reproducibility and fixture provenance |
| centered-and-clipped int16 conversion with optional normalization factor | waveform normalization surface | `_center_clip_to_int16` | fixture extraction and offline replay must preserve the same recording semantics |
| target `PASS` iff no failure reasons remain after codec, NWB roundtrip, and SpikeInterface checks | current evaluation contract | `run_public_corpus_eval` | Phase 07 must reuse this logic rather than inventing new replay verdicts |
| summary breadth counting excludes DANDI anchor and AJILE out-of-family control | adjudication boundary | `public_corpus_summary.json` | keeps diagnostic replays from being counted as new authority closure |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Provenance-preserving fixture extraction | turns existing proof NWBs plus sidecar metadata into stable committed offline fixtures | `07-01` | existing `gate_c_roundtrip.nwb` artifacts plus their JSON sidecars |
| Shared evaluator for local and remote sources | keeps offline and network replays comparable by reusing the same codec / roundtrip / SpikeInterface path | `07-01`, `07-02` | `src/zpe_neuro/public_corpus.py` |
| Target filtering | allows DANDI anchor replay without forcing AJILE diagnostic failure into the same top-level command | `07-02` | current CLI surface plus small wrapper extension |
| Artifact-root isolation | prevents proof collisions and keeps diagnostic work bounded | all plans | Phase 06 summary, existing `--artifact-root` support |
| Diagnostic labeling | records that `000055` and KiloSort4 work do not count toward lane closure | `07-02`, `07-03` | current family-boundary memo plus Phase 07 context |

### Approximation Schemes

| Approximation | Small Parameter / Bound | Regime of Validity | Error / Limitation | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| `sample_limit = 6000`, `channel_limit = 8` selected-window replay | bounded slice size | valid for current proof surface and replay packaging | does not prove larger-channel or full-recording behavior | separate larger-slice diagnostics, not Phase 07 baseline |
| committed offline fixture from selected proof NWB | selected-slice freeze | valid for offline reproducibility of the chosen slice | does not prove full remote scan-policy reproducibility | bounded remote replay against upstream DANDI |
| AJILE / `000055` diagnostic reuse | out-of-family negative-control role | valid as family-boundary regression check | not a counted breadth target | separate lane / second-mode research |

## Standard Approaches

### Approach 1: Fixture-Manifest Replay Layer Over The Existing Harness (RECOMMENDED)

**What:** Keep `run_public_corpus_eval` and its downstream evaluation logic as the source of truth. Add a thin layer that can load either a remote DANDI target or a committed local fixture, and allow target selection so the DANDI anchor and AJILE diagnostic can be replayed separately.

**Why standard:** This is the smallest extension that preserves comparability. The core logic for candidate-window scan, codec evaluation, NWB roundtrip, and SpikeInterface evaluation already exists. Replacing it would create unnecessary drift.

**Track record:** The current proof packet already proves the evaluator can distinguish the DANDI positive anchor from the AJILE diagnostic fail. Phase 07 should formalize that surface rather than rediscover it.

**Key steps:**

1. Define a fixture manifest schema that ties each committed local NWB slice to its source dataset id, asset path, selected start sample, expected role, and expected status.
2. Add a local-source loader that reconstructs a `Recording` from a fixture NWB while preserving the same metadata shape the remote path emits.
3. Add target filtering so `000034` can be replayed alone and `000055` can be run only as an explicit diagnostic command.
4. Keep artifact schemas aligned between remote and fixture modes so verification compares like with like.
5. Add docs and Make targets that clearly separate `offline fixture verify`, `remote DANDI replay`, and `diagnostic AJILE replay`.

**Known difficulties at each step:**

- Step 1: Provenance drift if the fixture is copied without a sidecar manifest. Prevent this by recording source JSON artifact path, original selected start sample, and fixture hash.
- Step 2: Semantic drift if the local fixture path bypasses the same downstream evaluator. Prevent this by reusing `_evaluate_recording` and `_run_target_insertion_evals`.
- Step 3: False failure if one command still runs both DANDI and AJILE. Prevent this by making target selection explicit.
- Step 4: Overclaim if fixture mode is described as “full replay.” Prevent this by naming it “selected-slice offline replay.”

### Approach 2: Thin `PublicCorpusRunner` Facade (FALLBACK)

**What:** Introduce a small wrapper class or manifest-driven façade that exposes `run_target(...)`, `run_fixture(...)`, and `run_remote(...)` while delegating all heavy work to the existing helper functions.

**When to switch:** Use this only if function parameters and CLI branching become hard to document or hard to test cleanly.

**Tradeoffs:** Better ergonomics and clearer documentation, but more code surface and a higher risk of accidental logic duplication. Do not move core selection/evaluation logic into the wrapper.

### Anti-Patterns to Avoid

- **Docs-only reproducibility:** writing `REPRODUCING.md` without a committed fixture and an automated offline test path.
  - _Example:_ a manual DANDI command exists, but no test can replay any corpus artifact offline.
- **Full-download-first design:** making a multi-GB DANDI download the default path on this Mac.
  - _Example:_ Phase 07 requires downloading full `000034` before any verification can run.
- **Diagnostic status collapse:** keeping AJILE diagnostic work in the default command so the “main replay command” exits nonzero for expected reasons.
  - _Example:_ `tools/run_public_corpus_eval.py` still always runs both targets and treats AJILE’s expected fail as the top-level verdict.
- **Comparator sprawl:** letting KiloSort4 installation or GPU specifics leak into `pyproject` extras, CI, or baseline docs.
  - _Example:_ adding CUDA-dependent steps to `verify-package.yml`.
- **Anchor substitution by narration:** silently using March 21 artifacts without noting that the March 20 reference locators and `07_WAY_FORWARD.md` are missing.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| DANDI selected-window anchor is a real positive `PASS` | `event_count = 41`, `peak_count = 34`, `nwb_roundtrip.status = PASS`, `status = PASS`, `selected_start_sample = 16871250` | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` | use as the positive benchmark and expected remote replay target |
| AJILE selected-window rerun is an informative diagnostic `FAIL` | `event_count = 3`, `peak_count = 0`, `sorter_probe_status = FAIL`, `status = FAIL`, `first_window_rank = 9`, `selected_start_sample = 20889595` | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_ajile12_sub01_ses7_ecephys.json` | use as the negative-control / family-boundary regression case |
| Family boundary is currently `OUT_OF_FAMILY` | explicit memo with `Confidence: medium` and `Status: PASS` | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ajile12_family_boundary_decision.md` | preserve wording and decision boundary in docs and outputs |
| Current breadth summary excludes DANDI and AJILE from counted breadth | DANDI role `tier1_authority_anchor`, AJILE role `out_of_family_control`, only IBL counted | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` | keep summary/counting logic from drifting when adding replay surface |
| Phase 06 clean-env baseline is sequential-only and still below blind-clone closure | fresh `.[gate,dev]` baseline passes unit slice plus Gate C/Gate D sequentially; parallel runs still collide | `.gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md` | keep replay-pack claims below blind-clone closure |
| Public harness already supports deterministic scan policy | `WINDOW_POLICY_CHOICES = ("first", "scan")` with selection artifacts emitted per target | `src/zpe_neuro/public_corpus.py` | extend minimally; do not reimplement scan logic |

**Key insight:** Phase 07 should package, expose, and verify the current proof surface. It should not spend effort rediscovering whether DANDI passes or whether AJILE is out-of-family unless a bounded replay is explicitly chosen to regression-check those already-known results.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| `gate_c_roundtrip.nwb` for DANDI selected slice | tiny committed NWB candidate for an offline fixture | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/dandi_000034_mouse412804_ecephys/gate_c_roundtrip.nwb` | valid for selected-slice offline replay only |
| `gate_c_roundtrip.nwb` for AJILE selected slice | tiny committed negative-control fixture | `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ajile12_sub01_ses7_ecephys/gate_c_roundtrip.nwb` | valid for diagnostic offline replay only |
| `public_corpus_window_selection_*` artifacts | stable selected start samples and candidate rankings | March 21 refinement packet | use to populate fixture provenance manifest |
| existing `verify-package.yml` workflow | current CI surface to extend | `.github/workflows/verify-package.yml` | do not create a second redundant CI workflow |

### Relevant Prior Work

| Paper / Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Phase 06 clean-env summary | repo-local prior phase | 2026 | defines reproducibility baseline and remaining blind-clone gap | keep replay-pack claims below blind-clone closure |
| March 21 refinement packet | repo-local prior phase | 2026 | provides living DANDI / AJILE artifacts and selected-window metadata | fixture provenance, expected statuses, proof packet layout |
| Revised action brief | repo-local owner brief | 2026 | adds offline fixture, replay docs, and bounded GPU comparator expectations | execution sequence and bounded optional work |

## Don't Re-Derive

- Do not reimplement candidate-window scan or ranking logic. Reuse the existing functions in `src/zpe_neuro/public_corpus.py`.
- Do not re-open the AJILE family boundary without a fresh executed proof artifact that actually overturns the current `OUT_OF_FAMILY` memo.
- Do not create a brand-new CI workflow when `verify-package.yml` already exists and can be extended.
- Do not make full DANDI downloads the default path. The existing remote streaming harness plus fixture path are enough for Phase 07.
- Do not redo IBL breadth work. Phase 07 is about replay surface and comparator isolation, not another breadth-closing search.

## Implementation Strategy

### Smallest Honest Execution Slice (`07-01`)

1. Create a stable fixture manifest from the March 21 DANDI and AJILE proof artifacts.
2. Commit tiny offline fixtures derived from the existing `gate_c_roundtrip.nwb` files.
3. Add a local fixture loader that feeds the same downstream evaluator used by remote replay.
4. Add offline integration tests that prove:
   - DANDI fixture replays through codec + NWB + SpikeInterface without network.
   - AJILE fixture remains diagnostic and does not turn into a counted pass.
   - no network-backed imports or DANDI API calls are required for fixture tests.
5. Add `REPRODUCING.md` and/or Make targets that make the three paths explicit:
   - offline selected-slice replay
   - remote DANDI anchor replay
   - optional AJILE diagnostic replay

**Why this first:** it adds immediate durable value, needs no large new download, and closes the biggest current gap: the repo has proof artifacts but no committed offline replay contract around them.

### Bounded Remote Replay (`07-02`)

1. Add target selection to the runner so `000034` can be replayed alone.
2. Keep remote replay on the existing streaming path; do not require full local corpus download by default.
3. Add explicit artifact-root examples and write replay outputs to a fresh isolated run directory.
4. If `000055` is replayed at all, make it a separate opt-in command and mark it diagnostic in both docs and artifacts.
5. Preserve current family-boundary labels and counted-breadth exclusion in any replay summary surface.

**Recommended rule:** The DANDI replay command should be able to exit `0` on its own. The AJILE diagnostic command may be expected to exit nonzero, and docs should say so plainly.

### Isolated GPU Comparator Probe (`07-03`)

1. Create a RunPod-only runbook or script that records pod id, image, CUDA version, Python env, commit SHA, and exact command log.
2. Probe KiloSort4 installation in a clean GPU environment first; only attempt a bounded run if install succeeds.
3. Use one known slice only. Do not expand into corpus breadth or large benchmark tables.
4. Record comparator outcome under a clearly separate artifact root and label it comparator-only.
5. Stop after one bounded success or one decisive failure record. Do not let this work dominate the phase.

## Computational Tools

### Core Tools

| Tool | Version / Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| `src/zpe_neuro/public_corpus.py` | repo module | source-of-truth public replay logic | already owns selection, loading, codec eval, and insertion checks |
| `tools/run_public_corpus_eval.py` | repo CLI | repo-local replay entrypoint | already exposes artifact-root and core replay parameters |
| `pynwb`, `h5py`, `remfile`, `dandi` | `.[public]` / `.[proof]` extras | remote NWB access and local NWB fixture loading | already declared by the repo |
| `spikeinterface`, `scikit-learn` | `.[gate]`, `.[public]`, `.[proof]` extras | downstream insertion/comparator surface | already part of current evidence path |
| `pytest` | `.[dev]` extra | automated offline verification | standard repo test mechanism |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| existing proof artifacts under `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/` | source for fixture extraction and expected-value manifests | `07-01` |
| `verify-package.yml` | CI anchor for package and replay-surface verification | `07-01` |
| RunPod SSH surface | bounded GPU comparator probe only | `07-03` |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| extending `verify-package.yml` | adding a new `.github/workflows/ci.yml` | duplicates CI and drifts from the existing package-verification authority surface |
| remote streaming plus target filtering | full `dandi download` workflow | simpler to explain, but wrong default for the current disk constraint and Phase 07 scope |
| fixture manifest plus shared evaluator | hand-written synthetic arrays | smaller tests, but weaker tie to the real proof surface |
| existing simple / tridesclous2 comparator baseline | immediate KiloSort4 integration | stronger headline, but violates the bounded optional comparator constraint |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| fixture extraction from existing proof NWBs | seconds, <1 MB of new committed bytes if copied | provenance bookkeeping, not compute | use sidecar manifest and hashes |
| offline fixture replay | local CPU, small | environment provisioning | add explicit `.[proof,dev]` or `.[public,dev]` instructions |
| bounded DANDI `000034` remote replay | moderate network I/O, no full dataset download required by default | network latency and DANDI availability | keep it manual / opt-in and isolated by target |
| optional AJILE `000055` remote diagnostic | moderate network I/O | expected downstream failure and nonzero exit | keep as separate diagnostic command |
| KiloSort4 probe | GPU-bound | CUDA env and dependency setup | RunPod only, bounded to one slice and one runbook |

**Installation / Setup:**

```bash
python -m pip install -e '.[dev]'
python -m pip install -e '.[proof,dev]'
python -m pip install -e '.[gate,dev]'
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| fixture manifest hash check | committed fixture really matches the claimed proof source | compute hash of fixture file and compare to manifest | exact match |
| shared-schema replay check | local fixture and remote replay use the same artifact contract | compare required JSON keys and role labels across both modes | schema parity |
| DANDI offline fixture replay check | selected-slice DANDI proof is replayable without network | run offline fixture test in a clean env | codec positive, NWB `PASS`, SpikeInterface `PASS` |
| AJILE offline diagnostic replay check | current family-boundary negative control is preserved | run offline diagnostic test on AJILE fixture | remains non-counted diagnostic and does not become a counted pass |
| artifact-root isolation check | replay commands do not collide with shared roots | run with explicit per-run roots | outputs land only in requested root |

### Known Limits and Benchmarks

| Limit / Benchmark | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| DANDI selected-window anchor | `sample_limit=6000`, `channel_limit=8`, `window_policy=scan` | `PASS`, selected start `16871250` | March 21 DANDI eval JSON |
| AJILE selected-window diagnostic | same bounded slice dimensions, 500 Hz recording | `FAIL`, selected start `20889595`, first window rank `9` | March 21 AJILE eval JSON |
| offline selected-slice replay boundary | committed selected window only | valid for slice replay, not for full-corpus scan proof | implied by fixture design |
| clean-env baseline boundary | `.[gate,dev]` sequential only | still below blind-clone closure | Phase 06 summary |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| DANDI fixture event count | replay fixture and inspect `codec_metrics.event_count` | exact or no-drift integer check | `41` |
| DANDI SpikeInterface peak count | replay fixture and inspect `spikeinterface.peak_count` | allow small tolerance only if backend drift is observed; otherwise exact | `34` |
| AJILE fixture failure signature | replay fixture and inspect status / peak count / family label | status-level exactness | `status = FAIL`, `peak_count = 0` |
| fixture provenance | compare manifest selected start / dataset id / asset path | exact | March 21 selection + eval artifacts |

### Red Flags During Computation

- The offline replay path passes, but it cannot be shown to avoid DANDI API or network access.
- A default replay command still evaluates AJILE and therefore reports overall `FAIL` when the user is only trying to replay the DANDI anchor.
- Phase 07 docs or summaries imply that a fixture replay proves full remote scan-policy reproducibility.
- Any replay update changes the current DANDI `PASS` or AJILE `OUT_OF_FAMILY` stance without a fresh proof artifact that clearly justifies it.
- KiloSort4 work starts changing package extras, baseline docs, or CI.

## Common Pitfalls

### Pitfall 1: Selected-Slice Fixture Overclaim

**What goes wrong:** The fixture becomes described as if it proves end-to-end remote corpus reproducibility.
**Why it happens:** The fixture is tiny and easy to run, so it is tempting to treat it as a full replay substitute.
**How to avoid:** Name it explicitly as a selected-slice fixture and keep full-scan replay as a separate remote step.
**Warning signs:** docs say “replay the DANDI dataset offline” instead of “replay the committed DANDI selected slice offline.”
**Recovery:** split the documentation and test names into `offline selected-slice` versus `remote scan replay`.

### Pitfall 2: Stale Anchor Locator Drift

**What goes wrong:** The phase is planned against `state.json` reference paths that no longer exist.
**Why it happens:** March 20 locators remain in the machine-readable contract, but the living packet is March 21.
**How to avoid:** call out stale locators in the research and planning artifacts, then either restore or update them during execution.
**Warning signs:** commands or docs refer to `2026-03-20_zpe_neuro_repo_realignment`, but the repo only contains March 21 packets.
**Recovery:** repair the contract reference or add an explicit substitution note in the phase artifacts.

### Pitfall 3: Diagnostic Failure Becomes Baseline Command Failure

**What goes wrong:** the only public replay command returns nonzero because it still includes AJILE by default.
**Why it happens:** current runner loops all targets and defines top-level success as all-target pass.
**How to avoid:** add explicit target selection and separate anchor replay from diagnostic replay.
**Warning signs:** user-facing docs tell people to run a command that predictably exits `1`.
**Recovery:** split commands by target role and document expected exit semantics.

### Pitfall 4: GPU Comparator Sprawl

**What goes wrong:** optional KiloSort4 work starts dictating package shape, CI, or scientific narrative.
**Why it happens:** GPU comparator work feels like an upgrade path and can attract too much scope.
**How to avoid:** keep it in a separate runbook, separate artifact root, and separate success criteria.
**Warning signs:** CUDA instructions appear in baseline install docs or GitHub Actions.
**Recovery:** move comparator work back into an isolated operator-only or proof-only surface.

## Level of Rigor

**Required for this phase:** controlled reproducibility evidence with explicit claim boundaries

**Justification:** Phase 07 is not a new-science phase. It is a surface-hardening phase that must preserve the current authority anchor, expose a real offline replay path, and isolate optional diagnostics without narrative drift.

**What this means concretely:**

- Offline tests must prove selected-slice replay works without network access.
- Remote replay docs must be executable and bounded, but they do not count as evidence until artifacts are produced.
- Any `000055` / AJILE work must preserve diagnostic labeling and current family-boundary logic.
- Any RunPod / GPU result must carry provenance and must not be counted as authority closure.
- Missing anchors must be surfaced explicitly in plan and summary artifacts.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| ad hoc proof packet without committed offline fixture contract | fixture-backed offline replay on committed selected slices | target for Phase 07 | makes the replay surface testable without large downloads |
| one runner that always evaluates both DANDI and AJILE | role-aware target selection for anchor versus diagnostic runs | target for Phase 07 | makes DANDI replay usable as a normal command |
| implicit KiloSort4 unavailability note in proof artifacts | explicit comparator-only RunPod runbook with provenance | target for Phase 07 | prevents GPU work from contaminating baseline claims |

**Superseded approaches to avoid:**

- Full-download-first public replay: wrong default for this machine and unnecessary for the first honest slice.
- New workflow proliferation: extending `verify-package.yml` is cleaner than adding a second CI surface.

## Open Questions

1. **Should `000055` remote replay be in-scope for execution or only documented?**
   - What we know: the current repo already contains a living AJILE diagnostic artifact and an explicit `OUT_OF_FAMILY` memo.
   - What's unclear: whether re-running the remote diagnostic adds enough value now to justify runner complexity in `07-02`.
   - Impact on this phase: affects whether `07-02` is required for closure or can remain optional/manual.
   - Recommendation: do not block `07-01` on `000055`; keep `000055` replay opt-in unless the execution phase can add target filtering cheaply.

2. **Where should the committed fixtures live?**
   - What we know: the current proof NWBs are tiny, about `260K` each.
   - What's unclear: whether the repo wants fixtures under `tests/fixtures/` or a proof-owned fixture directory.
   - Impact on this phase: affects test ergonomics and provenance documentation.
   - Recommendation: prefer `tests/fixtures/public_corpus/` plus a manifest that points back to the proof packet.

3. **Does Phase 07 need a new wrapper class?**
   - What we know: the brief mentions `PublicCorpusRunner`, but the repo currently uses functions and one CLI script.
   - What's unclear: whether adding source/target selection makes the current surface awkward enough to justify a wrapper.
   - Impact on this phase: affects code volume and documentation clarity.
   - Recommendation: start without a wrapper; add a thin façade only if argument sprawl becomes real during execution.

4. **How should the missing `Ref-WAY-FORWARD` be handled?**
   - What we know: the contract and receipts still reference `docs/team_packet/07_WAY_FORWARD.md`, but the file is absent.
   - What's unclear: whether it should be restored or replaced by a new explicit Phase 07 handoff artifact.
   - Impact on this phase: missing anchor weakens honest planning unless acknowledged.
   - Recommendation: make the gap explicit in the plan and, if cheap, repair the anchor as part of phase hygiene.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| shared source/target extension to `run_public_corpus_eval` | function surface becomes too awkward | thin `PublicCorpusRunner` façade that delegates to existing functions | low to medium |
| committing copied fixture files | repo prefers no byte duplication | keep fixtures under `proofs/selected_artifacts/` and commit only a stable manifest plus tests that reference them | low |
| bounded remote replay on the Mac | local network / disk / env constraints remain too awkward | RunPod remote replay with explicit provenance and no closure claim | medium |
| KiloSort4 install probe | GPU env still fails after one or two bounded strategies | stop and document failure signature plus working substitution | low |

**Decision criteria:** abandon the minimal in-repo approach only if extending the existing harness requires major logic duplication or if remote replay cannot be bounded without violating the current disk and honesty constraints.

## Sources

### Primary (HIGH confidence)

- `.gpd/phases/07-reproducible-open-corpus-replay-pack/07-CONTEXT.md` - locked Phase 07 decisions and must-read items
- `../ZPE-Neuro_ACTION_BRIEF.md` - revised phase brief and bounded GPU/replay scope
- `.gpd/PROJECT.md` - current contract, anchor registry, scope boundary
- `.gpd/REQUIREMENTS.md` - Phase 07 requirements and false-progress boundaries
- `.gpd/ROADMAP.md` - current phase decomposition and success criteria
- `.gpd/STATE.md` - current phase posture and recent decisions
- `.gpd/phases/06-blind-clone-authority-pack-baseline/06-01-SUMMARY.md` - clean-env baseline and blind-clone boundary
- `src/zpe_neuro/public_corpus.py` - live replay implementation and selection logic
- `tools/run_public_corpus_eval.py` - current repo-local replay entrypoint
- `.github/workflows/verify-package.yml` - current CI verification surface
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_dandi_000034_mouse412804_ecephys.json` - living DANDI anchor artifact
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_eval_ajile12_sub01_ses7_ecephys.json` - living AJILE diagnostic artifact
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_summary.json` - current counting and family-boundary summary
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/public_corpus_window_selection_*.json` - selected-window provenance for fixtures
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ajile12_family_boundary_decision.md` - current family-boundary memo

### Secondary (MEDIUM confidence)

- `README.md`, `docs/ARCHITECTURE.md`, `docs/LEGAL_BOUNDARIES.md` - current repo-surface description of packaged versus operator-only surfaces
- `runbooks/20260320T153824Z_codex_receipt.md` and `runbooks/20260321T022645Z_codex_receipt.md` - historical routing context and evidence references

### Tertiary (LOW confidence)

- None. No external web or literature search was used because the user explicitly constrained work to the repo surface and named local authoritative inputs.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - current replay logic and proof artifacts are concrete and local
- Standard approaches: HIGH - the minimal extension path is clear from the current implementation surface
- Computational tools: HIGH - package extras, scripts, and CI surface are already present
- Validation strategies: MEDIUM - the repo has no ready local pytest env at this moment, so validation recommendations are grounded in code and artifact structure rather than a fresh local rerun

**Research date:** 2026-04-05
**Valid until:** until the public-corpus runner surface, proof packet paths, or Phase 07 contract references materially change
