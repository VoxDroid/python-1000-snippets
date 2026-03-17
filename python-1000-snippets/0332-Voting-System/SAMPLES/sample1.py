"""Plurality voting: candidate with most first-place votes wins."""

from collections import Counter


def plurality_winner(ballots):
    first_choices = [ballot[0] for ballot in ballots if ballot]
    count = Counter(first_choices)
    return count.most_common(1)[0][0]


if __name__ == "__main__":
    ballots = [
        ["A", "B", "C"],
        ["B", "A", "C"],
        ["A", "C", "B"],
        ["C", "A", "B"],
    ]
    winner = plurality_winner(ballots)
    print("Plurality winner:", winner)
