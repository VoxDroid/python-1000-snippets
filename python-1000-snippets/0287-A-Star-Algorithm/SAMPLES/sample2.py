# sample2.py
# A* search on a weighted grid (non-uniform move cost).

import heapq


def astar_weighted(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node):
        x, y = node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] >= 0:
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
            tentative = g_score[current] + grid[neighbor[0]][neighbor[1]]
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative, neighbor))

    return None, float('inf')


if __name__ == '__main__':
    # -1 represents obstacle, positive values represent movement cost
    grid = [
        [1, 1, 1, 1, 1],
        [1, -1, -1, -1, 1],
        [1, 1, 5, -1, 1],
        [1, -1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    start = (0, 0)
    goal = (4, 4)

    path, cost = astar_weighted(grid, start, goal)
    print('Weighted path:', path)
    print('Total movement cost:', cost)
