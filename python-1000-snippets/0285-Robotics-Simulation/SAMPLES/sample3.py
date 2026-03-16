# sample3.py
# Simple grid-based path planning (greedy) in a 2D occupancy grid.

import numpy as np


def greedy_path(start, goal, obstacles=None, max_steps=100):
    if obstacles is None:
        obstacles = set()

    current = start
    path = [current]
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while current != goal and len(path) < max_steps:
        dx = int(np.sign(goal[0] - current[0]))
        dy = int(np.sign(goal[1] - current[1]))

        # Candidate moves (prioritize reducing distance to goal)
        candidates = [
            (current[0] + dx, current[1]),
            (current[0], current[1] + dy),
            (current[0] - dx, current[1]),
            (current[0], current[1] - dy),
        ]

        best = None
        best_dist = manhattan(current, goal)
        for nxt in candidates:
            if nxt in obstacles or nxt == current:
                continue
            d = manhattan(nxt, goal)
            if d < best_dist:
                best = nxt
                best_dist = d

        if best is None:
            # Stuck, cannot improve distance
            break

        current = best
        path.append(current)

    return path


if __name__ == '__main__':
    start = (0, 0)
    goal = (5, 5)
    obstacles = {(2, y) for y in range(6)}  # vertical wall

    path = greedy_path(start, goal, obstacles=obstacles)

    print("Path length:", len(path))
    print("Path:", path)
