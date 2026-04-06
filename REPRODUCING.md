# Reproducing ZPE-Neuro

This document covers the reproducible paths that are now exercised directly in
the repo: offline tests, public-corpus downloads, and the DANDI benchmark
runner.

## Offline Verify

Install the offline/public replay stack:

```bash
python3.11 -m pip install -e '.[dev,public,proof]'
```

Run the full offline regression slice:

```bash
make offline-verify
```

Current expected result:

```text
25 passed
```

Notes:
- The committed fixture at `tests/fixtures/dandi000034_extract.nwb` keeps the
  DANDI offline tests local.
- In a `.[dev]`-only environment, the `pynwb`-backed fixture tests skip
  cleanly instead of breaking the shipped unit slice.

## Public DANDI Downloads

The DANDI CLI used here requires the output directory to exist first:

```bash
mkdir -p data/dandi000034 data/dandi000055
```

Then run the exact public acquisition commands:

```bash
dandi download https://dandiarchive.org/dandiset/000034/draft --output-dir data/dandi000034/
dandi download https://dandiarchive.org/dandiset/000055/draft --output-dir data/dandi000055/
```

The repo-local convenience target is:

```bash
make download-dandi
```

## Benchmark Commands

Run the DANDI `000034` benchmark and refresh the committed offline fixture:

```bash
python3.11 tools/run_public_corpus_benchmark.py \
  --dandiset 000034 \
  --artifact-root proofs/artifacts/dandi000034_benchmark \
  --fixture-output tests/fixtures/dandi000034_extract.nwb
```

Run against a local `dandi download` tree instead of the remote content URL:

```bash
python3.11 tools/run_public_corpus_benchmark.py \
  --dandiset 000034 \
  --data-root data/dandi000034 \
  --artifact-root proofs/artifacts/dandi000034_benchmark \
  --fixture-output tests/fixtures/dandi000034_extract.nwb
```

Current `000034` benchmark anchor:
- selected start sample: `16871250`
- codec events: `41`
- compression ratio: `401.0443864229765`
- fixture size: `294600` bytes

## Offline Fixture Expectations

The committed fixture captures:
- `6000` samples
- `8` channels
- `30000 Hz`

The fixture-backed offline tests validate:
- deterministic encode/decode behavior
- representative public-corpus metrics on the selected DANDI `000034` slice
- scaling and clipping helpers without network access

## KiloSort4 Status

KiloSort4 remains an operator-only comparator path.

Current truth:
- actual KiloSort4 runs require a CUDA-capable GPU
- the packaged offline verify path does not depend on KiloSort4
- the upstream `llvmlite` / `numba` installation story still needs a dedicated
  operator note before it can be claimed as a reproducible repo default

See `docs/KILOSORT4.md` for the current operator note.
