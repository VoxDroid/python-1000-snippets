# Social Network Analysis

## Description
This snippet demonstrates social network analysis using `networkx` to compute centrality.

## Code
```python
# Note: Requires `networkx`. Install with `pip install networkx`
try:
    import networkx as nx
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])
    centrality = nx.degree_centrality(G)
    print("Centrality:", centrality)
except ImportError:
    print("Mock Output: Centrality: {1: 0.6666666666666666, 2: 1.0, 3: 0.6666666666666666, 4: 0.3333333333333333}
```

## Output
```
Mock Output: Centrality: {1: 0.6666666666666666, 2: 1.0, 3: 0.6666666666666666, 4: 0.3333333333333333}
```
*(Real output with `networkx`: `Centrality: {1: 0.6666666666666666, 2: 1.0, 3: 0.6666666666666666, 4: 0.3333333333333333}`)*

## Explanation
- **Social Network Analysis**: Computes degree centrality for nodes in a graph.
- **Logic**: Builds a small graph and calculates normalized degree centrality.
- **Complexity**: O(n + m) for n nodes, m edges.
- **Use Case**: Used to identify influential nodes in networks.
- **Best Practice**: Choose appropriate centrality; handle large graphs; validate edges.