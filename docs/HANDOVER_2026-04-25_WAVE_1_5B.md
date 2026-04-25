# ZPE-Neuro Handover - 2026-04-25 Wave 1.5b

> **STATUS UPDATE — 2026-04-25 archaeology+resolve pass:**
> PR `#36` merged at `8a7da6f` (2026-04-25T17:20:39+02:00). Blind-clone replay artifacts are now on `origin/main`
> under `proofs/selected_artifacts/2026-04-24_zpe_neuro_blind_clone_replay/`. The constraints in §2, §7, §13, and §15
> that say "do not claim main already reflects April 24 authority replay" are NOW OBSOLETE. They were correct at the
> time of writing; they no longer apply. PR `#39` is also merged. The governing state is `origin/main` at
> `0f9cf7d` or later. HF recovery routes in §10 (`Architect-Prime/zpe-neuro-artifacts`,
> `Architect-Prime/zpe-neuro-lane-archive`) remain valid anchors.

This document is the current handoff for a successor agent. It is written from branch `chore/wave-1-5b-investor-readiness-2026-04-25` at commit `c51811a50e2c603d0d203fe6b72f0511558b6408`.

## 1. Executive State

ZPE-Neuro currently has two relevant open PRs:

- PR `#39`: `chore(neuro): Wave 1.5b investor-readiness hardening`
  - branch: `chore/wave-1-5b-investor-readiness-2026-04-25`
  - status: open, not draft
  - head: `c51811a50e2c603d0d203fe6b72f0511558b6408`
  - URL: <https://github.com/Zer0pa/ZPE-Neuro/pull/39>
- PR `#36`: `Authority replay closure and DANDI 000003 breadth for ZPE-Neuro`
  - branch: `codex/neuro-authority-replay-2026-04-23`
  - status: open, not draft
  - head: `6f6a61a86de736d72a3beec307fe5b77be031875` on origin
  - URL: <https://github.com/Zer0pa/ZPE-Neuro/pull/36>

Current `origin/main` is:

- branch: `main`
- head: `dec2f8beab8df7db59d7b202b97a7a770ed1b3de`
- commit subject: `h1 lane hygiene neuro (#35)`

## 2. Governing Distinction

Do not conflate the two open PRs.

PR `#39` is investor-readiness hardening on top of the current mainline March 21 authority surface. It fixes CI, hardens packaging metadata, removes README drift, and removes dead repo clutter.

PR `#36` is separate. That branch contains the April 24 authority-replay and DANDI `000003` breadth work. It is not merged. Until PR `#36` is merged, the repo front door on main remains the narrower March 21 authority posture.

That distinction matters. A new agent must not claim that main already reflects April 24 authority truth. It does not.

## 3. What PR #39 Changed

PR `#39` contains exactly these material changes relative to current `origin/main`:

1. `README.md`
   - pruned to proof-plus-CI-backed claims only
   - removed unsupported commercial-readiness block
   - removed encoding KV row
   - removed IBL metric promotion and second-target breadth promotion
   - removed competitive benchmark section
   - removed proof-anchor table
   - removed front-door PyPI install claim
   - retained bounded DANDI `000034`, Gate C, Gate D, and AJILE out-of-family claims because those are tied to tracked artifacts and CI coverage

2. `pyproject.toml`
   - build backend pin changed from `setuptools>=68` to `setuptools>=68,<82`
   - removed deprecated classifier `License :: Other/Proprietary License`
   - removed dead optional dependency group `ops`
   - kept project URLs, version, and SAL license expression intact

3. `.github/workflows/auto-add-to-project.yml`
   - added:
     - `if: ${{ vars.ENABLE_PROJECT_AUTOMATION == 'true' }}`
   - reason: the project-board automation was failing on PR open with `Bad credentials` against `secrets.ADD_TO_PROJECT_PAT`
   - this converts the external org-project integration into explicit opt-in infra instead of hard-failing lane PRs by default

4. Deleted drift
   - `proofs/artifacts/dandi000055_benchmark/`
   - `proofs/manifests/PROOF_SELECTION_2026-03-09.md`
   - `tools/log_comet_run.py`

## 4. Why Those Deletions Were Safe

### `proofs/artifacts/dandi000055_benchmark/`

