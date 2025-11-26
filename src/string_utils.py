"""String utility functions for CI demonstration."""

import pickle
import tempfile


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in s.split())


def load_string_from_file(data: bytes) -> str:
    """Load a string from pickled data.

    SECURITY ISSUE: pickle.loads can execute arbitrary code!
    Bandit B301: Pickle usage detected
    """
    # SECURITY BUG: Never unpickle untrusted data!
    return pickle.loads(data)


def create_temp_file(content: str) -> str:
    """Create a temporary file with content.

    SECURITY ISSUE: mktemp is insecure, use mkstemp instead!
    Bandit B306: Use of insecure mktemp function
    """
    # SECURITY BUG: mktemp has race condition vulnerabilities!
    filename = tempfile.mktemp()
    with open(filename, "w") as f:
        f.write(content)
    return filename
