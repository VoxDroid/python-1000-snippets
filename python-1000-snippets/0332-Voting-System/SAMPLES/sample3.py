"""Borda count voting system."""

from collections import Counter
from typing import List


def borda_count(ballots: List[List[str]]) -> str:
    scores = Counter()
    for ballot in ballots:
        for rank, candidate in enumerate(ballot[::-1]):
            scores[candidate] += rank + 1
    # Higher score wins
    return scores.most_common(1)[0][0]


if __name__ == "__main__":
    ballots = [
        ["A", "B", "C"],
        ["B", "A", "C"],
        ["C", "B", "A"],
        ["B", "A", "C"],
    ]
    winner = borda_count(ballots)
    print("Borda winner:", winner)
