# 2026-04-24 ZPE-Neuro Blind-Clone Replay

This packet records a clean replay from current `origin/main` truth at commit
`950f03706237bdf71612827fe8fc5200687b7681`.

## Decisive outcomes

- `pytest tests` -> `PASS`
- Gate C -> `PASS`
- Gate D -> `PASS`
- DANDI `000034` replay anchor -> `PASS`

## Important boundary

The repo-local `public_corpus_summary.json` in this replay packet is `FAIL`
because AJILE remains an out-of-family control in the current lane. That does
not invalidate the blind-clone replay gate, which was satisfied by:

- clean environment build from declared surfaces
- repo-local tests
- Gate C
- Gate D
- DANDI `000034` replay

## Key files

1. `verification_summary.md`
2. `env_manifest.json`
3. `pytest_output.txt`
4. `gate_c_summary.json`
5. `gate_d_summary.json`
6. `public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
7. `public_corpus_window_selection_dandi_000034_mouse412804_ecephys.json`
