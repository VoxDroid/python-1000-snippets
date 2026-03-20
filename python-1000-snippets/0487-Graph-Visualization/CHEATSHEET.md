# 0487-Graph-Visualization Cheatsheet

## Quick Start
Run a sample:
```bash
python3 python-1000-snippets/0487-Graph-Visualization/SAMPLES/sample1.py
```

## Tips
- `sample2.py` generates a DOT file at `temp/graph.dot` that you can render with Graphviz (e.g. `dot -Tpng temp/graph.dot -o temp/graph.png`).
- Use the adjacency list output in `sample1.py` to understand node connections.
- Degree centrality in `sample3.py` is computed as degree/(n-1) for a simple comparison between nodes.
