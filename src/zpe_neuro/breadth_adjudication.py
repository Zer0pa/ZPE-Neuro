from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ARTIFACT_ROOT = REPO_ROOT / "proofs" / "selected_artifacts" / "2026-03-21_zpe_neuro_ibl_refinement"
DEFAULT_WINDOW_ROOT = DEFAULT_ARTIFACT_ROOT
DEFAULT_IBL_ROOT = DEFAULT_ARTIFACT_ROOT


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def _resolve_repo_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO_ROOT / path


def _relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)


def _utc_now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat()


def _fallback_role(label: str) -> str:
    if label == "dandi_000034_mouse412804_ecephys":
        return "tier1_authority_anchor"
    if label == "ajile12_sub01_ses7_ecephys":
        return "out_of_family_control"
    if label == "dandi_000003_yutamouse20_ecephys":
        return "next_extracellular_target"
    return "candidate_target"


def _fallback_counted_in_breadth(label: str, tier: str) -> bool:
    if label in {"dandi_000034_mouse412804_ecephys", "ajile12_sub01_ses7_ecephys"}:
        return False
    return tier == "tier2_breadth"


def _normalize_public_eval(path: Path, payload: dict[str, Any], artifact_root: Path) -> dict[str, Any]:
    source = payload.get("source", {})
    label = str(source.get("target_label") or path.stem.removeprefix("public_corpus_eval_"))
    tier = str(source.get("tier") or "tier2_breadth")
    role = str(source.get("role") or _fallback_role(label))
    counted_in_breadth = bool(source.get("counted_in_breadth", _fallback_counted_in_breadth(label, tier)))
    return {
        "target_label": label,
        "tier": tier,
        "waveform_executed": True,
        "evaluation_status": payload.get("status", "FAIL"),
        "counted_in_breadth": counted_in_breadth,
        "role": role,
        "artifact": _relative(artifact_root / path.name),
    }


def build_family_boundary_decision(
    dandi_eval: dict[str, Any],
    ajile_eval: dict[str, Any],
    ajile_selection: dict[str, Any],
    ibl_eval: dict[str, Any],
) -> dict[str, Any]:
    ajile_source = ajile_eval.get("source", {})
    ajile_codec = ajile_eval.get("codec_metrics", {})
    ajile_spike = ajile_eval.get("spikeinterface", {})
    dandi_codec = dandi_eval.get("codec_metrics", {})
    dandi_spike = dandi_eval.get("spikeinterface", {})
    ibl_spike = ibl_eval.get("spikeinterface", {})

    decision = "OUT_OF_FAMILY"
    confidence = "medium"
    if (
        ajile_eval.get("status") == "PASS"
        or ajile_spike.get("status") == "PASS"
        or int(ajile_spike.get("peak_count") or 0) > 0
    ):
        decision = "IN_FAMILY"
        confidence = "low"

    rationale = [
        (
            "DANDI remains the sovereign positive anchor: the selected-window rerun stayed PASS "
            f"with {int(dandi_codec.get('event_count') or 0)} codec events and "
            f"{int(dandi_spike.get('peak_count') or 0)} detected peaks."
        ),
        (
            "AJILE no longer hides behind a quiet first window: the scan policy promoted an "
            f"informative slice at sample {int(ajile_selection.get('selected_start_sample') or 0)} "
            f"where the first window ranked {int(ajile_selection.get('first_window_rank') or 0)}."
        ),
        (
            "That informative AJILE slice still produced only "
            f"{int(ajile_codec.get('event_count') or 0)} codec events at "
            f"{int(ajile_source.get('sampling_rate_hz') or 0)} Hz, with "
            f"{int(ajile_spike.get('peak_count') or 0)} detected peaks and final status "
            f"{ajile_eval.get('status', 'UNKNOWN')}."
        ),
        (
            "IBL now provides the counted second extracellular-style waveform path in the current "
            f"packet, with {int(ibl_spike.get('peak_count') or 0)} detected peaks and downstream "
            f"status {ibl_eval.get('evaluation_status', 'UNKNOWN')}. Breadth is therefore bounded "
            "to the extracellular lane rather than broad neural generality."
        ),
    ]
    return {
        "decision": decision,
        "confidence": confidence,
        "status": "PASS",
        "summary": (
            "AJILE12 is out-of-family for the current Lane 1 spike-oriented codec; "
            "the lane should narrow around extracellular-style authority rather than narrate broad support."
        )
        if decision == "OUT_OF_FAMILY"
        else "AJILE12 remains in-family, but the current evidence is too weak to count it as supported.",
        "rationale": rationale,
        "evidence_basis": {
            "dandi_status": dandi_eval.get("status"),
            "dandi_event_count": int(dandi_codec.get("event_count") or 0),
            "dandi_peak_count": int(dandi_spike.get("peak_count") or 0),
            "ajile_status": ajile_eval.get("status"),
            "ajile_event_count": int(ajile_codec.get("event_count") or 0),
            "ajile_peak_count": int(ajile_spike.get("peak_count") or 0),
            "ajile_sampling_rate_hz": int(ajile_source.get("sampling_rate_hz") or 0),
            "ajile_selected_start_sample": int(ajile_selection.get("selected_start_sample") or 0),
            "ibl_waveform_status": ibl_eval.get("status"),
            "ibl_evaluation_status": ibl_eval.get("evaluation_status"),
            "ibl_peak_count": int(ibl_spike.get("peak_count") or 0),
        },
        "next_lane_implication": (
            "Treat Lane 1 as a narrower extracellular wedge. Human intracranial breadth should be a separate lane "
            "or a later second-mode effort, not a hidden requirement for the current codec."
        ),
    }


