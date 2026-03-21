from __future__ import annotations

import unittest

from zpe_neuro.breadth_adjudication import build_family_boundary_decision, build_public_summary


class BreadthAdjudicationTests(unittest.TestCase):
    def test_family_boundary_defaults_to_out_of_family_for_ajile_fail(self) -> None:
        decision = build_family_boundary_decision(
            dandi_eval={
                "status": "PASS",
                "codec_metrics": {"event_count": 41},
                "spikeinterface": {"peak_count": 34},
            },
            ajile_eval={
                "status": "FAIL",
                "source": {"sampling_rate_hz": 500},
                "codec_metrics": {"event_count": 3},
                "spikeinterface": {"status": "FAIL", "peak_count": 0},
            },
            ajile_selection={"selected_start_sample": 20889595, "first_window_rank": 9},
            ibl_eval={
                "status": "PASS",
                "evaluation_status": "FAIL",
                "spikeinterface": {"peak_count": 0},
            },
        )
        self.assertEqual(decision["decision"], "OUT_OF_FAMILY")
        self.assertEqual(decision["status"], "PASS")

    def test_public_summary_counts_only_designated_breadth_targets(self) -> None:
        summary = build_public_summary(
            artifact_root=__import__("pathlib").Path("proofs/selected_artifacts/test"),
            family_boundary={"decision": "OUT_OF_FAMILY"},
            dandi_eval={"source": {"target_label": "dandi", "tier": "tier1"}, "status": "PASS"},
            ajile_eval={"source": {"target_label": "ajile", "tier": "tier2"}, "status": "FAIL"},
            ibl_eval={
                "source": {"target_label": "ibl", "tier": "tier2"},
                "status": "PASS",
                "evaluation_status": "FAIL",
                "waveform_slice_executed": True,
            },
            selection_summary={"window_policy": "scan"},
        )
        self.assertEqual(summary["breadth_verdict"], "FAIL")
        self.assertEqual(summary["breadth_counts"]["counted_targets"], 1)
        self.assertEqual(summary["breadth_counts"]["counted_passes"], 0)


if __name__ == "__main__":
    unittest.main()
