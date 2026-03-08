# 0092-Floyd-Warshall-Algorithm Cheatsheet

- Input is adjacency matrix `graph[i][j]` with `inf` for no direct edge.
- Initialize `dist` copy of matrix, set `dist[i][i]=0`.
- Triple loop:
  ```python
  for k in range(V):
      for i in range(V):
          for j in range(V):
              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  ```
- After execution, `dist[i][j]` is shortest distance from i to j.
- Negative cycle detection: if any `dist[i][i] < 0` after algorithm, a negative cycle exists.
- To reconstruct paths, maintain `next[i][j]` and update alongside distances.
- O(V³) time; useful for dense graphs or when all pairs answers needed.
