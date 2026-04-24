# Reproducibility

## Canonical Inputs

- `tests/fixtures/dandi000034_extract.nwb` - offline NWB fixture for the
  repo-local public-corpus regression slice.
- `tests/fixtures/dandi_000034_mouse412804_ecephys_scan_6000x8.npz` -
  deterministic scan fixture for codec and edge-case coverage.
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/dandi_000034_mouse412804_ecephys/` -
  retained bounded DANDI slice referenced by the current authority packet.
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ibl_ks014_2019_12_03_probe00_ap__chunk0000_ch096_w06000/` -
  retained bounded IBL slice referenced by the current authority packet.
- `proofs/selected_artifacts/2026-03-21_zpe_neuro_ibl_refinement/ibl_ks014_2019_12_03_probe00_ap__chunk0732_ch128_w12000/` -
  retained bounded IBL slice referenced by the current authority packet.

## Golden-Bundle Hash

This will be populated by the `receipt-bundle.yml` workflow in Wave 3.

## Verification Command

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest tests
```

## Supported Runtimes

- `Python >=3.11` as declared in `pyproject.toml`.
- `pip install zpe-neuro` for the packaged runtime surface.
- `pip install -e '.[dev]'` for the repo-local verification slice.
- `pip install -e '.[gate,proof]'` for the bounded gate replay slice.
