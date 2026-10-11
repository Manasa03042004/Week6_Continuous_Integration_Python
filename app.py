"""Small calculator module used to demonstrate Python CI.

The module intentionally contains simple, deterministic functions so the CI
pipeline can validate style, behavior, and test reporting.
"""
from __future__ import annotations


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference between two numbers."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second


def divide(numerator: float, denominator: float) -> float:
    """Divide numerator by denominator, raising an error for zero."""
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return numerator / denominator


def main() -> None:
    """Run a short demonstration from the command line."""
    print("Python CI Demo — Calculator")
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    print(f"Division: 10 / 5 = {divide(10, 5)}")


if __name__ == "__main__":
    main()
