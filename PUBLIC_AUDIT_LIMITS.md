# Public Audit Limits

This file exists to stop over-reading the staged repo.

## Current Boundary

This repository is a private staging repo pushed on 2026-03-09. It is cleaner than the outer workspace, but it is not yet the final verification authority surface.

## Hard Limits

- No blind-clone verification has been completed from this repo yet.
- No broad retest campaign was run as part of staging.
- The proof corpus here is curated, not exhaustive.
- Some preserved proof artifacts still contain historical absolute paths from the original workspace.
- Commercialization is not closed. Allen parity remains an open risk surface.

## Specific Contradictions Still Present

- `NEU-C007`: summary `PASS` versus shipped `INCONCLUSIVE` sorter evidence
- Gate D: summary `PASS` versus shipped `DT-NEU-5 - FAIL`
- commercialization: scorecard `PASS` versus risk and board `OPEN`

## Correct Reading

Use this repo to inspect the package surface, the curated proof subset, and the current contradiction map.

Do not use this repo alone to claim:

- public release readiness
- clean portability
- full external-corpus reproducibility
- commercialization clearance
