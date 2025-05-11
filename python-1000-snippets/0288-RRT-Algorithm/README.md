# RRT Algorithm

## Description
This snippet demonstrates a Rapidly-exploring Random Tree (RRT) for path planning.

## Code
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

## Output
```
Final Node: (np.float64(3.7417485368905923), np.float64(4.308881577807811))
```

## Explanation
- **RRT Algorithm**: Builds a tree to find a path to the goal.
- **Logic**: Randomly samples points and extends the tree, avoiding obstacles.
- **Complexity**: O(n) for n iterations (tree growth varies).
- **Use Case**: Used for motion planning in robotics.
- **Best Practice**: Tune step size; handle complex obstacles; optimize tree.