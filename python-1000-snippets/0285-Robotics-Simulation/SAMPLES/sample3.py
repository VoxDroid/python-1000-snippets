# sample3.py
# Simple grid-based path planning (greedy) in a 2D occupancy grid.

import numpy as np


def greedy_path(start, goal, obstacles=None, max_steps=100):
    if obstacles is None:
        obstacles = set()

    current = start
    path = [current]
    while current != goal and len(path) < max_steps:
        dx = np.sign(goal[0] - current[0])
        dy = np.sign(goal[1] - current[1])

        # Prefer horizontal move first
        candidates = [(current[0] + dx, current[1]), (current[0], current[1] + dy)]
        moved = False
        for nxt in candidates:
            if nxt not in obstacles:
                current = nxt
                path.append(current)
                moved = True
                break
        if not moved:
            # No valid move; stop
            break

    return path


if __name__ == '__main__':
    start = (0, 0)
    goal = (5, 5)
    obstacles = {(2, y) for y in range(6)}  # vertical wall

    path = greedy_path(start, goal, obstacles=obstacles)

    print("Path length:", len(path))
    print("Path:", path)
