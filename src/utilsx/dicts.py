"""Utility functions for working with dictionaries."""

from collections import defaultdict
from collections.abc import Mapping
from typing import Any

from .typevars import NumberT, T


def rename_keys_in_nested_dict(
    dictionary: dict[str, Any], renaming: dict[str, str]
) -> dict[str, Any]:
    """Replace all specified keys by other specified names in an arbitrarily deep dictionary.

    Args:
        dictionary: A dictionary of arbitrary depth.
        renaming: A mapping from old to new key names.

    Returns:
        Copy of the original dictionary with ``old_key`` renamed to ``new_key``
        at all levels of key depth.
    """
    # This ``isinstance`` check is required to leave non-dict structures as-is.
    if isinstance(dictionary, dict):
        return {
            (renaming.get(key, key)): rename_keys_in_nested_dict(value, renaming)
            for key, value in dictionary.items()
        }
    return dictionary


def multiply_dict_values(dictionary: Mapping[T, float], multiplier: float) -> dict[T, float]:
    """Get a copy of the dictionary with values multiplied by scalar, preserving keys.

    Args:
        dictionary: A dictionary to multiply values of.
        multiplier: A scalar multiplier.

    Returns:
        A copy of the original dictionary with values multiplied by scalar.
    """
    return {key: value * multiplier for key, value in dictionary.items()}


def sum_dicts(*dicts: dict[T, float]) -> dict[T, float]:
    """Given dictionaries, return their summation: a union of keys and totals of values.

    Args:
        *dicts: To be added up together, any number.

    Returns:
        A combined dictionary with a union of keys and totals of values.
    """
    output: dict[T, float] = defaultdict(float)
    for dictionary in dicts:
        for key, value in dictionary.items():
            output[key] += value
    return output


def remove_pairs_with_zero_values(dictionary: dict[T, float]) -> dict[T, float]:
    """Drop key-value pairs from a dictionary whose values are zero.

    Args:
        dictionary: To be filtered to exclude key-value pairs with zero values.

    Returns:
        A subset of the original dictionary items, only pairs with non-zero values.
    """
    return {key: value for key, value in dictionary.items() if value}


def sort_by_value(dictionary: dict[T, NumberT], reverse: bool = False) -> dict[T, NumberT]:
    """Sort a dictionary with numeric values by those values.

    Args:
        dictionary: A dictionary to sort by value.
        reverse: False for ascending order, True for descending. Exactly matches the ``reverse``
            argument of ``sorted`` Python function.

    Returns:
        Same dictionary in terms of content, just sorted by value.
    """
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))
