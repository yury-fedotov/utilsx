"""Utilities for enhancing your Pandas workflows."""

from importlib import import_module

_MODULE_DEPENDENCIES = frozenset(("pandas",))

for dependency in _MODULE_DEPENDENCIES:
    try:
        import_module(dependency)
    except ImportError as e:
        raise ImportError(
            "Optional dependency group 'pandas' is required for this feature.\n"
            "Add 'utilsx[pandas]' to your requirements list and install to virtual environment."
        ) from e

# This import should be after the dependency group check logic.
from ._missing import *  # noqa: E402
