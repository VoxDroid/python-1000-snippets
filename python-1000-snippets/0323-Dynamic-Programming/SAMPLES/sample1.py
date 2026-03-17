"""Compute Fibonacci numbers using memoization (top-down DP)."""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 20
    print(f"Fibonacci({n}) = {fibonacci(n)}")
