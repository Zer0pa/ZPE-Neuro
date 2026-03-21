# Repo Technical Alignment Execution Plan

Date: 2026-03-21
Lane: ZPE Neuro
Workspace: /Users/Zer0pa/ZPE/ZPE Neuro
Repo: /Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro
Instruction Surface:
- /Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro/runbooks/REPO_TECHNICAL_ALIGNMENT_EXECUTION_PROMPT.md
- /Users/Zer0pa/ZPE/ZPE Neuro/ZPE-Neuro/runbooks/REPO_TECHNICAL_EXECUTION_SUPPLEMENT.md

## Scope

Treat `ZPE-Neuro` as a standalone Python package with script-driven gate
harnesses and bounded public-corpus replay surfaces. Align package, extras,
verification entry points, and release automation to the truthful install and
execution boundary without implying full blind-clone or public-release closure.

## Execution Steps

1. Inspect `pyproject.toml`, package imports, tools, tests, and `.github`
   workflows to classify the actual package and release shape.
2. Identify contradictions between base install, optional proof and gate
   surfaces, script entry points, and workflow claims.
3. Implement the minimum technically correct fixes to packaging metadata,
   extras, workflow commands, and technical runbooks so install and release
   surfaces are truthful.
4. Falsify the result by building distributions, installing from a clean
   environment, verifying imports and extras, running the relevant tests and
   gate commands, and statically checking workflow logic.
5. Write a repo-local receipt with exact evidence paths and verdict language
   that does not overstate readiness.
