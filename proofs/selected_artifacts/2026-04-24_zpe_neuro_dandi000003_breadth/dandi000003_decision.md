# DANDI 000003 Decision

- Target: `dandi_000003_yutamouse20_ecephys`
- Verdict: `FAIL`
- Counted in breadth: `true`

## Failure basis

The first DANDI `000003` breadth probe failed because the sampled NWB assets in
this pass returned:

- `NO_ELECTRICAL_SERIES_FOUND`

Attempted asset paths in the machine-readable artifact:

- `sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140327_behavior+ecephys.nwb`
- `sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140321_behavior+ecephys.nwb`

The code now supports a broader sampled asset list for `000003`, but this pass
did not produce a successful compatible extracellular slice. The truthful lane
state therefore remains:

- blind-clone replay closed
- DANDI `000034` anchor preserved
- IBL counted breadth preserved
- DANDI `000003` breadth still open