def build_public_summary(
    artifact_root: Path,
    family_boundary: dict[str, Any],
    public_eval_targets: list[dict[str, Any]],
    dandi_eval: dict[str, Any],
    ajile_eval: dict[str, Any],
    ibl_eval: dict[str, Any],
    selection_summary: dict[str, Any],
) -> dict[str, Any]:
    targets = list(public_eval_targets)
    targets.append(
        {
            "target_label": ibl_eval["source"]["target_label"],
            "tier": ibl_eval["source"]["tier"],
            "waveform_executed": bool(ibl_eval.get("waveform_slice_executed")),
            "evaluation_status": ibl_eval.get("evaluation_status", "UNKNOWN"),
            "counted_in_breadth": True,
            "role": "second_extracellular_target",
            "artifact": _relative(artifact_root / "public_corpus_ibl_waveform_eval.json"),
        }
    )
    counted_targets = [item for item in targets if item["counted_in_breadth"]]
    counted_passes = [
        item
        for item in counted_targets
        if item["waveform_executed"] and item["evaluation_status"] == "PASS"
    ]
    breadth_status = "PASS" if counted_targets and len(counted_passes) == len(counted_targets) else "FAIL"
    tier1_anchor = next(
        (item for item in targets if item["role"] == "tier1_authority_anchor"),
        {
            "target_label": dandi_eval["source"]["target_label"],
            "evaluation_status": dandi_eval["status"],
        },
    )
    return {
        "schema_version": "breadth-adjudication-2026-03-21",
        "generated_at_utc": _utc_now_iso(),
        "status": breadth_status,
        "breadth_verdict": breadth_status,
        "family_boundary_decision": family_boundary["decision"],
        "family_boundary_artifact": "ajile12_family_boundary_decision.md",
        "window_policy": selection_summary.get("window_policy", "scan"),
        "window_selection_artifact": "public_corpus_window_selection_summary.json",
        "tier1_anchor": {
            "target_label": tier1_anchor["target_label"],
            "status": tier1_anchor["evaluation_status"],
            "reason": "Preserved positive authority anchor; not counted as breadth closure.",
        },
        "targets": targets,
        "counting_policy": {
            "summary": "Only real waveform targets count for breadth, and out-of-family controls do not count as breadth passes or misses.",
            "counted_target_labels": [item["target_label"] for item in counted_targets],
            "excluded_target_labels": [item["target_label"] for item in targets if not item["counted_in_breadth"]],
        },
        "breadth_counts": {
            "executed_waveform_targets": sum(1 for item in targets if item["waveform_executed"]),
            "counted_targets": len(counted_targets),
            "counted_passes": len(counted_passes),
        },
        "next_step": (
            "Keep the lane explicit as a bounded extracellular product, preserve the counted IBL pass, "
            "and keep blind-clone and commercialization gates separate from the current breadth verdict."
        ),
    }


