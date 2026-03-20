# sample1.py
# Simple AI agent that moves toward a goal on a grid while avoiding obstacles.

import random


def best_move(position, goal, obstacles, grid_size=(10, 10)):
    x, y = position
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    candidates = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size[0] and 0 <= ny < grid_size[1] and (nx, ny) not in obstacles:
            dist = abs(goal[0] - nx) + abs(goal[1] - ny)
            candidates.append(((nx, ny), dist))
    if not candidates:
        return position
    # choose move that minimizes distance to goal
    candidates.sort(key=lambda item: item[1])
    best = candidates[0][0]
    # if multiple, pick randomly among best
    best_dist = candidates[0][1]
    bests = [p for p, d in candidates if d == best_dist]
    return random.choice(bests)


def main() -> None:
    start = (0, 0)
    goal = (9, 9)
    obstacles = {(4, 4), (4, 5), (5, 4), (6, 6)}

    pos = start
    path = [pos]
    for _ in range(50):
        if pos == goal:
            break
        pos = best_move(pos, goal, obstacles)
        path.append(pos)

    print("Path length:", len(path))
    print("Path sample:", path[:5], "...", path[-3:])


if __name__ == "__main__":
    main()
