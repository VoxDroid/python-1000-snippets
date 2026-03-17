"""Generate a multiplication table using nested list comprehensions."""

from typing import List


def multiplication_table(n: int) -> List[List[int]]:
    return [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    table = multiplication_table(5)
    print("Multiplication table (5x5):", table)