This was an unreferenced benchmark artifact folder with no active callers or routing.

### `proofs/manifests/PROOF_SELECTION_2026-03-09.md`

This was a historical note explicitly superseded by `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`.

### `tools/log_comet_run.py`

This was an abandoned Comet helper with no repo callers. Removing it also made the `ops` extra dead and removable.

## 5. CI State Before And After PR #39

### Failing on `origin/main` before the fix

The failures on main were:

- `offline-verify / test (3.11)`
- `Verify Package Surface / build-and-core`
- `Verify Package Surface / gate-slice`
- `Verify Package Surface / proof-import-smoke`
- `Auto-add to project board`

Root cause for the package/test failures was the deprecated PEP 639-incompatible classifier in `pyproject.toml`:

- `License :: Other/Proprietary License`

That caused editable install and build failures in the CI jobs before tests even ran.

The project-board workflow failure was unrelated to package/test correctness. It was:

- `Bad credentials - https://docs.github.com/rest`

### Current status on PR `#39`

Passing checks:

- `Analyze (actions)`
- `Analyze (python)`
- `CodeQL`
- `offline-verify / test (3.11)`
- `build-and-core`
- `gate-slice`
- `proof-import-smoke`

Skipped by design:

- `offline-verify / lint`
- `offline-verify / type-check`

The original `Auto-add to project board` failure belongs to an earlier run on PR open. The workflow has now been gated behind `vars.ENABLE_PROJECT_AUTOMATION == 'true'`, so future open events will not hard-fail unless the owner explicitly enables the integration.

## 6. Local Verification Performed On PR #39

All of the following were run successfully on the branch while preparing PR `#39`:

```bash
python3.11 -m venv .venv-wave15b
source .venv-wave15b/bin/activate
python -m pip install --upgrade pip build
python -m pip install -e '.[dev]'
python -m build
python -m pytest tests
python tools/run_gate_c.py --artifact-root artifacts/ci_gate_surface --seed 20260220
python tools/run_gate_d.py --artifact-root artifacts/ci_gate_surface --replay-seeds 20260220,20260221,20260222,20260223,20260224
python - <<'PY2'
import h5py
import remfile
from dandi.dandiapi import DandiAPIClient
from pynwb import NWBHDF5IO
import spikeinterface
print('proof import surface ok')
PY2
```

Observed outcomes:

- `python -m build`: PASS
- `pytest tests`: `25 passed`
- Gate C: PASS
- Gate D: PASS
- proof import surface: PASS
- project URLs in `pyproject.toml`: `5 / 5` returned `HTTP 200`

## 7. Current README / Authority Posture

Current branch README is intentionally narrower than the broader authority packet. It now promotes only these front-door claims:

- DANDI `000034` bounded slice metrics and artifact
- Gate C `PASS`
- Gate D `PASS`
- AJILE out-of-family / excluded from breadth

It explicitly does **not** claim:

- blind-clone replay closure
- commercialization-safe closure
- tagged public release
- second-target breadth closure
- broader lane expansion

Again: that is only the README surface for PR `#39`. The broader April 24 authority replay and DANDI `000003` breadth work remain on PR `#36`.

## 8. What PR #36 Is

PR `#36` is the still-open authority branch:

- title: `Authority replay closure and DANDI 000003 breadth for ZPE-Neuro`
- branch: `codex/neuro-authority-replay-2026-04-23`
- URL: <https://github.com/Zer0pa/ZPE-Neuro/pull/36>

Per its PR body, it is intended to:

- close the blind-clone authority replay from current repo truth
- add the first in-family DANDI `000003` breadth execution
- record the truthful `FAIL` for that breadth target
- update front-door authority routing to the April 24 truth

Important current status:

- PR `#36` predates the Wave 1.5b hardening fixes
- its current CI status is red on the same package/install jobs that were failing on old main before PR `#39`
- this means a successor agent should expect to rebase or forward-port the PR `#39` fixes into PR `#36` after PR `#39` merges, or otherwise reconcile the two branches

Do not close PR `#36` as duplicate. It carries materially different content not yet on main.

## 9. Recommended Next Actions

The cleanest next sequence is:

