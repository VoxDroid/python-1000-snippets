# Depth First Search

## Description
This snippet implements depth-first search (DFS) on a graph using recursion to explore all vertices.

## Code
```python
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    result = [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
print("DFS Traversal:", dfs(graph, 0))
```

## Output
```
DFS Traversal: [0, 1, 2, 3]
```

## Explanation
- **DFS**: Explores as far as possible along each branch before backtracking.
- **Recursion**: Visits a vertex, marks it, and recursively explores unvisited neighbors.
- **Visited Set**: Prevents revisiting vertices in cycles.
- **Use Case**: Used in pathfinding, cycle detection, or topological sorting.
- **Best Practice**: Handle disconnected graphs by running DFS on all unvisited vertices.