<p>
  <img src=".github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src=".github/assets/readme/section-bars/before-you-start.svg" alt="BEFORE YOU START" width="100%">
</p>

ZPE-Neuro is private-first and evidence-first. Contribute against the repo's
current truth, not against a hoped-for release state.

Read these first:
- `README.md`
- `proofs/manifests/CURRENT_AUTHORITY_PACKET.md`
- `docs/ARCHITECTURE.md`
- `PUBLIC_AUDIT_LIMITS.md`
- `docs/LEGAL_BOUNDARIES.md`

<p>
  <img src=".github/assets/readme/section-bars/setup-and-verification.svg" alt="SETUP AND VERIFICATION" width="100%">
</p>

Baseline environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -c "import zpe_neuro"
```

Shipped repo-local checks:

```bash
python -m pip install -e '.[dev]'
python -m pytest tests
```

Optional clean repo-local execution surfaces:

```bash
python -m pip install -e '.[gate,dev]'
python -m pip install -e '.[public]'
python -m pip install -e '.[proof]'
```

`tools/` runners require a checkout. Use `--artifact-root` when you need an
isolated output tree or when comparing reruns.

Operator-only paths:
- IBL metadata/chunked-waveform tooling
- bounded IBL refinement runners
- Allen parity runners

If you work on those paths, record the exact manual dependency and toolchain
setup because they are not currently claimed as clean packaged extras.

<p>
  <img src=".github/assets/readme/section-bars/pr-process.svg" alt="PR PROCESS" width="100%">
</p>

Every pull request should state:
- what changed
- what did not change
- which claim or runtime surface moved
- which evidence or rerun supports the change
- which open gaps remain

If a doc changes a status word, the evidence path must change with it.

<p>
  <img src=".github/assets/readme/section-bars/scope-discipline.svg" alt="SCOPE DISCIPLINE" width="100%">
</p>

Do:
- keep prose subordinate to code and proof artifacts
- preserve negative and inconclusive evidence
- name historical versus current surfaces explicitly
- route readers back to canonical docs instead of duplicating claims

Do not:
- borrow ZPE-IMC claims, metrics, or proof posture
- point the front door at ignored local-only artifacts
- hardcode machine-specific paths as current instructions
- upgrade private staging into public-release language without evidence
