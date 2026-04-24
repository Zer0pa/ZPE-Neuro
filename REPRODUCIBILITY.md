# Reproducibility

## Canonical Inputs

- `tests/fixtures/dandi000034_extract.nwb`
- `tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/dandi_000034_mouse412804_ecephys/`
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ibl_ks014_2019_12_03_probe00_ap/`

## Golden-Bundle Hash

This field will be populated by the `receipt-bundle.yml` workflow in Wave 3.

## Verification Command

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest tests
```

## Supported Runtimes

- Python 3.11+
- `pip install .` for the packaged core surface
- `pip install -e '.[dev]'` for the repo-local test slice
- `pip install -e '.[gate,proof]'` for the bounded gate and public replay surface
