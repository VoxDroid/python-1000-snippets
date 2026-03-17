"""Parse and filter a CSV-style grid using nested list comprehensions."""

from typing import List


def parse_grid(lines: List[str]) -> List[List[str]]:
    return [line.split(',') for line in lines]


def filter_grid(grid: List[List[str]], predicate) -> List[List[str]]:
    return [[cell for cell in row if predicate(cell)] for row in grid]


if __name__ == "__main__":
    lines = [
        "A,B,C",
        "D,E,F",
        "G,H,I",
    ]

    grid = parse_grid(lines)
    print("Parsed grid:", grid)

    filtered = filter_grid(grid, lambda v: v in {"A", "B", "E", "F"})
    print("Filtered grid:", filtered)
