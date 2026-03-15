# RRT Algorithm

## Description
This snippet demonstrates a Rapidly-exploring Random Tree (RRT) for path planning.

## Samples
- `SAMPLES/sample1.py`: Basic RRT growth, stops when reaching the goal.
- `SAMPLES/sample2.py`: RRT with goal bias, builds a tree and reports best node.
- `SAMPLES/sample3.py`: Simple RRT* variant that rewires nearby nodes to improve path cost.

## Example (from sample1)
```python
import numpy as np
np.random.seed(42)
start, goal = (0, 0), (4, 4)
obstacle = (2, 2)
nodes = [start]
for _ in range(100):
    rand = np.random.random(2) * 5
    nearest = min(nodes, key=lambda n: np.linalg.norm(np.array(n) - rand))
    new_node = tuple(np.array(nearest) + 0.5 * (rand - nearest) / np.linalg.norm(rand - nearest))
    if abs(new_node[0] - obstacle[0]) > 0.5 or abs(new_node[1] - obstacle[1]) > 0.5:
        nodes.append(new_node)
        if np.linalg.norm(np.array(new_node) - goal) < 0.5:
            break
print("Final Node:", nodes[-1])
```

## Output (sample1)
```
Final Node: (np.float64(3.7417485368905923), np.float64(4.308881577807811))
```

## Explanation
- **RRT Algorithm**: Builds a tree to find a path to the goal.
- **Logic**: Randomly samples points and extends the tree, avoiding obstacles.
- **RRT***: Adds rewiring of nearby nodes to improve path cost.
- **Complexity**: O(n) per iteration, with more work for rewiring.
- **Use Case**: Used for motion planning in robotics.
- **Best Practice**: Tune step size, goal bias, and neighborhood radius for RRT*.
