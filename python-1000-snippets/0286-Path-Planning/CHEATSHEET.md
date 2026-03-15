# 0286 - Path Planning Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py  # A* search
python SAMPLES/sample2.py  # BFS search
python SAMPLES/sample3.py  # Dijkstra's algorithm
```

## Tips
- A*: choose a consistent heuristic (Manhattan distance for grids) to guarantee optimality.
- BFS explores all nodes at the current depth before moving deeper, making it ideal for unweighted grids.
- Dijkstra is like BFS but accounts for edge weights; it finds the lowest-cost path.
