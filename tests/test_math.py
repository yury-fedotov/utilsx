from collections.abc import Sequence

import pytest

from utilsx import ceil_to_multiple, double, halve, normalize


@pytest.mark.parametrize(
    ("x", "expected"),
    (
        (10, 5),
        (3, 1.5),
        (0, 0),
        (-8, -4),
        (-3.6, -1.8),
        (7.5, 3.75),
        (1, 0.5),
        (-1, -0.5),
        (1000000, 500000),
    ),
)
def test_halve(x: float, expected: float) -> None:
    assert halve(x) == expected


@pytest.mark.parametrize(
    ("x", "expected"),
    (
        (10, 20),
        (3, 6),
        (0, 0),
        (-8, -16),
        (-3.6, -7.2),
        (7.5, 15),
        (1, 2),
        (-1, -2),
        (1000000, 2000000),
    ),
)
def test_double(x: float, expected: float) -> None:
    assert double(x) == expected


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
