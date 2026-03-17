"""Use nested list comprehensions to build a matrix and compute its transpose."""

from typing import List


def build_matrix(rows: int, cols: int) -> List[List[int]]:
    return [[i * cols + j for j in range(cols)] for i in range(rows)]


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = build_matrix(3, 4)
    print("Matrix:", matrix)
    print("Transpose:", transpose(matrix))
