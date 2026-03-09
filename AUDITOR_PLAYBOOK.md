# Auditor Playbook

This is the shortest honest audit path for the current private staging snapshot of ZPE-Neuro.

It is not a public-release verification packet and it is not a substitute for Phase 5 clean-room validation.

## Shortest Audit Path

1. Clone the private repo:

```bash
git clone https://github.com/Zer0pa/ZPE-Neuro.git
cd ZPE-Neuro
```

2. Install the core package:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

3. Run the lightweight shipped tests:

```bash
python -m unittest discover -s tests -v
```

4. Read the current contradiction surfaces:

- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/neuro_spikeinterface_e2e.json`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/falsification_results.md`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/commercialization_risk_register.md`
- `proofs/selected_artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated/handoff_manifest.json`

5. Read the selection note:

- `proofs/manifests/PROOF_SELECTION_2026-03-09.md`

## What This Audit Path Proves

- the staged repo has a coherent package surface
- lightweight tests exist and can be run
- the proof subset is present and readable
- unresolved contradictions are surfaced explicitly

## What This Audit Path Does Not Prove

- full clean-room portability
- full optional proof-stack replay
- fresh external corpus access
- commercialization closure
- public-release readiness

Read `PUBLIC_AUDIT_LIMITS.md` before treating any staged result as broader truth.
