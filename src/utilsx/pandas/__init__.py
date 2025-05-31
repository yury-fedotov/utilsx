"""Utilities for enhancing your Pandas workflows."""

try:
    import pandas as pd
except ImportError as e:
    raise ImportError(
        "Optional dependency 'pandas' is required for this feature.\n"
        "Add 'utilsx[pandas]' to your requirements list."
    ) from e

from ._missing import *
