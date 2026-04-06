# DANDI 000055 Download Note

Exact command executed on the isolated RunPod workspace for A2:

```bash
dandi download https://dandiarchive.org/dandiset/000055/draft --output-dir data/dandi000055/
```

Observed authoritative target path in the live DANDI API and local download tree:

```text
sub-01/sub-01_ses-7_behavior+ecephys.nwb
```

The benchmark artifact in this directory was produced with:

```bash
python3.11 tools/run_public_corpus_benchmark.py --dandiset 000055 --artifact-root proofs/artifacts/dandi000055_benchmark
```

This follows the benchmark invocation shape shown in the brief:
`PublicCorpusRunner(dandiset_id="000055")`.

The exact `dandi download` command above was launched successfully in parallel
to remove the stale download blocker and populate the local DANDI tree in the
isolated RunPod workspace while the benchmark replay executed against the
canonical `000055` breadth target.
