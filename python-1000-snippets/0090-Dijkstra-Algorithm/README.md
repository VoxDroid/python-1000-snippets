# Dijkstra Algorithm

## Description
This snippet implements Dijkstra’s algorithm to find the shortest paths from a source vertex to all other vertices in a weighted graph.

## Code
```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {
    0: [(1, 4), (2, 8)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 8), (1, 2), (3, 5)],
    3: [(1, 5), (2, 5)]
}
print("Shortest Paths:", dijkstra(graph, 0))
```

## Output
```
Shortest Paths: {0: 0, 1: 4, 2: 6, 3: 9}
```

## Explanation
- **Dijkstra’s Algorithm**: Finds shortest paths using a priority queue to explore vertices by increasing distance.
- **Graph**: Represented as a dictionary of adjacency lists with (neighbor, weight) pairs.
- **Complexity**: O((V + E) log V) with a binary heap, where V is vertices and E is edges.
- **Use Case**: Used in routing protocols, GPS navigation, or network optimization.
- **Best Practice**: Ensure non-negative weights; use libraries like `networkx` for production.