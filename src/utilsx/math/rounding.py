"""Utilities for various flavors of rounding, like ceiling."""

import math


def ceil_to_multiple(x: float, multiple: int) -> int:
    """Ceil a number to the next multiple of another value.

    Args:
        x: Number to ceil.
        multiple: Enforce the output to be a multiple of.

    Return:
        X input ceiled to the next multiple of another value.
    """
    return math.ceil(x / multiple) * multiple