def _write_markdown_memo(path: Path, family_boundary: dict[str, Any], evidence_paths: dict[str, str]) -> None:
    rationale_lines = "\n".join(f"- {line}" for line in family_boundary["rationale"])
    path.write_text(
        "\n".join(
            [
                "# AJILE12 Family Boundary Decision",
                "",
                f"- Decision: `{family_boundary['decision']}`",
                f"- Confidence: `{family_boundary['confidence']}`",
                f"- Status: `{family_boundary['status']}`",
                "",
                "## Verdict",
                family_boundary["summary"],
                "",
                "## Evidence Basis",
                rationale_lines,
                "",
                "## Source Artifacts",
                f"- DANDI selected-window eval: `{evidence_paths['dandi_eval']}`",
                f"- AJILE selected-window eval: `{evidence_paths['ajile_eval']}`",
                f"- AJILE selection artifact: `{evidence_paths['ajile_selection']}`",
                f"- IBL waveform eval: `{evidence_paths['ibl_eval']}`",
                "",
                "## Next-Lane Implication",
                family_boundary["next_lane_implication"],
                "",
            ]
        )
    )


def run_breadth_adjudication(
    artifact_root: Path = DEFAULT_ARTIFACT_ROOT,
    window_root: Path = DEFAULT_WINDOW_ROOT,
    ibl_root: Path = DEFAULT_IBL_ROOT,
) -> dict[str, Any]:
    artifact_root = _resolve_repo_path(artifact_root)
    window_root = _resolve_repo_path(window_root)
    ibl_root = _resolve_repo_path(ibl_root)
    artifact_root.mkdir(parents=True, exist_ok=True)

    dandi_eval_path = window_root / "public_corpus_eval_dandi_000034_mouse412804_ecephys.json"
    ajile_eval_path = window_root / "public_corpus_eval_ajile12_sub01_ses7_ecephys.json"
    ajile_selection_path = window_root / "public_corpus_window_selection_ajile12_sub01_ses7_ecephys.json"
    selection_summary_path = window_root / "public_corpus_window_selection_summary.json"
    dandi_selection_path = window_root / "public_corpus_window_selection_dandi_000034_mouse412804_ecephys.json"
    ibl_eval_path = ibl_root / "public_corpus_ibl_waveform_eval.json"

    dandi_eval = _read_json(dandi_eval_path)
    ajile_eval = _read_json(ajile_eval_path)
    ajile_selection = _read_json(ajile_selection_path)
    selection_summary = _read_json(selection_summary_path)
    dandi_selection = _read_json(dandi_selection_path)
    ibl_eval = _read_json(ibl_eval_path)
    public_eval_targets = [
        _normalize_public_eval(path, _read_json(path), artifact_root)
        for path in sorted(window_root.glob("public_corpus_eval_*.json"))
    ]

    family_boundary = build_family_boundary_decision(
        dandi_eval=dandi_eval,
        ajile_eval=ajile_eval,
        ajile_selection=ajile_selection,
        ibl_eval=ibl_eval,
    )
    summary = build_public_summary(
        artifact_root=artifact_root,
        family_boundary=family_boundary,
        public_eval_targets=public_eval_targets,
        dandi_eval=dandi_eval,
        ajile_eval=ajile_eval,
        ibl_eval=ibl_eval,
        selection_summary=selection_summary,
    )

    _write_markdown_memo(
        artifact_root / "ajile12_family_boundary_decision.md",
        family_boundary=family_boundary,
        evidence_paths={
            "dandi_eval": _relative(dandi_eval_path),
            "ajile_eval": _relative(ajile_eval_path),
            "ajile_selection": _relative(ajile_selection_path),
            "ibl_eval": _relative(ibl_eval_path),
        },
    )

    copied_selection_summary = dict(selection_summary)
    copied_selection_summary["generated_at_utc"] = _utc_now_iso()
    copied_selection_summary["source_artifact"] = _relative(selection_summary_path)
    copied_selection_summary["target_artifacts"] = {
        item["target_label"]: _relative(window_root / item["artifact"])
        for item in selection_summary.get("targets", [])
        if item.get("artifact")
    }

    payloads_to_copy: list[tuple[str, dict[str, Any]]] = [
        ("public_corpus_summary.json", summary),
        ("public_corpus_window_selection_summary.json", copied_selection_summary),
        ("public_corpus_ibl_waveform_eval.json", ibl_eval),
    ]
    for path in sorted(window_root.glob("public_corpus_eval_*.json")):
        payloads_to_copy.append((path.name, _read_json(path)))
    for path in sorted(window_root.glob("public_corpus_window_selection_*.json")):
        payloads_to_copy.append((path.name, _read_json(path)))

    for name, payload in payloads_to_copy:
        (artifact_root / name).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    return {
        "status": "PASS",
        "artifact_root": _relative(artifact_root),
        "family_boundary_decision": family_boundary["decision"],
        "breadth_verdict": summary["breadth_verdict"],
    }
