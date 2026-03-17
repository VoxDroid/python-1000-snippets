"""Compute mixed-strategy Nash equilibrium for a general 2x2 game."""

from typing import Tuple


def mixed_strategy_2x2(row_payoff: Tuple[Tuple[float, float], Tuple[float, float]],
                      col_payoff: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    # Row player's mixed strategy p on row 1.
    # Column player's mixed strategy q on col 1.
    a, b = row_payoff[0]
    c, d = row_payoff[1]
    # Solve for q to make row player indifferent between row 1 and row 2.
    denom_row = (a - b - c + d)
    q = 0.5
    if denom_row != 0:
        q = (d - c) / denom_row

    # Solve for p to make column player indifferent between col 1 and col 2.
    e, f = col_payoff[0]
    g, h = col_payoff[1]
    denom_col = (e - f - g + h)
    p = 0.5
    if denom_col != 0:
        p = (h - g) / denom_col

    # Clamp probabilities to [0,1]
    p = max(0.0, min(1.0, p))
    q = max(0.0, min(1.0, q))

    return (p, 1 - p), (q, 1 - q)


if __name__ == "__main__":
    # Example 2x2 game (Battle of the Sexes)
    row_payoff = ((2, 0), (0, 1))
    col_payoff = ((1, 0), (0, 2))

    row_mix, col_mix = mixed_strategy_2x2(row_payoff, col_payoff)
    print(f"General 2x2 mixed equilibrium: row={row_mix}, col={col_mix}")
