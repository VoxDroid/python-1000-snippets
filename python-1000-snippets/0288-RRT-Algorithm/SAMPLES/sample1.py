# sample1.py
# Basic RRT implementation in 2D with a single circular obstacle.

import numpy as np


def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def steer(from_node, to_point, step_size=0.5):
    direction = np.array(to_point) - np.array(from_node)
    dist = np.linalg.norm(direction)
    if dist < step_size:
        return tuple(to_point)
    return tuple(np.array(from_node) + direction / dist * step_size)


def collision(node, obstacle_center, obstacle_radius):
    return distance(node, obstacle_center) < obstacle_radius


if __name__ == '__main__':
    np.random.seed(42)
    start = (0.0, 0.0)
    goal = (4.0, 4.0)
    obstacle_center = (2.0, 2.0)
    obstacle_radius = 0.7

    nodes = [start]
    goal_reached = False

    for _ in range(200):
        rand = tuple(np.random.random(2) * 5)
        nearest = min(nodes, key=lambda n: distance(n, rand))
        new_node = steer(nearest, rand, step_size=0.5)

        if not collision(new_node, obstacle_center, obstacle_radius):
            nodes.append(new_node)
            if distance(new_node, goal) < 0.5:
                goal_reached = True
                break

    print('Goal reached:', goal_reached)
    print('Number of nodes:', len(nodes))
    print('Last node:', nodes[-1])
