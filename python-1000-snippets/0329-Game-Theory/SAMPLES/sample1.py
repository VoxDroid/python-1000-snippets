"""Find pure-strategy Nash equilibria in a 2-player normal-form game."""

from typing import List, Tuple


def find_pure_nash(row_payoffs: List[List[float]], col_payoffs: List[List[float]]) -> List[Tuple[int, int]]:
    n = len(row_payoffs)
    m = len(row_payoffs[0])
    equilibria: List[Tuple[int, int]] = []

    for i in range(n):
        for j in range(m):
            row_best = max(row_payoffs[i][k] for k in range(m))
            col_best = max(col_payoffs[k][j] for k in range(n))
            if row_payoffs[i][j] == row_best and col_payoffs[i][j] == col_best:
                equilibria.append((i, j))
    return equilibria


if __name__ == "__main__":
    # Prisoner's Dilemma (row: cooperate=0/defect=1, col: cooperate=0/defect=1)
    # Payoffs are (row, col)
    row_payoffs = [[3, 0], [5, 1]]
    col_payoffs = [[3, 5], [0, 1]]

    equilibria = find_pure_nash(row_payoffs, col_payoffs)
    print("Pure-strategy Nash equilibria:", equilibria)
