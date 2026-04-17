# Open Dataset Surfaces

Verified on 2026-04-06 for the next public-corpus breadth surfaces named in the
action brief.

## Current Reading

This register does not upgrade the current lane claim by itself. It classifies
which public datasets are easiest to add next without drifting beyond the
current extracellular lane.

| Dataset | Official surface | Format | Lane fit | Recommended status |
|---|---|---|---|---|
| Allen Brain Observatory Visual Coding Neuropixels | AllenSDK `EcephysProjectCache`; Allen Brain Map API direct download fallback | NWB | `IN_FAMILY`, but operator-only today | high-value next extracellular target once `allensdk` dependency conflict is isolated |
| IBL Brain Wide Map / public IBL corpus | ONE remote/local modes; Alyx-backed public data access | ONE / ALF / NWB-adjacent waveform surfaces | `IN_FAMILY`, but operator-only today | keep as an operator path and benchmark route, not a packaged extra |
| DANDI `000003` | DANDI archive draft dandiset | NWB | `IN_FAMILY` | easiest next DANDI breadth target because the current repo already handles DANDI + NWB |
| DANDI `000005` | DANDI archive draft dandiset | NWB | `OUT_OF_LANE` for the current codec | keep as a challenge corpus, not a counted extracellular breadth target |
| OpenNeuro EEG datasets | OpenNeuro browser + CLI/DataLad/git-annex download surfaces | BIDS / EEG / EDF | `OUT_OF_LANE` for the current codec | useful only as a future second-mode lane, not current breadth evidence |

## Verified Surfaces

### Allen Brain Observatory Visual Coding Neuropixels

- Official docs describe the dataset as high-density extracellular Neuropixels
  recordings available as NWB files through AllenSDK.
- Primary access surface:
  `allensdk.brain_observatory.ecephys.ecephys_project_cache.EcephysProjectCache`
- Allen docs also keep a direct download route through `api.brain-map.org` for
  users who cannot rely on AllenSDK-managed transfers.
- Current repo posture: operator-only, because `allensdk` still conflicts with
  the package floor declared in `pyproject.toml` and documented in
  `docs/ARCHITECTURE.md`.
- Sources:
  - https://allensdk.readthedocs.io/en/stable/visual_coding_neuropixels.html
  - https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_data_access.html

### IBL Brain Wide Map / public IBL corpus

- Official ONE docs describe both remote and local modes for public data access.
- This remains in-family for extracellular waveform work, but the repo should
  keep it operator-only until the `ONE-api` / `ibl-neuropixel` / upstream
  toolchain story is cleaner.
- Source:
  - https://int-brain-lab.github.io/ONE/notebooks/one_modes.html

### DANDI `000003`

- Live DANDI API check on 2026-04-06:
  - name:
    `Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells`
  - files: `101`
  - bytes: `2559248010229`
  - variables include `ElectricalSeries`, `LFP`, and `Units`
  - measurement techniques include multi-electrode extracellular electrophysiology
- Example observed asset paths:
  - `sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140327_behavior+ecephys.nwb`
  - `sub-YutaMouse20/sub-YutaMouse20_ses-YutaMouse20-140321_behavior+ecephys.nwb`
- Why it is the cleanest next target:
  - open DANDI surface
  - NWB payload
  - extracellular recordings already aligned with the current loader family
- Candidate acquisition command:
  `dandi download https://dandiarchive.org/dandiset/000003/draft --output-dir data/dandi000003/`

### DANDI `000005`

- Live DANDI API check on 2026-04-06:
  - name:
    `Electrophysiology data from thalamic and cortical neurons during somatosensation`
  - files: `148`
  - bytes: `46436686324`
  - variables include `CurrentClampStimulusSeries` and `CurrentClampSeries`
  - measurement techniques include `current clamp technique`
- Example observed asset paths:
  - `sub-anm186997/sub-anm186997_ses-20130317_behavior+ecephys.nwb`
  - `sub-anm184389/sub-anm184389_ses-20130213_behavior+ecephys.nwb`
- Repo interpretation:
  - open and valuable, but not a counted Lane 1 breadth target because the
    current codec is scoped to extracellular recordings.
- Candidate acquisition command:
  `dandi download https://dandiarchive.org/dandiset/000005/draft --output-dir data/dandi000005/`

### OpenNeuro EEG

- OpenNeuro documents browser download, CLI download, DataLad, and git-annex
  surfaces for public datasets.
- EEG is valuable as a future second representation mode, but it does not fit
  the current extracellular lane and should not be counted toward the present
  breadth claim.
- Sources:
  - https://docs.openneuro.org/packages/openneuro-cli.html
  - https://docs.openneuro.org/user_guide.html

## Priority Order

1. DANDI `000003` is the strongest next breadth candidate because it is open,
   NWB-based, and in-family for the current loader.
2. Allen Visual Coding Neuropixels is the next highest-value extracellular
   target, but it stays operator-only until the dependency split is honest.
3. IBL remains useful as a public operator route and replay path, not a new
   packaged surface.
4. DANDI `000005` and OpenNeuro EEG should be treated as explicit out-of-lane
   challenge corpora until the repo grows a second mode.
