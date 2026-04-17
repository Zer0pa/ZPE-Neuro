# Reorientation Open Questions — 2026-04-17

- Novelty-schedule boundary: I treated the codec packet and replay contract as the clearest novelty surface, but I am not certain whether the breadth-adjudication layer should also be scheduled as novel. I checked `src/zpe_neuro/wave1.py`, `src/zpe_neuro/public_corpus.py`, and `src/zpe_neuro/breadth_adjudication.py`; this needs the license agent's judgment, not a repo-doc guess.
- Template-bank scope: the fixed waveform template bank is central to the implementation, but I could not justify from repo evidence alone whether it is independently novel or just part of the broader codec. I traced it to `src/zpe_neuro/wave1.py:145-173` and left the question open for the license pass.
