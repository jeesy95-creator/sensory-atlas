from sensory_atlas.loaders import load_sensory_objects
from sensory_atlas.parser import parse_sentence
from sensory_atlas.ui_helpers import (
    evaluate_all_datasets,
    format_axis_value,
    get_object_lookup,
    objects_to_dataframe,
    parser_output_to_display_dict,
)


def test_objects_to_dataframe_has_required_columns() -> None:
    objects = load_sensory_objects()
    df = objects_to_dataframe(objects)

    assert not df.empty
    for column in ("object_id", "label", "korean_label", "family"):
        assert column in df.columns


def test_format_axis_value_handles_draft_values() -> None:
    assert format_axis_value("Cold") == "Cold"
    assert format_axis_value(["Clean", "Sharp"]) == "Clean, Sharp"
    assert format_axis_value(None) == ""


def test_parser_output_to_display_dict_contains_anchor_and_axes() -> None:
    objects = load_sensory_objects()
    lookup = get_object_lookup(objects)
    output = parse_sentence("해상도는 낮지만 분위기만 남아", objects)

    display = parser_output_to_display_dict(output, lookup)

    assert display["anchor"]
    assert display["axes"]
    assert "Rendering" in display["axes"]


def test_evaluate_all_datasets_returns_reports() -> None:
    reports = evaluate_all_datasets()

    assert set(reports) == {"default", "blind", "holdout"}
    assert reports["default"].total == 20
    assert reports["blind"].total == 30
    assert reports["holdout"].total == 50
