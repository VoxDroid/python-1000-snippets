# Prim Algorithm

## Description
This snippet implements Prim’s algorithm to find the minimum spanning tree of a weighted undirected graph using a priority queue.

## Code
```python
import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    
    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        for next_v, next_w in graph[v]:
            if next_v not in visited:
                heapq.heappush(edges, (next_w, v, next_v))
    
    return mst

graph = {
    0: [(1, 4), (2, 8)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 8), (1, 2), (3, 5)],
    3: [(1, 5), (2, 5)]
}
print("MST Edges:", prim(graph, 0))
```

## Output
```
MST Edges: [(0, 1, 4), (1, 2, 2), (1, 3, 5)]
```

## Explanation
- **Prim’s**: Grows the MST by adding the smallest edge connecting a visited vertex to an unvisited one.
- **Priority Queue**: Uses `heapq` to select the minimum-weight edge.
- **Complexity**: O(E log V) time, O(V) space.
- **Use Case**: Used in network optimization or clustering.
- **Best Practice**: Ensure graph is connected; optimize for dense graphs.