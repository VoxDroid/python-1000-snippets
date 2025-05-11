# A Star Algorithm

## Description
This snippet demonstrates the A* pathfinding algorithm.

## Code
```python
from heapq import heappush, heappop
grid = [[0]*5 for _ in range(5)]
grid[2][2] = 1  # Obstacle
start, goal = (0, 0), (4, 4)
queue = [(0, start)]
came_from = {}
g_score = {start: 0}
while queue:
    _, current = heappop(queue)
    if current == goal:
        break
    x, y = current
    for nx, ny in [(x+1, y), (x, y+1)]:
        if 0 <= nx < 5 and 0 <= ny < 5 and grid[nx][ny] == 0:
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get((nx, ny), float("inf")):
                came_from[(nx, ny)] = current
                g_score[(nx, ny)] = tentative_g
                f_score = tentative_g + abs(nx - goal[0]) + abs(ny - goal[1])
                heappush(queue, (f_score, (nx, ny)))
path = []
current = goal
while current in came_from:
    path.append(current)
    current = came_from[current]
path.append(start)
print("Path:", path[::-1])
```

## Output
```
Path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
```

## Explanation
- **A Star Algorithm**: Finds the shortest path using a heuristic-guided search.
- **Logic**: Uses a priority queue to explore nodes with lowest estimated cost.
- **Complexity**: O(r*c*log(r*c)) for r rows, c columns.
- **Use Case**: Used for navigation in robotics or games.
- **Best Practice**: Optimize heuristic; handle edge cases; validate grid.