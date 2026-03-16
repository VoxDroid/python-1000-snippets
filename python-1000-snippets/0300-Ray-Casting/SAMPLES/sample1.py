# sample1.py
# Ray casting in a 2D grid: find the first obstacle along a ray using Bresenham's algorithm.

import math


def bresenham_line(x0, y0, x1, y1):
    """Bresenham's line algorithm between two grid cells."""
    x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            yield x, y
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            yield x, y
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    yield x, y


def cast_ray(grid, origin, direction, max_dist=20):
    x0, y0 = origin
    x1 = x0 + direction[0] * max_dist
    y1 = y0 + direction[1] * max_dist
    for x, y in bresenham_line(x0, y0, x1, y1):
        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
            break
        if grid[y][x] == 1:
            return (x, y)
    return None


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    origin = (0, 2)
    direction = (1, 0.2)  # ray direction
    hit = cast_ray(grid, origin, direction)
    print('Ray hit at:', hit)
