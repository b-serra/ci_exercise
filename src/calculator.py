"""Simple calculator module for CI demonstration."""

import os  # LINT ERROR: F401 - unused import
import sys  # LINT ERROR: F401 - unused import
from typing import List  # LINT ERROR: F401 - unused import


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):  # LINT ERROR: Missing type annotations (MyPy)
    """Raise base to the power of exponent."""
    result = base ** exponent
    unused_variable = 42  # LINT ERROR: F841 - local variable assigned but never used
    return result
