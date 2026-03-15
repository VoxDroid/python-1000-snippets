# A Star Algorithm

## Description
This snippet demonstrates the A* search algorithm for grid-based pathfinding.
It includes examples showing standard A* with Manhattan heuristic, weighted cost grids, and heuristic comparisons.

## Dependencies
No external dependencies are required.

## Samples
- `SAMPLES/sample1.py`: Basic A* path planning on a grid with obstacles.
- `SAMPLES/sample2.py`: A* on a weighted grid (non-uniform movement costs).
- `SAMPLES/sample3.py`: Compare Manhattan vs Euclidean heuristics.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Use an admissible heuristic (never overestimates) to guarantee optimal paths.
- Manhattan distance works well on 4-connected grids.
- For weighted grids, include movement cost in the g-score updates.
