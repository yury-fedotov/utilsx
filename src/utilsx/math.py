"""Utility functions for mathematical operations."""

import math
from collections.abc import Collection, Sequence
from typing import Literal

from utilsx.constants import MILLION, THOUSAND

_TUnits = Literal["thousand", "million"]


def halve(x: float) -> float:
    """Divide a number by two. In other words, get its half."""
    return x / 2


def double(x: float) -> float:
    """Multiply a number by two. In other words, double it."""
    return x * 2


def convert_number_to_units(number: float, units: _TUnits) -> float:
    """Convert a number to thousands or millions.

    Args:
        number: Number to convert.
        units: Units to convert to.

    Returns:
        A number converted to specified units.
    """
    match units:
        case "thousand":
            denominator = THOUSAND
        case "million":
            denominator = MILLION
        case _:
            raise ValueError(f"Unrecognized units: {units}")

    return number / denominator


def check_values_add_up_to_one(
    values: Collection[float],
    mode: Literal["fractions", "percentages", "either"] = "either",
) -> bool:
    """Check if values in a collection add up to 1 or 100.

    Args:
        values: Values to check.
        mode: "fractions" if they should add up to 1, "percentages" if they should add up to 100,
            "either" if either of this works.

    Returns:
        Boolean outcome of the check.
    """
    match mode:
        case "fractions":
            valid_totals = frozenset((1,))
        case "percentages":
            valid_totals = frozenset((100,))
        case "either":
            valid_totals = frozenset((1, 100))
        case _:
            raise ValueError(f"Unrecognized mode: {mode}")

    sum_of_values = sum(values)
    return any(
        math.isclose(sum_of_values, valid_total, rel_tol=0.001) for valid_total in valid_totals
    )


def normalize(values: Sequence[float]) -> list[float]:
    """Normalize a sequence of numbers to make them add up to one."""
    return [value / sum(values) for value in values]


def safe_divide(numerator: float, denominator: float, fallback: float = 0) -> float:
    """Divide one number by another, falling back on something in case of ``ZeroDivisionError``.

    Args:
        numerator: Number to divide.
        denominator: Denominator to use.
        fallback: Fallback value to use in case the denominator is zero, defaults to zero.
    """
    return numerator / denominator if denominator != 0 else fallback


def ceil_to_multiple(x: float, multiple: int) -> int:
    """Ceil a number to the next multiple of another value.

    Args:
        x: Number to ceil.
        multiple: Enforce the output to be a multiple of.

    Return:
        X input ceiled to the next multiple of another value.
    """
    return math.ceil(x / multiple) * multiple
