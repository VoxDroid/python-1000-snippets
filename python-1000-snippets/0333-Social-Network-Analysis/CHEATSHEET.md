# 0333-Social-Network-Analysis Cheatsheet

## Quick commands
```bash
pip install networkx
python SAMPLES/sample1.py  # centrality metrics
python SAMPLES/sample2.py  # connected components and shortest path
python SAMPLES/sample3.py  # community detection and clustering
```

## Tips
- `networkx.Graph()` builds an undirected graph; use `DiGraph()` for directed.
- Common centrality metrics:
  - `degree_centrality(G)`
  - `betweenness_centrality(G)`
  - `closeness_centrality(G)`
- For shortest paths, use `nx.shortest_path(G, source, target)`.
- For community detection, use `nx.algorithms.community.greedy_modularity_communities(G)`.

## Example outline
```python
import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])
print(nx.degree_centrality(G))
```
