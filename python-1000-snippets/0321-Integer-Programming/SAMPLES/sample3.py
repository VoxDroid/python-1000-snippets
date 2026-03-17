#!/usr/bin/env python3
"""Simple scheduling problem solved by enumeration."""

import itertools


def schedule_value(assignments, values):
    return sum(values[i][a] for i, a in enumerate(assignments))


def is_valid(assignments, conflict_pairs):
    for a, b in conflict_pairs:
        if assignments[a] == assignments[b]:
            return False
    return True


def main():
    # 3 tasks, 2 machines
    values = [
        [3, 1],  # task 0
        [2, 4],  # task 1
        [5, 2],  # task 2
    ]
    conflict_pairs = [(0, 1)]  # tasks that can't be on same machine

    best_val = -float('inf')
    best_assign = None
    for assign in itertools.product(range(2), repeat=3):
        if not is_valid(assign, conflict_pairs):
            continue
        val = schedule_value(assign, values)
        if val > best_val:
            best_val = val
            best_assign = assign

    print(f"Best schedule value: {best_val}, assignment: {list(best_assign)}")


if __name__ == '__main__':
    main()