1. Owner reviews and merges PR `#39`.
2. After PR `#39` lands, rebase PR `#36` onto the new `main`.
3. Re-run CI on PR `#36`.
4. Reconfirm that PR `#36` still only contains the authority replay / DANDI `000003` breadth / routing work and not unrelated investor-readiness drift.
5. Continue from there.

If asked to continue immediately without waiting for merge, the next agent should work on PR `#36`, but must account for the fact that `main` does not yet include the Wave 1.5b hardening commits.

## 10. Cold Start / Recovery Context

If a future agent is starting from scratch or from a deleted local lane, there is a separate custody/restart branch:

- branch: `codex/neuro-restart-custody-2026-04-24`
- head: `5c49fab097a07a4dd25db68a80c584f4ebdd3e1a`

That branch includes:

- `docs/custody/2026-04-24/startup_prompts/ZPE-Neuro_STARTUP_PROMPT_2026-04-24.md`
- `docs/custody/2026-04-24/remote_state_manifest.json`

It also points to the verified Hugging Face recovery route used during custody:

- `Architect-Prime/zpe-neuro-artifacts`
- `Architect-Prime/zpe-neuro-lane-archive`

That route is relevant for recovery and archived large artifacts, not for the Wave 1.5b packaging/CI fixes themselves.

## 11. Read-In Order For A New Agent

If the new agent starts from PR `#39`, read in this order:

1. this file
2. PR `#39` body
3. `README.md`
4. `pyproject.toml`
5. `.github/workflows/auto-add-to-project.yml`
6. `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
7. PR `#36` body
8. `git log --oneline --decorate -8`

If the new agent starts cold from recovery, read in this order:

1. `docs/custody/2026-04-24/startup_prompts/ZPE-Neuro_STARTUP_PROMPT_2026-04-24.md` on branch `codex/neuro-restart-custody-2026-04-24`
2. `docs/custody/2026-04-24/remote_state_manifest.json` on the same branch
3. this file
4. PR `#39`
5. PR `#36`

## 12. Resume Commands

### Resume PR `#39`

```bash
git clone --branch chore/wave-1-5b-investor-readiness-2026-04-25 https://github.com/Zer0pa/ZPE-Neuro.git
cd ZPE-Neuro
git status --short --branch
gh pr view 39 --repo Zer0pa/ZPE-Neuro
gh pr checks 39 --repo Zer0pa/ZPE-Neuro
```

### Resume PR `#36`

```bash
git fetch origin codex/neuro-authority-replay-2026-04-23
git switch -c authority-replay origin/codex/neuro-authority-replay-2026-04-23
gh pr view 36 --repo Zer0pa/ZPE-Neuro
gh pr checks 36 --repo Zer0pa/ZPE-Neuro
```

### Rebuild local verification env

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest tests
```

### Full package / proof / gate verification

```bash
python -m pip install -e '.[dev,public,proof,gate]'
python -m build
python tools/run_gate_c.py --artifact-root artifacts/manual_gate_c --seed 20260220
python tools/run_gate_d.py --artifact-root artifacts/manual_gate_d --replay-seeds 20260220,20260221,20260222,20260223,20260224
```

## 13. Things The Next Agent Should Not Re-Decide

- Do not reintroduce README claims unless they are backed by both tracked proof and CI coverage.
- Do not resurrect the deleted Comet helper or the `ops` extra.
- Do not remove the `setuptools<82` upper bound unless you test it.
- Do not claim that main already reflects the April 24 authority replay.
- Do not present the DANDI `000003` breadth result as a pass.
- Do not remove the project-board gating unless the owner intentionally restores working org-project credentials and wants the workflow live by default.

## 14. Current Cleanliness

At the time of writing this handover:

- branch: `chore/wave-1-5b-investor-readiness-2026-04-25`
- head: `c51811a50e2c603d0d203fe6b72f0511558b6408`
- worktree: clean before adding this handover document
- PR `#39`: open and ready for review
- PR `#36`: open and still needs reconciliation after `#39`

## 15. Bottom Line

If a new agent needs the shortest accurate summary:

- PR `#39` is the current investor-readiness hardening branch and is green.
- PR `#36` is the still-open authority replay / DANDI `000003` branch and remains separate.
- Merge `#39` first, then rebase and continue `#36`.
