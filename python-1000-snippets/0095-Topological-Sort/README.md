# Topological Sort

## Description
This snippet implements topological sorting for a directed acyclic graph (DAG) using depth-first search.

## Code
```python
def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print("Topological Order:", topological_sort(graph))
```

## Output
```
Topological Order: [0, 2, 1, 3]
```

## Explanation
- **Topological Sort**: Orders vertices such that if there’s an edge from u to v, u comes before v.
- **DFS**: Explores each vertex, adding it to a stack after visiting all its neighbors.
- **Complexity**: O(V + E) time, O(V) space.
- **Use Case**: Used in task scheduling, course prerequisites, or build systems.
- **Best Practice**: Detect cycles to ensure the graph is a DAG.