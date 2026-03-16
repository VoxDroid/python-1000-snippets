# sample2.py
# Compute a visibility polygon from a point in a 2D grid using ray casting.

import math


def cast_ray(grid, origin, angle, max_dist=20):
    x0, y0 = origin
    dx = math.cos(angle)
    dy = math.sin(angle)
    for d in [i * 0.5 for i in range(int(max_dist * 2))]:
        x = x0 + dx * d
        y = y0 + dy * d
        xi = int(round(x))
        yi = int(round(y))
        if yi < 0 or yi >= len(grid) or xi < 0 or xi >= len(grid[0]):
            return (x, y)
        if grid[yi][xi] == 1:
            return (x, y)
    return (x0 + dx * max_dist, y0 + dy * max_dist)


if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    origin = (2.5, 2.5)
    points = []
    for angle in [i * math.pi / 8 for i in range(16)]:
        hit = cast_ray(grid, origin, angle)
        points.append(hit)

    print('Visibility polygon points:')
    for p in points:
        print('  ', p)
