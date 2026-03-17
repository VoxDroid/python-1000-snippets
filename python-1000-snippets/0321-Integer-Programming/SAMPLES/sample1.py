#!/usr/bin/env python3
"""Brute-force knapsack solver for small item sets."""

import itertools


def knapsack(values, weights, capacity):
    n = len(values)
    best_value = 0
    best_sel = None

    for bits in itertools.product([0, 1], repeat=n):
        total_weight = sum(w * b for w, b in zip(weights, bits))
        if total_weight > capacity:
            continue
        total_value = sum(v * b for v, b in zip(values, bits))
        if total_value > best_value:
            best_value = total_value
            best_sel = bits

    return best_value, list(best_sel)


def main():
    values = [5, 3, 4, 2]
    weights = [2, 1, 3, 2]
    capacity = 5

    best_value, best_items = knapsack(values, weights, capacity)
    print(f"Best knapsack value: {best_value}, items: {best_items}")


if __name__ == '__main__':
    main()
