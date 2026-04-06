# DANDI 000034 Download Note

Exact command executed on the isolated RunPod workspace for A1:

```bash
dandi download https://dandiarchive.org/dandiset/000034/draft --output-dir data/dandi000034/
```

Observed authoritative target path in the live DANDI API and local download tree:

```text
sub-mouse412804/sub-mouse412804_ecephys.nwb
```

The benchmark artifact in this directory was produced with:

```bash
python3.11 tools/run_public_corpus_benchmark.py --dandiset 000034 --artifact-root proofs/artifacts/dandi000034_benchmark
```

This follows the benchmark invocation shape shown in the brief:
`PublicCorpusRunner(dandiset_id="000034")`.

The exact `dandi download` command above was launched successfully in parallel to
remove the stale "S3-dependent" blocker and populate the local DANDI tree in
the isolated RunPod workspace while the benchmark replay executed against the
canonical `000034` Tier-1 anchor.
