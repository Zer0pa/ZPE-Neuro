<p>
  <img src="../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

# KiloSort4 Operator Note

Snapshot date: `2026-04-06`

This repo keeps KiloSort4 in the benchmark-only/operator-only lane. It is not
part of the shipped clean install surface.

## Current Verdict

| Question | Verdict |
|---|---|
| Does real KiloSort4 execution require GPU? | `YES` — use a CUDA-capable NVIDIA GPU |
| Is KiloSort4 itself currently documented as a `llvmlite` install? | `NO` — the current official install path is `kilosort` + PyTorch |
| Are `llvmlite==0.41.x` or `0.43.x` still useful? | `YES`, but only for older `numba`-dependent auxiliary paths, not as a standalone KiloSort4 fix |

## Official KiloSort4 Path

The current official KiloSort4 installation path is:

```bash
conda create --name kilosort python=3.11
conda activate kilosort
python -m pip install "kilosort[gui]"
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

Adjust the PyTorch CUDA wheel to match the actual GPU/driver pair. The current
official KiloSort4 docs explicitly recommend conda for environment management
and PyTorch for GPU enablement.

## What That Means For This Repo

The repo's historical `llvmlite` failure should be treated as an
auxiliary-toolchain issue, not automatically as a KiloSort4 core install
failure.

Most likely split:
- modern KiloSort4 path: `kilosort` + PyTorch + CUDA
- older operator stack pain: `numba` / `llvmlite` chains inside legacy or
  adjacent tooling

## If You Still Need `llvmlite`

Use conda-prebuilt binaries instead of a source build.

Compatibility anchors from the official Numba install matrix:
- Numba `0.58.x` pairs with `llvmlite 0.41.x`
- Numba `0.60.x` pairs with `llvmlite 0.43.x`
- Numba `0.62.0` raises the floor to `llvmlite 0.45+`

That means the brief's candidate pins:

```bash
conda install numba=0.58 llvmlite=0.41
```

or

```bash
conda install numba=0.60 llvmlite=0.43
```

are coherent operator probes, but only when the `numba` pin matches the
`llvmlite` pin.

## Recommended Repo Guidance

1. Keep KiloSort4 benchmark-only and operator-only.
2. Document the modern official path as the primary route.
3. Treat `conda install numba llvmlite` as a fallback only for older
   numba-dependent tooling.
4. Do not add KiloSort4 or CUDA PyTorch to the packaged extras.
