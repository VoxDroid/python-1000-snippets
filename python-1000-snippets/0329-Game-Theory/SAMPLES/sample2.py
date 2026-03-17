"""Simulate repeated Prisoner's Dilemma between two simple strategies."""

from typing import Callable, List, Tuple


def play_round(move_a: str, move_b: str) -> Tuple[int, int]:
    # Payoff matrix: (cooperate, cooperate)=(3,3), (cooperate, defect)=(0,5), (defect, cooperate)=(5,0), (defect, defect)=(1,1)
    payoff = {
        ('C', 'C'): (3, 3),
        ('C', 'D'): (0, 5),
        ('D', 'C'): (5, 0),
        ('D', 'D'): (1, 1),
    }
    return payoff[(move_a, move_b)]


def simulate(strategy_a: Callable[[List[str], List[str]], str], strategy_b: Callable[[List[str], List[str]], str], rounds: int = 5):
    history_a: List[str] = []
    history_b: List[str] = []
    score_a = 0
    score_b = 0

    for r in range(rounds):
        move_a = strategy_a(history_a, history_b)
        move_b = strategy_b(history_b, history_a)
        payoff_a, payoff_b = play_round(move_a, move_b)
        score_a += payoff_a
        score_b += payoff_b
        history_a.append(move_a)
        history_b.append(move_b)
        print(f"Round {r+1}: ({move_a}, {move_b}) payoffs=({payoff_a}, {payoff_b})")

    print(f"Total scores: A={score_a}, B={score_b}")


def tit_for_tat(own: List[str], opp: List[str]) -> str:
    return 'C' if not opp else opp[-1]


def always_defect(own: List[str], opp: List[str]) -> str:
    return 'D'


if __name__ == "__main__":
    simulate(tit_for_tat, always_defect, rounds=5)
