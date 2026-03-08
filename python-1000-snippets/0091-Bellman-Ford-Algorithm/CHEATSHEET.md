# 0091-Bellman-Ford-Algorithm Cheatsheet

- Bellman-Ford computes shortest paths from source, supporting negative edge weights.
- Initialize distances to ∞, source 0.
- Repeat relaxation for all edges `|V|-1` times:
  ```python
  for _ in range(len(graph)-1):
      for u in graph:
          for v,w in graph[u]:
              if dist[u] + w < dist[v]:
                  dist[v] = dist[u] + w
  ```
- After relaxations, scan edges once more to detect negative cycles; if any distance can still decrease, cycle exists.
- Path reconstruction similar to Dijkstra: maintain `prev` map during relaxation.
- Complexity O(V*E); slower than Dijkstra but handles negatives.
- Avoid graphs with negative cycles; algorithm returns None or raises error.
