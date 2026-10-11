"""Automated tests for the calculator CI demonstration."""
import pytest

from app import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(first, second, expected):
    assert add(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [(5, 3, 2), (3, 5, -2), (0, 0, 0)],
)
def test_subtract(first, second, expected):
    assert subtract(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [(2, 3, 6), (-2, 3, -6), (2.5, 4, 10.0)],
)
def test_multiply(first, second, expected):
    assert multiply(first, second) == expected


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [(10, 2, 5), (9, 3, 3), (-8, 2, -4), (5, 2, 2.5)],
)
def test_divide(numerator, denominator, expected):
    assert divide(numerator, denominator) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_by_zero_is_not_silently_accepted():
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)
