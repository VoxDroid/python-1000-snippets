"""Second-price (Vickrey) auction simulation."""

import numpy as np


def vickrey_auction(bids: np.ndarray) -> (int, int):
    winner = int(np.argmax(bids))
    sorted_bids = np.sort(bids)
    price = int(sorted_bids[-2]) if len(bids) > 1 else int(bids[0])
    return winner, price


if __name__ == "__main__":
    np.random.seed(42)
    bids = np.random.randint(10, 100, 5)
    winner, price = vickrey_auction(bids)
    print("Bids:", bids.tolist())
    print("Winner Index:", winner, "Price paid (2nd highest):", price)
