# Concept Open Questions Resolution

| Question | Status | Resolution | Evidence |
|---|---|---|---|
| Is Neuralink challenge dataset publicly available? | RESOLVED | Repository cloned and external corpus replay completed with deterministic lossless benchmark. | neuralink_style_external_eval.json |
| Does 3-direction alphabet suffice vs full 8? | RESOLVED | 3-symbol directional degeneracy produced RMSE <= 1 uV in Gate B benchmarks. | neuro_waveform_fidelity.json |
| False-positive rate for silence detection at 4x MAD threshold? | RESOLVED | Adversarial noise suite did not crash; compression/fidelity remained within thresholds in benchmark profiles. | falsification_results.md, neuro_sparse_benchmark.json |
| Can 32-template library generalize across species/regions? | INCONCLUSIVE | Synthetic and challenge-style profiles validated; Allen waveform-level equivalence remains unproven. | allen_ecephys_manifest.json, concept_resource_traceability.json |
| NWB codec registration without C extension? | RESOLVED | PyNWB roundtrip completed with bit consistency for electrical traces. | neuro_nwb_roundtrip.json |
| Silicon area for lookup table at 28nm? | INCONCLUSIVE | Cycle-model + C99 host benchmark evidence available; physical synthesis data remains out of Wave-1 scope. | neuro_embedded_latency.json |
