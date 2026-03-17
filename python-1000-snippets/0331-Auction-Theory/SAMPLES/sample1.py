"""First-price sealed-bid auction simulation."""

import numpy as np


def first_price_auction(bids: np.ndarray) -> int:
    return int(np.argmax(bids))


if __name__ == "__main__":
    np.random.seed(42)
    bids = np.random.randint(10, 100, 5)
    winner = first_price_auction(bids)
    price = bids[winner]
    print("Bids:", bids.tolist())
    print("Winner Index:", winner, "Price:", price)
