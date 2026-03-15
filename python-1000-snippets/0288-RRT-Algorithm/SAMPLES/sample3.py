# sample3.py
# Simple RRT* variant: rewires nearby nodes to improve path cost.

import numpy as np


def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def steer(from_node, to_point, step_size=0.5):
    direction = np.array(to_point) - np.array(from_node)
    dist = np.linalg.norm(direction)
    if dist < step_size:
        return tuple(to_point)
    return tuple(np.array(from_node) + direction / dist * step_size)


def is_collision(node, obstacle_center, obstacle_radius):
    return distance(node, obstacle_center) < obstacle_radius


if __name__ == '__main__':
    np.random.seed(1)
    start = (0.0, 0.0)
    goal = (4.0, 4.0)
    obstacle_center = (2.0, 2.0)
    obstacle_radius = 0.7

    nodes = [start]
    parents = {start: None}
    cost = {start: 0.0}

    for _ in range(500):
        sample = tuple(np.random.random(2) * 5)
        nearest = min(nodes, key=lambda n: distance(n, sample))
        new_node = steer(nearest, sample, step_size=0.5)

        if is_collision(new_node, obstacle_center, obstacle_radius):
            continue

        # Find best parent among nearby nodes
        radius = 1.0
        neighbors = [n for n in nodes if distance(n, new_node) <= radius]
        best_parent = nearest
        best_cost = cost[nearest] + distance(nearest, new_node)
        for n in neighbors:
            c = cost[n] + distance(n, new_node)
            if c < best_cost:
                best_cost = c
                best_parent = n

        nodes.append(new_node)
        parents[new_node] = best_parent
        cost[new_node] = best_cost

        # Rewire nearby nodes
        for n in neighbors:
            new_cost = best_cost + distance(new_node, n)
            if new_cost < cost[n]:
                parents[n] = new_node
                cost[n] = new_cost

        if distance(new_node, goal) < 0.5:
            goal_node = new_node
            break
    else:
        goal_node = None

    if goal_node is not None:
        path = []
        node = goal_node
        while node is not None:
            path.append(node)
            node = parents[node]
        path.reverse()
        print('Found path length:', len(path))
        print('Path (first 5):', path[:5])
    else:
        print('No path found')
