# Kruskal Algorithm

## Description
This snippet implements Kruskal’s algorithm to find the minimum spanning tree (MST) of a weighted undirected graph using a union-find data structure.

## Code
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(graph, V):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if u < v:  # Avoid duplicates
                edges.append((w, u, v))
    edges.sort()
    
    uf = UnionFind(V)
    mst = []
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst

graph = {
    0: [(1, 4), (2, 8)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 8), (1, 2), (3, 5)],
    3: [(1, 5), (2, 5)]
}
print("MST Edges:", kruskal(graph, 4))
```

## Output
```
MST Edges: [(1, 2, 2), (0, 1, 4), (1, 3, 5)]
```

## Explanation
- **Kruskal’s**: Selects edges in increasing weight order, adding them to the MST if they don’t form a cycle.
- **Union-Find**: Detects cycles by tracking connected components.
- **Complexity**: O(E log E) time for sorting, O(V) space.
- **Use Case**: Used in network design (e.g., minimum-cost wiring).
- **Best Practice**: Ensure graph connectivity; use efficient union-find with path compression.