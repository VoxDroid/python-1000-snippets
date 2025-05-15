# Dynamic Programming

## Description
This snippet implements the Floyd-Warshall algorithm for a transportation network, finding shortest paths between all pairs of cities to optimize routing.

## Code
```python
# Dynamic Programming: Floyd-Warshall algorithm
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Floyd-Warshall model
    class FloydWarshall:
        def __init__(self, distances: np.ndarray):
            # Initialize distance matrix
            self.n = len(distances)
            self.dist = distances.copy()
            self.dist[np.isinf(self.dist)] = float('inf')  # Ensure proper infinity handling

        def solve(self) -> np.ndarray:
            # Compute all-pairs shortest paths
            dist = self.dist.copy()
            for k in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if dist[i, k] + dist[k, j] < dist[i, j]:
                            dist[i, j] = dist[i, k] + dist[k, j]
            return dist

    # Run Floyd-Warshall simulation
    def run_floyd_warshall(n_cities: int) -> dict:
        # Optimize routing
        # Create random distance matrix (symmetric, no self-loops)
        distances = np.random.uniform(10, 100, (n_cities, n_cities))
        distances = (distances + distances.T) / 2
        np.fill_diagonal(distances, 0)
        # Add some missing edges
        mask = np.random.choice([0, 1], (n_cities, n_cities), p=[0.3, 0.7])
        mask = np.triu(mask, 1) + np.triu(mask, 1).T
        distances[mask == 0] = float('inf')
        fw = FloydWarshall(distances)
        shortest_paths = fw.solve()
        return {'shortest_paths': shortest_paths}

    # Example usage
    result = run_floyd_warshall(n_cities=5)
    print("Dynamic programming result:", result['shortest_paths'][0, -1])  # Distance from city 0 to last city
except ImportError:
    print("Mock Output: Dynamic programming result: 50.0")
```

## Output
```
Mock Output: Dynamic programming result: 50.0
```
*(Real output with `numpy`: `Dynamic programming result: <distance from city 0 to last city, e.g., 50.0>`)*

## Explanation
- **Purpose**: Computes all-pairs shortest paths using the Floyd-Warshall algorithm.
- **Real-World Use Case**: A transportation network uses this to optimize delivery routes across cities, reducing fuel costs.
- **Code Breakdown**:
  - The `FloydWarshall` class initializes a distance matrix.
  - The `solve` method computes shortest paths via dynamic programming.
  - The `run_floyd_warshall` function generates a random graph and returns the shortest path matrix.
- **Technical Challenges**: Handling large graphs, managing infinity values, and detecting negative cycles.
- **Integration**: Complements Combinatorial Optimization (Snippet 987) for routing problems.
- **Scalability**: O(n^3) complexity for n cities; large graphs require sparse methods or Dijkstra’s algorithm.
- **Performance Metrics**: Solves graphs with n<100 in seconds, achieving exact shortest paths.
- **Best Practices**: Validate with real road data, handle disconnected graphs, and store paths for reconstruction.
- **Extensions**: Add path reconstruction or handle dynamic updates.
- **Limitations**: Dense matrix approach; real networks may be sparse or dynamic.