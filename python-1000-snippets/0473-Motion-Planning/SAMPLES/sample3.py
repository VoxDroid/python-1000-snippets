# sample3.py
# Potential field planning that moves from start towards goal while avoiding obstacles.

import math


def potential_field(start, goal, obstacles, steps=50, alpha=1.0, beta=100.0, step_size=0.2):
    pos = list(start)
    path = [tuple(pos)]

    for _ in range(steps):
        # Attractive force toward the goal
        dx = goal[0] - pos[0]
        dy = goal[1] - pos[1]
        dist_goal = math.hypot(dx, dy) + 1e-8
        force_x = alpha * dx / dist_goal
        force_y = alpha * dy / dist_goal

        # Repulsive forces from obstacles
        for ox, oy, radius in obstacles:
            dx_o = pos[0] - ox
            dy_o = pos[1] - oy
            dist_o = math.hypot(dx_o, dy_o) - radius
            if dist_o <= 0:
                dist_o = 1e-3
            if dist_o < 1.0:
                rep = beta * (1.0 / dist_o**2)
                force_x += rep * dx_o / (dist_o + 1e-8)
                force_y += rep * dy_o / (dist_o + 1e-8)

        norm = math.hypot(force_x, force_y) + 1e-8
        pos[0] += step_size * force_x / norm
        pos[1] += step_size * force_y / norm
        path.append(tuple(pos))

        if math.hypot(goal[0] - pos[0], goal[1] - pos[1]) < 0.1:
            break

    return path


def main() -> None:
    start = (0.0, 0.0)
    goal = (5.0, 5.0)
    obstacles = [(2.5, 2.5, 0.7), (3.5, 1.5, 0.5)]

    path = potential_field(start, goal, obstacles)
    print("Generated path length:", len(path))
    print("First 3 points:", path[:3])
    print("Last 3 points:", path[-3:])


if __name__ == "__main__":
    main()
