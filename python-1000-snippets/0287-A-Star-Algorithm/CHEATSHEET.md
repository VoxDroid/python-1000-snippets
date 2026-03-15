# 0287 - A* Algorithm Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- A*: use a priority queue with `f = g + h` where `g` is cost so far and `h` is heuristic estimate.
- Manhattan heuristic: `abs(dx)+abs(dy)` for grid navigation.
- Ensure heuristic is admissible (never overestimates the true remaining cost) for optimal paths.
- For weighted grids, include movement cost in the `g` score when considering neighbors.
