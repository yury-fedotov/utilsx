from utilsx.constants._time import HOURS_IN_YEAR, MINUTES_IN_WEEK


def test_time() -> None:
    """Test that time constants are mutually consistent."""
    assert HOURS_IN_YEAR == 8760
    assert MINUTES_IN_WEEK == 10080
