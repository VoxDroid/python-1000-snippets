# Breadth First Search

## Description
This snippet implements breadth-first search (BFS) on a graph using a queue to explore vertices level by level.

## Code
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
print("BFS Traversal:", bfs(graph, 0))
```

## Output
```
BFS Traversal: [0, 1, 2, 3]
```

## Explanation
- **BFS**: Explores all neighbors at the current depth before moving to the next level.
- **Queue**: Uses `deque` for FIFO processing of vertices.
- **Visited Set**: Prevents revisiting vertices.
- **Use Case**: Used in shortest path problems, social networks, or level-order traversal.
- **Best Practice**: Handle disconnected graphs and optimize for large graphs with adjacency lists.