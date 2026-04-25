# 2026-04-24 ZPE-Neuro DANDI 000003 Breadth Probe

This packet records the first next-family DANDI breadth attempt after
blind-clone replay closure.

## Decisive outcomes

- DANDI `000034` replay anchor -> `PASS`
- AJILE control -> `FAIL` and remains out of family
- carried IBL counted breadth target -> `PASS`
- DANDI `000003` first in-family breadth probe -> `FAIL`

## Why DANDI `000003` failed

The sampled `000003` NWB assets used in this pass did not expose a compatible
`ElectricalSeries` surface through the current loader path. The failure was
captured directly in the machine-readable eval artifact instead of being
narrated away.

## Key files

1. `public_corpus_summary.json`
2. `dandi000003_decision.md`
3. `public_corpus_eval_dandi_000003_yutamouse20_ecephys.json`
4. `public_corpus_eval_dandi_000034_mouse412804_ecephys.json`
5. `public_corpus_ibl_waveform_eval.json`
6. `ajile12_family_boundary_decision.md`
