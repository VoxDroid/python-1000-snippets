# sample1.py
# Simple RRT planner in a 2D world with circular obstacles.

import math
import random


def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def steer(from_pt, to_pt, max_dist):
    dist = distance(from_pt, to_pt)
    if dist <= max_dist:
        return to_pt
    ratio = max_dist / dist
    return (from_pt[0] + (to_pt[0] - from_pt[0]) * ratio,
            from_pt[1] + (to_pt[1] - from_pt[1]) * ratio)


def collides(point, obstacles, radius=0.1):
    for (ox, oy, r) in obstacles:
        if distance(point, (ox, oy)) <= r + radius:
            return True
    return False


def rrt(start, goal, obstacles, bounds, max_iters=500, step=0.5, goal_threshold=0.5):
    nodes = [start]
    parent = {start: None}

    for i in range(max_iters):
        rand = (random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1]))
        nearest = min(nodes, key=lambda p: distance(p, rand))
        new_pt = steer(nearest, rand, step)
        if collides(new_pt, obstacles):
            continue
        nodes.append(new_pt)
        parent[new_pt] = nearest

        if distance(new_pt, goal) < goal_threshold:
            parent[goal] = new_pt
            nodes.append(goal)
            break

    # reconstruct path
    if goal not in parent:
        return None
    path = [goal]
    cur = goal
    while parent[cur] is not None:
        cur = parent[cur]
        path.append(cur)
    return list(reversed(path))


def main() -> None:
    start = (0.5, 0.5)
    goal = (9.0, 9.0)
    obstacles = [(5, 5, 1.2), (7, 3, 0.8), (3, 7, 1.0)]
    bounds = ((0, 10), (0, 10))

    path = rrt(start, goal, obstacles, bounds)
    if path is None:
        print("No path found")
        return

    print("Path length:", len(path))
    print("First 3 points:", path[:3])
    print("Last 3 points:", path[-3:])


if __name__ == "__main__":
    main()
