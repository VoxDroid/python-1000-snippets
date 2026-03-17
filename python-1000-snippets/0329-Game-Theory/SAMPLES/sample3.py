"""Compute the minimax value for a zero-sum game payoff matrix."""

from typing import List


def minimax_value(payoff: List[List[float]]) -> float:
    # Row player wants to maximize; Column player wants to minimize the payoff.
    # Row player's maximin (lower bound): max over rows of the row minimum.
    maximin = max(min(row) for row in payoff)
    # Column player's minimax (upper bound): min over columns of the column maximum.
    minimax = min(max(payoff[r][c] for r in range(len(payoff))) for c in range(len(payoff[0])))
    # In zero-sum games, maximin <= minimax. If equal, pure strategy value exists.
    return (maximin + minimax) / 2


if __name__ == "__main__":
    matrix = [
        [3, 0],
        [5, 1],
    ]
    value = minimax_value(matrix)
    print("Minimax value (row player):", value)
