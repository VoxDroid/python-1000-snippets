"""Simple English auction (ascending bid) simulation."""

import random
from typing import List, Tuple


def english_auction(valuations: List[float], start_price: float = 0.0, step: float = 1.0) -> Tuple[int, float]:
    # Each bidder bids as long as current price is below their valuation.
    price = start_price
    active = list(range(len(valuations)))

    while len(active) > 1:
        price += step
        active = [i for i in active if valuations[i] >= price]
    winner = active[0] if active else -1
    return winner, price


if __name__ == "__main__":
    random.seed(42)
    valuations = [random.uniform(10, 100) for _ in range(5)]
    winner, price = english_auction(valuations)
    print("Valuations:", [round(v, 2) for v in valuations])
    print("Winner Index:", winner, "Price:", round(price, 2))
