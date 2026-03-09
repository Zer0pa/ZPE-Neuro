# Contributing

This repo is private-first and evidence-first.

## Before You Start

- Read `README.md`
- Read `docs/ARCHITECTURE.md`
- Read `PUBLIC_AUDIT_LIMITS.md`
- Read `proofs/README.md`

## Baseline Rules

- Keep scope tight
- Preserve negative and inconclusive results
- Do not remove contradiction evidence without a replacement artifact
- Do not treat private staging as publish-ready by default

## Environment

Core path:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

Optional proof dependencies:

```bash
python -m pip install -e '.[proof]'
```

## Pull Request Expectations

- explain what changed
- explain what did not change
- include evidence when behavior changes
- call out any remaining contradictions explicitly

## What Not To Submit

- cosmetic claim inflation
- proof deletions without justification
- machine-specific path hardcoding
- public-release assumptions without verification evidence
