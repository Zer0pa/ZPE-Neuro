# ZPE-Neuro Novelty Card

**Product:** ZPE-Neuro  
**Domain:** Deterministic encoding of extracellular spike-event recordings and bounded replay packets  
**What we sell:** Reproducible extracellular spike-event encoding, replay, and audit lineage for neuroscience infrastructure teams

## Novel contributions

1. **Deterministic spike-event token stream codec** — ZPE-Neuro turns each channel into a compact token stream with explicit skip (`S`) and pulse (`P`) tokens, fixed 40-sample windows, 5-bit template identifiers, 8-bit amplitude quantization, and deterministic decode back into waveform-aligned windows. The codec keeps encoded bit counts and overlap drops explicit inside the packet instead of hiding them in an external transport layer. Code: `src/zpe_neuro/wave1.py:321-405`. Nearest prior art (if known): standard run-length coding, spike-template pipelines, and amplitude quantization. What is genuinely new here: the specific packet contract for bounded extracellular replay, with deterministic event ordering, fixed-window reconstruction, and codec-accounted bit totals tied directly to the retained proof surface.
2. **Bounded public-corpus replay measurement contract** — The public replay surface evaluates the same codec contract against retained extracellular corpora and records event counts, encoded bits, compression ratio, RMSE, timing, fidelity, and overlap-drop behavior from one runner path. Code: `src/zpe_neuro/public_corpus.py:601-663`. Nearest prior art (if known): generic dataset benchmark harnesses. What is genuinely new here: the way ZPE-Neuro binds the codec packet, waveform reconstruction metrics, and retained authority artifacts into a single reproducible extracellular evaluation surface rather than a loose benchmark script.

## Standard techniques used (explicit, not novel)

- Run-length gaps
- Quantized amplitude buckets
- Template banks and template matching
- Deterministic sort/order of encoded events
- RMSE and timing measurements
- NWB / PyNWB packaging and replay
- SpikeInterface-based downstream evaluation

## Compass-8 / 8-primitive architecture

NO — the shipped codec surface here is a spike-event token stream over fixed waveform windows, not a Compass-8 directional encoder. Current implementation: `src/zpe_neuro/wave1.py:321-405`.

## Open novelty questions for the license agent

- Does the bounded breadth-adjudication layer belong in the novelty schedule, or should the schedule stay limited to the codec packet and replay contract? Relevant code: `src/zpe_neuro/breadth_adjudication.py:80-107`.
- Should the fixed template-bank construction itself be claimed as novel, or only the token-stream packet plus deterministic decode contract? Relevant code: `src/zpe_neuro/wave1.py:145-173`, `src/zpe_neuro/wave1.py:321-405`.
