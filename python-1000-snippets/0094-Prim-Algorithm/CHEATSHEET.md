# 0094-Prim-Algorithm Cheatsheet

- Prim’s builds MST by starting at a vertex and repeatedly adding the smallest edge that connects visited set to unvisited vertices.
- Use `heapq` to maintain candidate edges `(weight,u,v)`.
- Maintain a `visited` set to avoid cycles.
- Pseudocode:
  ```python
  visited={start}
  edges=[(w,start,v) for v,w in graph[start]]
  heapq.heapify(edges)
  while edges:
      w,u,v=heapq.heappop(edges)
      if v not in visited:
          visited.add(v)
          mst.append((u,v,w))
          for nxt,wt in graph[v]:
              if nxt not in visited:
                  heapq.heappush(edges,(wt,v,nxt))
  ```
- Complexity O(E log V). Better for sparse graphs; use adjacency matrix for dense graphs.
- Graph must be connected to cover all vertices; otherwise MST will only span visited component.
