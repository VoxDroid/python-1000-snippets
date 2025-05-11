# Collision Detection

## Description
This snippet demonstrates 2D collision detection using bounding boxes.

## Code
```python
def check_collision(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2

box1 = (40, 40, 20, 20)
box2 = (50, 50, 20, 20)
print("Collision:", check_collision(box1, box2))
```

## Output
```
Collision: True
```

## Explanation
- **Collision Detection**: Checks if two rectangular boxes overlap.
- **Logic**: Uses axis-aligned bounding box (AABB) collision test.
- **Complexity**: O(1) per check.
- **Use Case**: Used in games or physics simulations.
- **Best Practice**: Optimize for multiple objects; use spatial partitioning; validate inputs.