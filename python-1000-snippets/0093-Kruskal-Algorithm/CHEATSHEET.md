# 0093-Kruskal-Algorithm Cheatsheet

- Kruskal’s algorithm builds an MST by sorting edges by weight and adding them if they connect different components.
- Use a Union-Find (disjoint set) structure to keep track of components:
  ```python
  uf = UnionFind(V)
  def find(x): ... # path compression
  def union(x,y): uf.parent[find(x)] = find(y)
  ```
- Graph input: adjacency list of undirected edges `(neighbor, weight)`.
- Gather edges `(w,u,v)` with `u<v` to avoid duplicates, then `edges.sort()`.
- Iterate edges, use `uf.find` to check if adding creates cycle.
- Time complexity dominated by sorting O(E log E).
- For disconnected graphs, MST will not cover all vertices; check component count.
