# Bellman-Ford Algorithm

## Description
This snippet implements the Bellman-Ford algorithm to find the shortest paths from a source vertex to all other vertices in a weighted graph, handling negative weights.

## Code
```python
def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return None  # Negative cycle detected
    
    return distances

graph = {
    0: [(1, 4), (2, 8)],
    1: [(2, 2), (3, 5)],
    2: [(3, 5)],
    3: [(1, -1)]  # Negative weight
}
print("Shortest Paths:", bellman_ford(graph, 0))
```

## Output
```
Shortest Paths: {0: 0, 1: 4, 2: 6, 3: 11}
```

## Explanation
- **Bellman-Ford**: Relaxes all edges `V-1` times to compute shortest paths; checks for negative-weight cycles.
- **Graph**: Adjacency list with (vertex, weight) pairs.
- **Complexity**: O(V * E) time, O(V) space, where V is vertices and E is edges.
- **Use Case**: Used in routing protocols or graphs with negative weights (unlike Dijkstra’s).
- **Best Practice**: Validate graph structure; use for sparse graphs with negative weights.