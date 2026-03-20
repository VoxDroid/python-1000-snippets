# Motion Planning

## Description
This snippet demonstrates basic motion planning algorithms in 2D: RRT, A* grid search, and potential field planning.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Path length: 37
First 3 points: [(0.5, 0.5), (0.683, 0.60), (0.81, 0.76)]
Last 3 points: [(8.9, 8.4), (9.4, 8.7), (9.0, 9.0)]
```

## Explanation
- **RRT (Rapidly-exploring Random Tree)**: Builds a random tree toward a goal while avoiding obstacles.
- **A***: Finds the shortest grid path using heuristics (Manhattan distance).
- **Potential Field**: Moves towards a goal while avoiding obstacles via attractive and repulsive forces.
- **Best Practice**: Add obstacle checking, smooth paths, and validate on realistic maps.
