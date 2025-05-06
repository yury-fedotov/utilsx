"""Tests for math functions."""

from collections.abc import Sequence

import pytest

from utilsx import ceil_to_multiple, normalize


@pytest.mark.parametrize(
    ("input_", "expected_output"),
    (
        ((0.5, 0.5), [0.5, 0.5]),
        ((3, 2), [0.6, 0.4]),
        ((0, 42), [0, 1]),
    ),
)
def test_normalize(input_: Sequence[float], expected_output: list[float]) -> None:
    assert normalize(input_) == expected_output


@pytest.mark.parametrize(
    ("x", "multiple", "expected"),
    (
        (23, 5, 25),
        (12, 7, 14),
        (47, 10, 50),
        (0, 5, 0),
        (-4, 3, -3),
        (-10, 4, -8),
        (15.2, 5, 20),
        (99, 1, 99),
        (100, 25, 100),
    ),
)
def test_ceil_to_multiple(x: float, multiple: int, expected: int) -> None:
    assert ceil_to_multiple(x, multiple) == expected
