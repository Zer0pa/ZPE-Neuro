# IBL Refinement Decision

Bounded IBL refinement found a counted second extracellular target `PASS`.

## Best Candidate
- chunk index: `732`
- channel span: `128:136`
- window start within chunk: `12000` samples
- codec events: `110`
- SpikeInterface peak count: `120`
- evaluation status: `PASS`
- artifact: `candidates/ibl_ks014_2019_12_03_probe00_ap__chunk0732_ch128_w12000.json`

## Interpretation
- The bounded search preserved the existing downstream contract: same codec, same NWB roundtrip requirement, same SpikeInterface path.
- The search broadened only chunk choice, channel window, and representative slice selection.
- Final verdict: `PASS`.

## Next Step
Rerun breadth adjudication and update lane state surfaces without weakening the remaining blind-clone, Allen, or release-boundary gates.
