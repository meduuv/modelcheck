from modelcheck import validate


def test_validate_reports_missing_fields():
    assert validate({"name": "demo"}) == ["version"]
