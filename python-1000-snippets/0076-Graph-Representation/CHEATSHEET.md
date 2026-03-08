# 0076-Graph-Representation Cheatsheet

- Use a dictionary mapping vertices to neighbor lists for adjacency lists.
- For directed graphs, only append edge one way; for undirected, append both ways.
- Example edge addition:
  ```python
  graph.setdefault(u, []).append(v)
  graph.setdefault(v, []).append(u)  # undirected
  ```
- Traversals:
  - **BFS** (breadth-first search) uses a queue.
  - **DFS** (depth-first search) can be recursive or use a stack.
- Utility functions:
  - `bfs(start)` returns order visited.
  - `dfs(start)` returns order visited.
  - `find_path(u, v)` returns a path list if exists.

## Quick example

```python
order = g.bfs(0)
path = g.find_path(0, 2)
```