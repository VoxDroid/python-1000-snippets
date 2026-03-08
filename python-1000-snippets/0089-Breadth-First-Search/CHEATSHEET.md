# 0089-Breadth-First-Search Cheatsheet

- BFS uses a queue to visit neighbors level-by-level.
- Pseudocode:
  ```python
  visited = set([start])
  q = deque([start])
  while q:
      v = q.popleft()
      for nbr in graph[v]:
          if nbr not in visited:
              visited.add(nbr)
              q.append(nbr)
  ```
- Use for shortest path in unweighted graph: record parent pointers.
- Can perform level-order traversal of trees using same pattern.
- Complexity: O(V + E) for adjacency list representation.
- For disconnected graphs, loop over all nodes and initiate BFS if unvisited.
