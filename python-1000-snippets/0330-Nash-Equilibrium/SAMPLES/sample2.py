"""Compute mixed-strategy Nash equilibrium in a 2x2 zero-sum game."""

from typing import Tuple


def mixed_strategy_zero_sum(a: float, b: float, c: float, d: float) -> Tuple[float, float]:
    """Compute (p, q) where p is row player's probability on first row and q is column player's probability on first column."""
    denom = a - b - c + d
    if denom == 0:
        # Degenerate; return 0.5, 0.5 as a fallback.
        return 0.5, 0.5
    p = (d - c) / denom
    q = (d - b) / denom
    return max(0.0, min(1.0, p)), max(0.0, min(1.0, q))


if __name__ == "__main__":
    # Example zero-sum matrix for row player:
    # [a b]
    # [c d]
    a, b, c, d = 1, -1, -1, 1  # matching pennies
    p, q = mixed_strategy_zero_sum(a, b, c, d)
    print(f"Mixed strategy (row): {p:.2f}, (col): {q:.2f}")
