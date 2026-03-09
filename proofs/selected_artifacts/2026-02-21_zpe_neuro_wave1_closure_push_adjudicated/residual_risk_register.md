# Residual Risk Register

| Risk | Impact | Mitigation | Status |
|---|---|---|---|
| Commercial-safe comparator path (PASS) | Comparator closure may not satisfy max-wave if MountainSort5 fails | Run M1 with MountainSort5 first; escalate to RunPod on compute failure | MITIGATED |
| Kilosort4 comparator high-stringency path (PASS) | Optional stricter parity not closed on local runtime | Local tuning sweep + container probe recorded; keep benchmark-isolated path and retry on RunPod GPU | MITIGATED |
| Allen external corpus parity (Neuropixels) | Real-world distribution shift risk if only metadata is validated | Run 3-attempt waveform closure loop (cache read, warehouse fetch, direct WFK stream) with explicit dependency proof | ADJUDICATED_FAIL |
| Neuralink challenge-style external corpus (PASS) | Challenge comparability risk if corpus execution is absent | Clone corpus repo and run deterministic lossless replay benchmark | MITIGATED |
| Embedded latency target-profile evidence | Hardware timing may differ on target silicon | Compile/run C99 hot-path benchmark and track host-normalized target profile | MITIGATED |
