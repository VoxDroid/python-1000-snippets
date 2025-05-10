# Graph Representation

## Description
This snippet shows how to represent a graph using an adjacency list (dictionary) in Python.

## Code
```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph
    
    def display(self):
        return {vertex: neighbors for vertex, neighbors in self.graph.items()}

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
print("Graph:", g.display())
```

## Output
```
Graph: {0: [1, 2], 1: [0, 2], 2: [0, 1]}
```

## Explanation
- **Graph**: A structure of vertices connected by edges; here, an undirected graph using an adjacency list.
- **Adjacency List**: A dictionary where each key (vertex) maps to a list of neighboring vertices.
- **Methods**:
  - `add_edge`: Adds an edge between vertices `u` and `v`.
  - `display`: Returns the graph structure.
- **Use Case**: Graphs are used in networks, social media, or pathfinding algorithms.
- **Best Practice**: Support directed graphs or weighted edges as needed; validate inputs.