# sample3.py
# Compare A* with Manhattan and Euclidean heuristics on the same grid.

import heapq
import math


def astar(grid, start, goal, heuristic):
    rows = len(grid)
    cols = len(grid[0])

    def neighbors(node):
        x, y = node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                yield (nx, ny)

    open_set = [(heuristic(start, goal), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return list(reversed(path)), g_score[goal]

        for neighbor in neighbors(current):
            tentative = g_score[current] + 1
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative, neighbor))

    return None, float('inf')


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (4, 4)

    path_m, cost_m = astar(grid, start, goal, manhattan)
    path_e, cost_e = astar(grid, start, goal, euclidean)

    print('Manhattan heuristic path length:', len(path_m), 'cost:', cost_m)
    print('Euclidean heuristic path length:', len(path_e), 'cost:', cost_e)
