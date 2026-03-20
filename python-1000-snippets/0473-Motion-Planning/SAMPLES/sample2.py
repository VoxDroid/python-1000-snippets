# sample2.py
# A* search on a grid with obstacles.

import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(node, grid):
    x, y = node
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == 0:
                yield (nx, ny)


def a_star(start, goal, grid):
    open_set = [(0, start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return list(reversed(path))

        for n in neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(n, float('inf')):
                g_score[n] = tentative_g
                priority = tentative_g + heuristic(n, goal)
                heapq.heappush(open_set, (priority, n))
                came_from[n] = current
    return None


def main() -> None:
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (5, 5)

    path = a_star(start, goal, grid)
    if path is None:
        print("No path found")
        return

    print("A* path length:", len(path))
    print("Sample path:", path[:5], "...", path[-3:])


if __name__ == "__main__":
    main()
