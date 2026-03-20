# 0473-Motion-Planning Cheatsheet

## Quick Tips
- RRT is good for high-dimensional spaces; add collision checks and a goal bias.
- A* finds shortest grid paths but requires an appropriate heuristic (e.g., Manhattan distance for 4-way movement).
- Potential fields are simple but can get stuck in local minima; combine with random exploration.

## Running examples
- `python SAMPLES/sample1.py` — RRT planning with circular obstacles.
- `python SAMPLES/sample2.py` — A* grid search planning.
- `python SAMPLES/sample3.py` — Potential field planning.
