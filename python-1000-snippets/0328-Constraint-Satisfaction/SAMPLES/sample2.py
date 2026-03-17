"""Solve a 4x4 Sudoku puzzle using backtracking."""

from typing import List, Optional


def is_valid(grid: List[List[int]], row: int, col: int, num: int) -> bool:
    # Row and column
    if any(grid[row][c] == num for c in range(4)):
        return False
    if any(grid[r][col] == num for r in range(4)):
        return False

    # 2x2 block
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for r in range(start_row, start_row + 2):
        for c in range(start_col, start_col + 2):
            if grid[r][c] == num:
                return False
    return True


def solve_sudoku(grid: List[List[int]]) -> Optional[List[List[int]]]:
    # Find next empty cell
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                for num in range(1, 5):
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num
                        res = solve_sudoku(grid)
                        if res is not None:
                            return res
                        grid[r][c] = 0
                return None
    return grid


if __name__ == "__main__":
    puzzle = [
        [1, 0, 0, 4],
        [0, 0, 1, 0],
        [0, 3, 0, 0],
        [2, 0, 0, 3],
    ]

    solution = solve_sudoku([row[:] for row in puzzle])
    print("Sudoku solved:")
    if solution:
        for row in solution:
            print(row)
    else:
        print("No solution found")
