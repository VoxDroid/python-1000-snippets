# Social Network Analysis

## Description
This snippet demonstrates social network analysis using `networkx` to build graphs and compute centrality and connectivity metrics.

## Files
- `SAMPLES/sample1.py`: Compute degree, betweenness, and closeness centrality on a small graph.
- `SAMPLES/sample2.py`: Find connected components and shortest paths.
- `SAMPLES/sample3.py`: Compute community detection (greedy modularity) and clustering coefficient.

## Quick start
```bash
pip install networkx
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Degree centrality: {1: 0.666..., 2: 1.0, 3: 0.666..., 4: 0.333...}
Shortest path 1->4: [1, 2, 4]
Communities: [{1, 2, 3}, {4}]
```

## Explanation
- **Social Network Analysis**: Uses graph structures (nodes+edges) to model relationships.
- **Centrality**: Identifies influential nodes (degree, betweenness, closeness).
- **Connectivity**: Examines components, shortest paths, clustering.
- **Use Case**: Applied to social media, communication networks, and recommendation graphs.
