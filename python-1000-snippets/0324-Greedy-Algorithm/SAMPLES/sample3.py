"""Fractional knapsack using greedy value/weight ratio."""

from typing import List, Tuple


def fractional_knapsack(values: List[float], weights: List[float], capacity: float) -> float:
    items = sorted(
        zip(values, weights), key=lambda vw: vw[0] / vw[1], reverse=True
    )
    total_value = 0.0
    remaining = capacity

    for value, weight in items:
        if remaining <= 0:
            break
        take = min(weight, remaining)
        total_value += take * (value / weight)
        remaining -= take

    return total_value


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    best = fractional_knapsack(values, weights, capacity)
    print("Fractional knapsack value:", best)
