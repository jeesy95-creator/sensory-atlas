"""Display helpers for the Streamlit demo."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from sensory_atlas.evaluator import EvaluationReport, evaluate_parser
from sensory_atlas.loaders import load_sensory_objects, load_test_sentences, project_root
from sensory_atlas.schema import ParserOutput, SensoryObject


DATASETS = {
    "default": "test_sentences_20.jsonl",
    "blind": "blind_test_sentences_30.jsonl",
    "holdout": "holdout_test_sentences_50.jsonl",
}
AXIS_LABELS = {
    "material": "Material",
    "temperature": "Temperature",
    "texture": "Texture",
    "light": "Light",
    "motion": "Motion",
    "time": "Time",
    "atmosphere": "Atmosphere",
    "density": "Density",
    "rendering": "Rendering",
    "organic_mineral": "Organic/Mineral",
}


def load_objects_for_ui(path: str | Path | None = None) -> list[SensoryObject]:
    return load_sensory_objects(path)


def objects_to_dataframe(objects: list[SensoryObject]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for obj in objects:
        extra = obj.model_extra or {}
        rows.append(
            {
                "object_id": obj.object_id,
                "label": obj.label,
                "korean_label": obj.korean_label,
                "object_type": obj.object_type,
                "family": obj.family,
                "definition": obj.definition,
                "confidence": obj.confidence,
                "status": extra.get("status"),
            }
        )
    return pd.DataFrame(rows)


def get_object_lookup(objects: list[SensoryObject]) -> dict[str, SensoryObject]:
    return {obj.object_id: obj for obj in objects}


def format_axis_value(value: str | list[str] | None) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value if item is not None)
    return str(value)


def format_axis_confidence(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.2f}"


def axis_evidence_to_dataframe(output: ParserOutput) -> pd.DataFrame:
    axes_payload = output.axes.model_dump()
    axis_keys = sorted(
        set(axes_payload)
        | set(output.axis_evidence)
        | set(output.axis_confidence),
        key=lambda item: (item not in AXIS_LABELS, item),
    )
    rows = []
    for axis in axis_keys:
        inferred_value = format_axis_value(axes_payload.get(axis))
        evidence = format_axis_value(output.axis_evidence.get(axis, []))
        confidence = format_axis_confidence(output.axis_confidence.get(axis))
        if not inferred_value and not evidence and not confidence:
            continue
        rows.append(
            {
                "axis": AXIS_LABELS.get(axis, axis),
                "inferred_value": inferred_value,
                "evidence": evidence,
                "axis_confidence": confidence,
            }
        )
    return pd.DataFrame(rows)


def _object_display_row(object_id: str, score: float | None, rank: int | None, lookup: dict[str, SensoryObject]) -> dict[str, Any]:
    obj = lookup.get(object_id)
    return {
        "rank": rank,
        "object_id": object_id,
        "korean_label": obj.korean_label if obj else "",
        "label": obj.label if obj else "",
        "score": score,
        "family": obj.family if obj else "",
    }


def parser_output_to_display_dict(
    output: ParserOutput,
    object_lookup: dict[str, SensoryObject],
) -> dict[str, Any]:
    anchor = None
    if output.anchor_object:
        anchor_obj = object_lookup.get(output.anchor_object.object_id)
        anchor = {
            "object_id": output.anchor_object.object_id,
            "score": output.anchor_object.score,
            "label": anchor_obj.label if anchor_obj else "",
            "korean_label": anchor_obj.korean_label if anchor_obj else "",
            "family": anchor_obj.family if anchor_obj else "",
            "definition": anchor_obj.definition if anchor_obj else "",
        }

    detected_rows = [
        _object_display_row(item.object_id, item.score, index, object_lookup)
        for index, item in enumerate(output.detected_objects, start=1)
    ]
    axes = {
        "Material": format_axis_value(output.axes.material),
        "Temperature": format_axis_value(output.axes.temperature),
        "Texture": format_axis_value(output.axes.texture),
        "Light": format_axis_value(output.axes.light),
        "Motion": format_axis_value(output.axes.motion),
        "Time": format_axis_value(output.axes.time),
        "Atmosphere": format_axis_value(output.axes.atmosphere),
        "Density": format_axis_value(output.axes.density),
        "Rendering": format_axis_value(output.axes.rendering),
        "Organic/Mineral": format_axis_value(output.axes.organic_mineral),
    }
    cue_groups = [
        {
            "group_id": item.group_id,
            "score": item.score,
            "matched_positive_cues": format_axis_value(item.matched_positive_cues),
            "matched_negative_cues": format_axis_value(item.matched_negative_cues),
        }
        for item in output.activated_cue_groups
    ]
    return {
        "summary": output.interpretation_summary,
        "anchor": anchor,
        "detected_objects": detected_rows,
        "axes": axes,
        "axis_evidence": output.axis_evidence,
        "axis_confidence": output.axis_confidence,
        "axis_evidence_table": axis_evidence_to_dataframe(output),
        "clarification_questions": output.clarification_questions,
        "activated_cue_groups": cue_groups,
        "confidence": output.confidence,
        "low_confidence": output.low_confidence,
        "raw": output.model_dump(mode="json"),
    }


def evaluate_all_datasets(root: str | Path | None = None) -> dict[str, EvaluationReport]:
    root_path = Path(root) if root else project_root()
    objects = load_sensory_objects(root_path / "data" / "sensory_objects.jsonl")
    reports: dict[str, EvaluationReport] = {}
    for dataset_name, file_name in DATASETS.items():
        records = load_test_sentences(root_path / "data" / file_name)
        reports[dataset_name] = evaluate_parser(records, objects, dataset_name=dataset_name)
    return reports
