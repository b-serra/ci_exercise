"""Simple calculator module for CI demonstration."""

import os  # LINT ERROR: F401 - unused import
import sys  # LINT ERROR: F401 - unused import
import subprocess
from typing import List  # LINT ERROR: F401 - unused import


def add(a: float,b: float) -> float:
    """Add two numbers."""
    return a+b


def subtract(a: float,b: float) -> float:
    """Subtract b from a."""
    return a-b


def multiply(a: float,b: float) -> float:
    """Multiply two numbers."""
    # BUG: Wrong operation - should be multiplication, not addition!
    return a+b
    return a + b


def divide(a: float,b: float) -> float:
    """Divide a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b


def power(base, exponent):  # LINT ERROR: Missing type annotations (MyPy)
    """Raise base to the power of exponent."""
    result = base ** exponent
    unused_variable = 42  # LINT ERROR: F841 - local variable assigned but never used
    return result


def evaluate_expression(expression: str) -> float:
    """Evaluate a mathematical expression.

    SECURITY ISSUE: Uses eval() which can execute arbitrary code!
    Bandit B307: Use of possibly insecure function - eval()
    """
    # SECURITY BUG: Never use eval() with untrusted input!
    return eval(expression)


def run_calculation(calc_command: str) -> str:
    """Run a calculation command.

    SECURITY ISSUE: Uses shell=True which is vulnerable to injection!
    Bandit B602: subprocess call with shell=True
    """
    # SECURITY BUG: shell=True is dangerous with user input!
    result = subprocess.run(calc_command, shell=True, capture_output=True, text=True)
    return result.stdout


# SECURITY ISSUE: Hardcoded password
# Bandit B105: Possible hardcoded password
API_KEY = "sk-1234567890abcdef"  # SECURITY BUG: Never hardcode secrets!
DATABASE_PASSWORD = "admin123"  # SECURITY BUG: Never hardcode passwords!
