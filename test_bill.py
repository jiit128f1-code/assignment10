import pytest
from bill import calc, calc2
@pytest.mark.parametrize(
    ("units", "expected"),
    [
        (50, 177.0),
        (100, 354.0),
        (101, 359.9),
        (150, 649.0),
        (200, 944.0),
        (300, 1534.0),
        (301, 1543.44),
    ],
)
def test_household_bills(units, expected):
    assert calc("A", "x", units, "H", 0, 0) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("units", "expected"),
    [
        (50, 354.0),
        (100, 708.0),
        (101, 718.62),
        (150, 1239.0),
        (200, 1770.0),
        (300, 2832.0),
        (301, 2846.16),
    ],
)
def test_commercial_bills(units, expected):
    assert calc("A", "x", units, "C", 0, 0) == pytest.approx(expected)
