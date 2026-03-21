# Lane 1 Wedge Recommendation

- Decision: `LOCK_TO_EXTRACELLULAR_AUTHORITY_WEDGE`
- Confidence: `medium`
- Status: `FAIL_FORWARD`

## Recommended Wedge

Lane 1 should be locked to a narrower extracellular research-infrastructure wedge: a spike-oriented codec and insertion path anchored on the validated DANDI `000034` public NWB pass, with NWB as the clean authority surface and SpikeInterface-style downstream compatibility treated as supportable only where the evidence is real.

## Why This Is The Strongest Honest Recommendation

- DANDI `000034` remains the only positive public authority anchor. The selected-window rerun stayed `PASS` with 41 codec events, 34 detected peaks, and bit-consistent NWB roundtrip output.
- AJILE12 is now explicitly `OUT_OF_FAMILY` for the current Lane 1 codec. Its informative slice still produced only 3 codec events at 500 Hz, 0 detected peaks, and final `FAIL`.
- IBL KS014/probe00 now proves a second extracellular-style waveform path exists locally, but the bounded slice still failed downstream with 0 detected peaks and `SPIKEINTERFACE_FAIL`, so counted breadth remains open.
- The carried-forward breadth summary is still `FAIL`: one counted extracellular breadth target exists and it currently fails, while the DANDI anchor stays positive but singular.

## What Lane 1 Should Include

- extracellular waveform authority anchored on the DANDI public insertion pass
- NWB-first insertion and preservation claims that trace to the existing proof packet
- explicit fail-forward language that keeps IBL as an unresolved breadth blocker rather than hiding it

## What Lane 1 Should Not Claim

- general public-corpus breadth closure
- human intracranial or broader neural-signal coverage
- public release readiness
- commercialization clearance or Allen parity

## Implication For Lane Structure

Broader human or intracranial neural coverage should sit outside Lane 1 unless a second representation mode is added. The Phase 4 decision is therefore a scope lock, not a gate close: keep the first lane narrow, extracellular, and authority-first.

## Optional Strengthening Path

A bounded local IBL downstream refinement pass is allowed as follow-on work because it can strengthen the extracellular wedge. It is not allowed to rewrite the current status: breadth is still open today, and the Phase 4 recommendation does not depend on narrating IBL as already solved.
