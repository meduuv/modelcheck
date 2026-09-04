"""Validate minimal model metadata."""


def validate(model: dict, required: tuple[str, ...] = ("name", "version")) -> list[str]:
    """Return missing required fields without modifying the input."""
    return [key for key in required if not str(model.get(key, "")).strip()]
