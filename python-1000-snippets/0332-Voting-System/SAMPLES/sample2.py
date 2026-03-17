"""Instant-runoff voting (IRV) / ranked-choice voting."""

from collections import Counter
from typing import List


def irv_winner(ballots: List[List[str]]) -> str:
    candidates = {c for ballot in ballots for c in ballot}
    while True:
        first_choices = [ballot[0] for ballot in ballots if ballot]
        counts = Counter(first_choices)
        if not counts:
            return ""
        winner, winner_votes = counts.most_common(1)[0]
        if winner_votes * 2 > sum(counts.values()):
            return winner
        # Eliminate lowest candidate(s)
        lowest_votes = min(counts.values())
        eliminated = {c for c, v in counts.items() if v == lowest_votes}
        ballots = [[c for c in ballot if c not in eliminated] for ballot in ballots]


if __name__ == "__main__":
    ballots = [
        ["A", "B", "C"],
        ["B", "C", "A"],
        ["C", "A", "B"],
        ["C", "B", "A"],
        ["B", "A", "C"],
    ]
    winner = irv_winner(ballots)
    print("IRV winner:", winner)
