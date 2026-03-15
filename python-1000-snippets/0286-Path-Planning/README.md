# Path Planning

## Description
This snippet demonstrates grid-based path planning algorithms.
It includes examples using A* search, breadth-first search (BFS), and Dijkstra's algorithm for weighted grids.

## Dependencies
No external dependencies are required.

## Samples
- `SAMPLES/sample1.py`: A* path planning on a grid with obstacles.
- `SAMPLES/sample2.py`: BFS path planning to find the shortest path.
- `SAMPLES/sample3.py`: Dijkstra’s algorithm on a weighted grid.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- A* uses a heuristic (Manhattan distance) for efficient search.
- BFS finds the shortest path in an unweighted grid.
- Dijkstra handles varying movement costs.
