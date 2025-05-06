"""Utilities for text transformations."""


def add_suffix(base: str, suffix: str, separator: str = "_") -> str:
    """Add suffix to a base string using a separator.

    If the suffix is empty, simply return the base string, do not add separator.
    """
    return f"{base}{separator}{suffix}" if suffix else base
