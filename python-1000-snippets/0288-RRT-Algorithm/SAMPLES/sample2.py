# sample2.py
# RRT with goal bias and path extraction.

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


def build_rrt(start, goal, obstacle_center, obstacle_radius, iterations=500, goal_bias=0.05):
    nodes = [start]
    parent = {start: None}

    for _ in range(iterations):
        if np.random.random() < goal_bias:
            sample = goal
        else:
            sample = tuple(np.random.random(2) * 5)

        nearest = min(nodes, key=lambda n: distance(n, sample))
        new_node = steer(nearest, sample)

        if not is_collision(new_node, obstacle_center, obstacle_radius):
            nodes.append(new_node)
            parent[new_node] = nearest
            if distance(new_node, goal) < 0.5:
                return nodes, parent, new_node

    return nodes, parent, None


def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))


if __name__ == '__main__':
    np.random.seed(0)
    start = (0.0, 0.0)
    goal = (4.0, 4.0)
    obstacle_center = (2.0, 2.0)
    obstacle_radius = 0.7

    nodes, parent, last = build_rrt(start, goal, obstacle_center, obstacle_radius)
    if last is not None:
        path = reconstruct_path(parent, last)
        print('Path to goal found with RRT:', path)
    else:
        print('Goal not reached; nodes generated:', len(nodes))
