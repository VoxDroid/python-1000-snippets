"""0/1 Knapsack using branch-and-bound with fractional knapsack upper bound."""

from typing import List, Tuple


def knapsack_branch_and_bound(values: List[int], weights: List[int], capacity: int) -> int:
    n = len(values)
    items = sorted(zip(values, weights), key=lambda vw: vw[0] / vw[1], reverse=True)

    best_value = 0

    def bound(i: int, current_value: int, remaining_capacity: int) -> float:
        # Compute optimistic upper bound using fractional knapsack
        value = current_value
        cap = remaining_capacity
        for v, w in items[i:]:
            if cap <= 0:
                break
            take = min(w, cap)
            value += take * (v / w)
            cap -= take
        return value

    def search(i: int, current_value: int, remaining_capacity: int):
        nonlocal best_value
        if i == n or remaining_capacity == 0:
            best_value = max(best_value, current_value)
            return

        # Prune if bound cannot beat current best
        if bound(i, current_value, remaining_capacity) <= best_value:
            return

        v, w = items[i]
        # Branch: include item
        if w <= remaining_capacity:
            search(i + 1, current_value + v, remaining_capacity - w)
        # Branch: exclude item
        search(i + 1, current_value, remaining_capacity)

    search(0, 0, capacity)
    return best_value


if __name__ == "__main__":
    values = [6, 10, 12]
    weights = [1, 2, 3]
    capacity = 5
    best = knapsack_branch_and_bound(values, weights, capacity)
    print("Best knapsack value:", best)
