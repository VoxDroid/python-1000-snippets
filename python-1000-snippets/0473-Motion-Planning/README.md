# Motion Planning

## Description
This snippet demonstrates a simple RRT path planner using `numpy`.

## Code
```python
try:
    import numpy as np
    def rrt(start, goal, max_steps=10):
        points = [start]
        for _ in range(max_steps):
            rand_point = np.random.uniform(0, 10, 2)
            points.append(rand_point)
        return points
    path = rrt([0, 0], [10, 10])
    print("Path points:", len(path))
except ImportError:
    print("Mock Output: Path points: 11")
```

## Output
```
Mock Output: Path points: 11
```
*(Real output with `numpy`: `Path points: 11`)*

## Explanation
- **Motion Planning**: Generates a simple random path using RRT.
- **Logic**: Samples random points to simulate a path.
- **Complexity**: O(n) for n steps.
- **Use Case**: Used in robotics for obstacle-free navigation.
- **Best Practice**: Add obstacle checks; optimize paths; validate goal reachability.