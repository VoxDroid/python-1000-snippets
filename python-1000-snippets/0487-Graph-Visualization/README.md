# Graph Visualization

## Description
This snippet demonstrates basic graph visualization and analysis without external plotting libraries.
It builds a small graph in memory, prints adjacency information, and exports a Graphviz DOT file.

## Code
The sample scripts cover:
- `sample1.py`: Prints an adjacency list and basic graph statistics.
- `sample2.py`: Writes a Graphviz DOT file to `temp/graph.dot`.
- `sample3.py`: Calculates degree centrality and prints sorted scores.

## Output
`sample1.py` prints an adjacency list and node/edge counts, e.g.:
```
Adjacency list:
A: B, C
B: A, D
C: A, D
D: B, C, E
E: D
Nodes: 5, Edges: 5
```

`sample2.py` writes a DOT file such as:
```
temp/graph.dot
```

`sample3.py` prints degree centrality scores, e.g.:
```
Degree centrality:
  D: 0.75
  A: 0.50
  B: 0.50
  C: 0.50
  E: 0.25
```

## Explanation
- **Graph Representation**: This snippet uses an adjacency list (dictionary of neighbor sets) to represent a graph.
- **Logic**: Write the graph as a Graphviz DOT file, inspect adjacency relationships, or compute metrics like degree centrality.
- **Complexity**: Most operations are O(n + e) for n nodes and e edges.
- **Use Case**: Useful for understanding graph structures and exporting graphs for visualization.
