# 0090-Dijkstra-Algorithm Cheatsheet

- Dijkstra computes shortest paths from a source in a weighted graph with non‑negative weights.
- Uses a priority queue (min‑heap) storing `(distance, vertex)` pairs.
- Initialize all distances to ∞ except start set to 0.
- Relax edges: when exploring vertex u, for each neighbor v with weight w:
  ```python
  if dist[u] + w < dist[v]:
      dist[v] = dist[u] + w
      heapq.heappush(pq, (dist[v], v))
  ```
- To reconstruct paths, maintain a `prev` dictionary mapping each vertex to its predecessor.
- Time complexity O((V+E) log V) with binary heap.
- Do not use with negative weights; Bellman–Ford is alternative.
