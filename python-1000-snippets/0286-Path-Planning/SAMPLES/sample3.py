# sample3.py
# Dijkstra's algorithm for path planning in a weighted grid.

import heapq


def dijkstra(start, goal, grid, weights):
    rows = len(grid)
    cols = len(grid[0])

    def neighbors(node):
        x, y = node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not grid[nx][ny]:
                yield (nx, ny)

    dist = {start: 0}
    prev = {start: None}
    pq = [(0, start)]

    while pq:
        d, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = prev[current]
            return list(reversed(path)), d

        if d > dist.get(current, float('inf')):
            continue

        for neigh in neighbors(current):
            nd = d + weights[neigh[0]][neigh[1]]
            if nd < dist.get(neigh, float('inf')):
                dist[neigh] = nd
                prev[neigh] = current
                heapq.heappush(pq, (nd, neigh))

    return None, float('inf')


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    weights = [[1 for _ in row] for row in grid]
    weights[2][2] = 5  # heavier cost

    start = (0, 0)
    goal = (4, 4)

    path, cost = dijkstra(start, goal, grid, weights)
    print('Path found by Dijkstra:', path)
    print('Total cost:', cost)
