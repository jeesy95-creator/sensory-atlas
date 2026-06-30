"""Candidate sensory object review workflow utilities."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from sensory_atlas.loaders import project_root, read_jsonl


ALLOWED_REVIEW_STATUSES = {
    "unreviewed",
    "reviewing",
    "approved_for_curated_merge",
    "needs_more_examples",
    "needs_distinction_review",
    "rejected",
    "merged",
}
ALLOWED_PRIORITIES = {"high", "medium", "low"}
RECOMMENDED_ACTIONS = {
    "ready_for_curated_merge",
    "needs_more_examples",
    "needs_distinction_review",
    "keep_as_candidate",
    "keep_as_axis_descriptor",
    "do_not_merge_yet",
}
NOTE_LIKE_TERMS = {
    "bergamot",
    "neroli",
    "orange",
    "musk",
    "amber",
    "oak",
    "vanilla",
    "fruit",
    "spice",
    "herbal",
    "coffee",
    "wine",
    "whisky",
    "jasmine",
    "rose",
}
SENSORY_AXIS_KEYS = {
    "material",
    "temperature",
    "texture",
    "light",
    "motion",
    "time",
    "atmosphere",
    "density",
    "rendering",
    "organic_mineral",
}
ARCHETYPE_WORDS = {
    "air",
    "skin",
    "surface",
    "warmth",
    "coolness",
    "texture",
    "atmosphere",
    "glow",
    "density",
    "body",
    "finish",
    "flow",
    "spark",
    "smoke",
    "softness",
    "clarity",
    "edge",
    "depth",
}


def _resolve(path: str | Path) -> Path:
    path = Path(path)
    if path.is_absolute():
        return path
    return project_root() / path


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if item is not None]
    return [str(value)]


def _tokenize(value: Any) -> set[str]:
    text = " ".join(_as_list(value)).casefold()
    return {token for token in re.findall(r"[a-z0-9가-힣]+", text) if len(token) >= 2}


def _score_from_count(count: int, high: int, medium: int) -> float:
    if count >= high:
        return 1.0
    if count >= medium:
        return 0.65
    if count > 0:
        return 0.35
    return 0.0


def load_candidate_objects(path: str | Path = "data/sensory_object_candidates.jsonl") -> list[dict[str, Any]]:
    return read_jsonl(_resolve(path))


def load_existing_objects(path: str | Path = "data/sensory_objects.jsonl") -> list[dict[str, Any]]:
    return read_jsonl(_resolve(path))


def load_candidate_review_status(
    path: str | Path = "data/candidate_review_status.jsonl",
) -> dict[str, dict[str, Any]]:
    status_path = _resolve(path)
    if not status_path.exists():
        return {}
    rows = read_jsonl(status_path)
    return {str(row["candidate_object_id"]): row for row in rows}


def _axis_overlap(candidate: dict[str, Any], existing: dict[str, Any]) -> float:
    candidate_axes = candidate.get("core_axes", {}) or {}
    existing_axes = existing.get("core_axes", {}) or {}
    if not candidate_axes or not existing_axes:
        return 0.0

    overlap = 0
    total = len(set(candidate_axes) | set(existing_axes))
    for axis, candidate_value in candidate_axes.items():
        existing_value = existing_axes.get(axis)
        if not existing_value:
            continue
        if set(_as_list(candidate_value)) & set(_as_list(existing_value)):
            overlap += 1
    return overlap / max(total, 1)


def _family_overlap(candidate: dict[str, Any], existing: dict[str, Any]) -> float:
    candidate_tokens = _tokenize(candidate.get("family", ""))
    existing_tokens = _tokenize(existing.get("family", ""))
    if not candidate_tokens or not existing_tokens:
        return 0.0
    return len(candidate_tokens & existing_tokens) / len(candidate_tokens | existing_tokens)


def _text_overlap(candidate: dict[str, Any], existing: dict[str, Any]) -> float:
    candidate_tokens = _tokenize(
        [
            candidate.get("definition", ""),
            *candidate.get("example_expressions", []),
            *candidate.get("suggested_phrase_cues", []),
        ]
    )
    existing_tokens = _tokenize(
        [
            existing.get("definition", ""),
            *existing.get("example_expressions", []),
            existing.get("label", ""),
            existing.get("korean_label", ""),
        ]
    )
    if not candidate_tokens or not existing_tokens:
        return 0.0
    return len(candidate_tokens & existing_tokens) / len(candidate_tokens | existing_tokens)


def compare_candidate_to_existing(
    candidate: dict[str, Any],
    existing_objects: list[dict[str, Any]],
    *,
    limit: int = 5,
) -> list[dict[str, Any]]:
    related = set(candidate.get("related_existing_objects", []))
    rows: list[dict[str, Any]] = []
    for existing in existing_objects:
        reasons: list[str] = []
        object_id = str(existing.get("object_id", ""))
        family_score = _family_overlap(candidate, existing)
        axis_score = _axis_overlap(candidate, existing)
        text_score = _text_overlap(candidate, existing)
        related_score = 1.0 if object_id in related else 0.0

        if related_score:
            reasons.append("related_existing_object")
        if family_score >= 0.15:
            reasons.append("family_overlap")
        if axis_score >= 0.20:
            reasons.append("axis_overlap")
        if text_score >= 0.03:
            reasons.append("keyword_overlap")

        overlap_score = min(
            1.0,
            0.35 * related_score + 0.25 * family_score + 0.25 * axis_score + 0.15 * text_score,
        )
        if overlap_score <= 0:
            continue
        rows.append(
            {
                "existing_object_id": object_id,
                "similarity_reason": reasons,
                "overlap_score": round(overlap_score, 2),
            }
        )

    return sorted(rows, key=lambda row: row["overlap_score"], reverse=True)[:limit]


def _note_dictionary_risk(candidate: dict[str, Any]) -> float:
    label_tokens = _tokenize([candidate.get("label", ""), candidate.get("candidate_object_id", "")])
    definition_tokens = _tokenize(candidate.get("definition", ""))
    note_hits = len(label_tokens & NOTE_LIKE_TERMS)
    has_archetype_language = bool((label_tokens | definition_tokens) & ARCHETYPE_WORDS)
    risk = min(1.0, 0.25 + 0.18 * note_hits)
    if has_archetype_language:
        risk -= 0.20
    if len(candidate.get("source_domains", [])) > 1:
        risk -= 0.10
    return round(max(0.0, min(risk, 1.0)), 2)


def compute_candidate_readiness(
    candidate: dict[str, Any],
    existing_objects: list[dict[str, Any]],
) -> dict[str, Any]:
    axes = candidate.get("core_axes", {}) or {}
    axis_count = len(set(axes) & SENSORY_AXIS_KEYS)
    definition_tokens = _tokenize(candidate.get("definition", ""))
    label_tokens = _tokenize([candidate.get("label", ""), candidate.get("candidate_object_id", "")])
    has_archetype_language = bool((definition_tokens | label_tokens) & ARCHETYPE_WORDS)

    sensory_archetype_score = min(1.0, 0.25 + 0.12 * axis_count + (0.20 if has_archetype_language else 0.0))
    cross_domain_reuse_score = _score_from_count(len(candidate.get("source_domains", [])), high=3, medium=2)
    example_coverage_score = _score_from_count(len(candidate.get("example_expressions", [])), high=5, medium=3)
    phrase_cue_readiness_score = _score_from_count(len(candidate.get("suggested_phrase_cues", [])), high=5, medium=3)
    negative_cue_readiness_score = _score_from_count(len(candidate.get("negative_cues", [])), high=3, medium=1)
    similar = compare_candidate_to_existing(candidate, existing_objects)
    max_overlap = similar[0]["overlap_score"] if similar else 0.0
    distinctiveness_score = round(max(0.0, 1.0 - max_overlap), 2)
    note_dictionary_risk = _note_dictionary_risk(candidate)

    positive_scores = [
        sensory_archetype_score,
        cross_domain_reuse_score,
        distinctiveness_score,
        example_coverage_score,
        phrase_cue_readiness_score,
        negative_cue_readiness_score,
    ]
    overall = sum(positive_scores) / len(positive_scores)
    overall = max(0.0, overall - note_dictionary_risk * 0.18)

    if note_dictionary_risk >= 0.70 or sensory_archetype_score < 0.45:
        recommended_action = "do_not_merge_yet"
    elif phrase_cue_readiness_score < 0.65 or example_coverage_score < 0.65:
        recommended_action = "needs_more_examples"
    elif distinctiveness_score < 0.55:
        recommended_action = "needs_distinction_review"
    elif "descriptor" in str(candidate.get("family", "")).casefold():
        recommended_action = "keep_as_axis_descriptor"
    elif overall >= 0.72 and note_dictionary_risk <= 0.45:
        recommended_action = "ready_for_curated_merge"
    else:
        recommended_action = "keep_as_candidate"

    return {
        "sensory_archetype_score": round(sensory_archetype_score, 2),
        "cross_domain_reuse_score": round(cross_domain_reuse_score, 2),
        "distinctiveness_score": distinctiveness_score,
        "example_coverage_score": round(example_coverage_score, 2),
        "phrase_cue_readiness_score": round(phrase_cue_readiness_score, 2),
        "negative_cue_readiness_score": round(negative_cue_readiness_score, 2),
        "note_dictionary_risk": note_dictionary_risk,
        "overall_readiness_score": round(overall, 2),
        "recommended_action": recommended_action,
        "similar_existing_objects": similar,
    }


def candidate_to_review_row(candidate: dict[str, Any], status: dict[str, Any] | None = None) -> dict[str, Any]:
    status = status or {}
    return {
        "candidate_object_id": candidate.get("candidate_object_id"),
        "korean_label": candidate.get("korean_label"),
        "label": candidate.get("label"),
        "source_domains": candidate.get("source_domains", []),
        "family": candidate.get("family"),
        "review_status": status.get("review_status", "unreviewed"),
        "recommended_action": status.get("recommended_action", "keep_as_candidate"),
        "priority": status.get("priority", "medium"),
        "reviewer_notes": status.get("reviewer_notes", ""),
        "promoted_to_object_id": status.get("promoted_to_object_id"),
        "reviewed_at": status.get("reviewed_at"),
    }


def generate_promotion_draft(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "object_id": candidate.get("candidate_object_id"),
        "label": candidate.get("label"),
        "korean_label": candidate.get("korean_label"),
        "object_type": "sensory_object_draft",
        "family": candidate.get("family"),
        "definition": candidate.get("definition"),
        "core_axes": candidate.get("core_axes", {}),
        "example_expressions": candidate.get("example_expressions", []),
        "related_objects": candidate.get("related_existing_objects", []),
        "opposite_objects": [],
        "associated_products": [],
        "evidence_refs": ["candidate_v1.1"],
        "status": "draft_from_candidate",
    }


def build_candidate_review_rows(
    candidates: list[dict[str, Any]],
    existing_objects: list[dict[str, Any]],
    review_status: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    review_status = review_status or {}
    rows: list[dict[str, Any]] = []
    for candidate in candidates:
        readiness = compute_candidate_readiness(candidate, existing_objects)
        status = dict(review_status.get(str(candidate["candidate_object_id"]), {}))
        status.setdefault("recommended_action", readiness["recommended_action"])
        row = candidate_to_review_row(candidate, status)
        row.update(readiness)
        rows.append(row)
    return rows


def summarize_candidate_actions(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(str(row.get("recommended_action", "keep_as_candidate")) for row in rows)
    return {action: counts.get(action, 0) for action in sorted(RECOMMENDED_ACTIONS)}


def generate_candidate_review_report(
    candidates: list[dict[str, Any]],
    existing_objects: list[dict[str, Any]],
    review_status: dict[str, dict[str, Any]] | None = None,
) -> str:
    rows = build_candidate_review_rows(candidates, existing_objects, review_status)
    action_counts = summarize_candidate_actions(rows)
    lookup = {candidate["candidate_object_id"]: candidate for candidate in candidates}

    lines = [
        "# Candidate Sensory Object Review Report",
        "",
        "## Summary",
        f"- Total candidates: {len(rows)}",
    ]
    for action, count in action_counts.items():
        lines.append(f"- {action}: {count}")

    high_priority = [row for row in rows if row.get("priority") == "high"]
    lines.extend(
        [
            "",
            "## High-Priority Candidates",
            "",
            "| candidate_object_id | korean_label | source_domains | recommended_action | readiness_score | note_dictionary_risk |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in high_priority:
        source_domains = ", ".join(row.get("source_domains", []))
        lines.append(
            f"| {row['candidate_object_id']} | {row['korean_label']} | {source_domains} | {row['recommended_action']} | {row['overall_readiness_score']:.2f} | {row['note_dictionary_risk']:.2f} |"
        )
    if not high_priority:
        lines.append("| - | - | - | - | - | - |")

    ready_rows = [row for row in rows if row["recommended_action"] == "ready_for_curated_merge"]
    lines.extend(["", "## Ready for Curated Merge"])
    if not ready_rows:
        lines.append("- No candidates currently recommended for curated merge.")
    for row in ready_rows:
        candidate = lookup[row["candidate_object_id"]]
        lines.extend(
            [
                "",
                f"### {candidate['candidate_object_id']} / {candidate.get('korean_label', '')}",
                f"- definition: {candidate.get('definition', '')}",
                f"- core axes: `{json.dumps(candidate.get('core_axes', {}), ensure_ascii=False)}`",
                f"- example expressions: {', '.join(candidate.get('example_expressions', []))}",
                f"- suggested phrase cues: {', '.join(candidate.get('suggested_phrase_cues', []))}",
                f"- negative cues: {', '.join(candidate.get('negative_cues', []))}",
                f"- related existing objects: {', '.join(candidate.get('related_existing_objects', []))}",
                f"- similar existing objects: {json.dumps(row.get('similar_existing_objects', []), ensure_ascii=False)}",
                "",
                "```json",
                json.dumps(generate_promotion_draft(candidate), ensure_ascii=False, indent=2),
                "```",
            ]
        )

    lines.extend(["", "## Needs Distinction Review"])
    distinction_rows = [row for row in rows if row["recommended_action"] == "needs_distinction_review"]
    if not distinction_rows:
        lines.append("- No candidates currently require distinction review.")
    for row in distinction_rows:
        lines.append(
            f"- {row['candidate_object_id']}: similar={json.dumps(row.get('similar_existing_objects', []), ensure_ascii=False)}"
        )

    lines.extend(["", "## Do Not Merge Yet"])
    do_not_merge_rows = [row for row in rows if row["recommended_action"] == "do_not_merge_yet"]
    if not do_not_merge_rows:
        lines.append("- No candidates currently marked do_not_merge_yet.")
    for row in do_not_merge_rows:
        lines.append(
            f"- {row['candidate_object_id']}: risk={row['note_dictionary_risk']:.2f}, readiness={row['overall_readiness_score']:.2f}"
        )

    return "\n".join(lines) + "\n"


def write_candidate_review_outputs(
    report_path: str | Path = "outputs/candidate_review_report.md",
    summary_path: str | Path = "outputs/candidate_review_summary.json",
) -> tuple[Path, Path, list[dict[str, Any]]]:
    candidates = load_candidate_objects()
    existing_objects = load_existing_objects()
    review_status = load_candidate_review_status()
    rows = build_candidate_review_rows(candidates, existing_objects, review_status)
    report = generate_candidate_review_report(candidates, existing_objects, review_status)

    resolved_report_path = _resolve(report_path)
    resolved_summary_path = _resolve(summary_path)
    resolved_report_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_summary_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_report_path.write_text(report, encoding="utf-8")
    resolved_summary_path.write_text(
        json.dumps(
            {
                "total_candidates": len(rows),
                "recommended_actions": summarize_candidate_actions(rows),
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return resolved_report_path, resolved_summary_path, rows
