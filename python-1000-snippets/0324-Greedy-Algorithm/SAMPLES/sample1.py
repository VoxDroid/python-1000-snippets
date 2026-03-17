"""Greedy coin change for standard U.S. coins."""

from typing import List


def coin_change(coins: List[int], amount: int) -> List[int]:
    coins = sorted(coins, reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    return result


if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    amount = 67
    change = coin_change(coins, amount)
    print(f"Change for {amount}: {change}")
