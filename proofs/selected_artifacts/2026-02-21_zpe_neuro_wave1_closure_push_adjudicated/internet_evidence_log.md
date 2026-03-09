# Internet Evidence Log

Generated: 2026-02-21T16:00:00Z
Lane: /Users/prinivenpillay/ZPE Multimodality/ZPE Neuro

## Source Links (Primary)
1. Kilosort parameter guidance (official docs): https://kilosort.readthedocs.io/en/latest/parameters.html
2. Kilosort repository README (hardware/platform constraints): https://raw.githubusercontent.com/MouseLand/Kilosort/main/README.md
3. Kilosort issue on low/no spikes behavior: https://github.com/MouseLand/Kilosort/issues/619
4. SpikeInterface Kilosort4 sorter docs (runtime parameters): https://spikeinterface.readthedocs.io/en/stable/modules/sorters.html#spikeinterface.sorters.run_sorter
5. AllenSDK ecephys cache notebook (download/runtime model): https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_data_access.html
6. Allen public API session endpoint: https://api.brain-map.org/api/v2/data/query.json?criteria=model::EcephysSession,rma::options[num_rows$eq10]
7. Allen AWS registry page: https://registry.opendata.aws/allen-brain-observatory/

## Local Package Versions
- kilosort==4.1.5
- spikeinterface==0.103.2
- allensdk==2.16.2
- wfdb==4.1.2
Command evidence:
- `source .venv/bin/activate && python -m pip show kilosort spikeinterface allensdk wfdb | rg "^(Name|Version):"`

## Comparator Debug Commands (Executed)
1. `set -a; source .env; set +a; source .venv/bin/activate; export ZPE_NEURO_ARTIFACT_ROOT=artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated; python3.11 tools/run_gate_m1.py`
2. `set -a; source .env; set +a; source .venv/bin/activate; export ZPE_NEURO_ARTIFACT_ROOT=artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated; python3.11 tools/run_gate_m2.py`
3. `set -a; source .env; set +a; source .venv/bin/activate; export ZPE_NEURO_ARTIFACT_ROOT=artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated; python3.11 tools/run_gate_m3.py`
4. `set -a; source .env; set +a; source .venv/bin/activate; export ZPE_NEURO_ARTIFACT_ROOT=artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated; python3.11 tools/run_gate_m4.py`
5. `set -a; source .env; set +a; source .venv/bin/activate; export ZPE_NEURO_ARTIFACT_ROOT=artifacts/2026-02-21_zpe_neuro_wave1_closure_push_adjudicated; python3.11 tools/run_gate_appendix_e.py`

## Mapping: Source -> Technical Fix
- KS4-FIX-A (small-probe + threshold tuning) mapped to Kilosort docs parameters guidance.
- KS4-FIX-B (geometry tuning, nearest_templates<=channels) mapped to Kilosort parameter reference and issue discussion.
- KS4-FIX-C (extended-duration run) mapped to issue reports of low-spike regimes and improved data support.
- Allen-FIX-A/B/C mapped to AllenSDK access notebook + Allen API endpoints.

## Outcome Summary
- Kilosort4 high-stringency closure achieved via KS4-FIX-C (`tmp_ks4_tuning_results.json`, `gate_m1_summary.json`).
- Allen waveform parity remains INCONCLUSIVE after 4 concrete attempts with explicit dependency signatures (`allen_waveform_parity_eval.json`).
