"""Utility function to sanitize a name by replacing invalid characters with a hyphen."""

import re


def sanitize_name(name: str) -> str:
    """Sanitize the name by replacing invalid characters with a hyphen."""
    sanitized = re.sub(r"[^a-zA-Z0-9_-]", "-", name)

    if not sanitized:
        raise ValueError("Name cannot be empty after sanitization")

    return sanitized
