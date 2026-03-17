"""Interval scheduling (activity selection) using greedy earliest finish time."""

from typing import List, Tuple


def select_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # Sort by end time
    intervals = sorted(intervals, key=lambda x: x[1])
    selected = []
    last_end = -float('inf')

    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


if __name__ == "__main__":
    intervals = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
    chosen = select_intervals(intervals)
    print("Selected intervals:", chosen)
