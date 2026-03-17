"""Solve the N-Queens problem using backtracking."""

from typing import List


def solve_n_queens(n: int) -> List[List[int]]:
    solutions: List[List[int]] = []
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c

    def backtrack(row: int, state: List[int]):
        if row == n:
            solutions.append(state.copy())
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            state.append(col)

            backtrack(row + 1, state)

            state.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0, [])
    return solutions


if __name__ == "__main__":
    n = 4
    sols = solve_n_queens(n)
    print(f"Solutions for {n}-Queens: {len(sols)}")
