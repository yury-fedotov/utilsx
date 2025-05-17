from collections.abc import Iterable

import pytest

from utilsx.exceptions import prohibit_negative_values


@pytest.mark.parametrize(
    ("values", "should_fail"),
    (
        ([0, 1, 2], False),
        ((0.0, 3.14, 100), False),
        ([], False),
        ([-1], True),
        (frozenset((0, -1, 2)), True),
        ([0.0, -3.14], True),
    ),
)
def test_prohibit_negative_values(values: Iterable[float], should_fail: bool) -> None:
    if should_fail:
        with pytest.raises(ValueError, match="prohibited"):
            prohibit_negative_values(values)
    else:
        prohibit_negative_values(values)
