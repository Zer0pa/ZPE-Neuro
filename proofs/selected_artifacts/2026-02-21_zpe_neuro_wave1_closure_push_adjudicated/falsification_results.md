# Falsification Results

## Summary
- Total cases: 6
- Failed cases: 1
- Uncaught crash count: 0
- Uncaught crash rate: 0.0000

## Case Outcomes
### DT-NEU-1 - PASS
- Description: Malformed metadata and invalid sampling rates
- Details: INVALID_SAMPLING_RATE

### DT-NEU-2 - PASS
- Description: Truncated spike windows and decode bounds checks
- Details: TRUNCATED_SPIKE_WINDOW

### DT-NEU-3 - PASS
- Description: High-noise adversarial perturbation
- Details: rmse_uV=8.0089

### DT-NEU-4 - PASS
- Description: Invalid sample-length metadata validation
- Details: INSUFFICIENT_SAMPLE_LENGTH

### DT-NEU-5 - FAIL
- Description: NWB contract corruption detection
- Details: Corrupted file read without error.

### DT-NEU-5B - PASS
- Description: SpikeInterface adapter contract corruption detection
- Details: tuple index out of range
