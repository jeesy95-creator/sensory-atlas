from sensory_atlas.loaders import load_sensory_objects
from sensory_atlas.parser import parse_sentence


def test_parser_output_includes_axis_evidence_fields() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("비 온 뒤 숲 바닥처럼 축축하고 초록빛이 도는 향", objects)
    payload = result.model_dump()

    assert "axis_evidence" in payload
    assert "axis_confidence" in payload
    assert "clarification_questions" in payload


def test_clear_sensory_terms_produce_axis_evidence() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("비 온 뒤 숲 바닥처럼 축축하고 초록빛이 도는 향", objects)

    assert result.axis_evidence
    assert set(result.axis_evidence) & {"moisture", "organic", "texture", "atmosphere"}


def test_axis_confidence_values_are_bounded() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("차갑고 투명한 유리 같은 향", objects)

    assert result.axis_confidence
    assert all(0.0 <= value <= 1.0 for value in result.axis_confidence.values())


def test_more_axis_evidence_increases_axis_confidence() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("차갑고 서늘하고 냉랭하게 선명한 향", objects)

    assert result.axis_confidence["temperature"] > result.axis_confidence.get("density", 0.0)


def test_ambiguous_low_confidence_input_produces_clarification_questions() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("좋은데 설명하기 어려운 향", objects)

    assert result.clarification_questions
    assert len(result.clarification_questions) <= 3
    assert all(question.endswith("요?") for question in result.clarification_questions)


def test_clear_high_confidence_input_can_skip_clarification_questions() -> None:
    objects = load_sensory_objects()
    result = parse_sentence("해상도는 낮지만 분위기만 남아", objects)

    assert result.anchor_object is not None
    assert result.anchor_object.object_id == "film_grain"
    assert result.clarification_questions == []
