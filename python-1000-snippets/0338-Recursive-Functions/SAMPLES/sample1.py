"""Compute factorial with memoization to avoid repeated recursion."""

from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print("Factorial(10):", factorial(10))
    # Show that memoization speeds up repeated calls
    print("Factorial(10) again:", factorial(10))
