# sample1.py
# A* path planning on a 2D grid with obstacles.

import heapq


def astar(start, goal, grid):
    rows = len(grid)
    cols = len(grid[0])

    def neighbors(node):
        x, y = node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                yield (nx, ny)

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(0 + heuristic(start, goal), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            # reconstruct
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return list(reversed(path))

        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    return None


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

    path = astar(start, goal, grid)
    print('Path found:', path)
