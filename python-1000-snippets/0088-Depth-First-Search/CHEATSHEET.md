# 0088-Depth-First-Search Cheatsheet

- DFS explores graph by going deep along each branch before backtracking.
- Two common implementations:
  - **Recursive**: simple, uses call stack.
  - **Iterative**: use explicit `stack` list.
- Maintain a `visited` set to avoid cycles.
- For disconnected graphs, loop over all vertices and call DFS if unvisited.
- Useful for:
  - Connectivity checks
  - Cycle detection (add recursion stack)
  - Topological sort (on DAG)
  - Solving mazes / puzzles.
- Pseudocode:
  ```python
  def dfs(u):
      visited.add(u)
      for v in neighbors(u):
          if v not in visited:
              dfs(v)
  ```
