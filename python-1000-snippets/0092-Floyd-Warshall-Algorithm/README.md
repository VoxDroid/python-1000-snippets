# Floyd-Warshall Algorithm

## Description
This snippet implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices in a weighted graph.

## Code
```python
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('infinity')] * V for _ in range(V)]
    
    # Initialize distances
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
        dist[i][i] = 0
    
    # Update distances
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = [
    [0, 4, 8, float('infinity')],
    [float('infinity'), 0, 2, 5],
    [float('infinity'), float('infinity'), 0, 5],
    [float('infinity'), float('infinity'), float('infinity'), 0]
]
result = floyd_warshall(graph)
for row in result:
    print(row)
```

## Output
```
[0, 4, 6, 9]
[inf, 0, 2, 5]
[inf, inf, 0, 5]
[inf, inf, inf, 0]
```

## Explanation
- **Floyd-Warshall**: Computes shortest paths between all vertex pairs using dynamic programming.
- **Graph**: Adjacency matrix; `float('infinity')` for no edge.
- **Complexity**: O(V³) time, O(V²) space.
- **Use Case**: Used in network analysis or all-pairs shortest path problems.
- **Best Practice**: Handle negative cycles; use sparse representations for large graphs.