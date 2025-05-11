# Ray Casting

## Description
This snippet demonstrates simple 2D ray casting to detect intersections.

## Code
```python
def ray_cast(origin, direction, wall):
    x1, y1 = origin
    dx, dy = direction
    x2, y2, x3, y3 = wall  # wall is a segment from (x2, y2) to (x3, y3)

    # Ray: (x, y) = (x1, y1) + t*(dx, dy)
    # Wall segment: (x, y) = (x2, y2) + u*((x3 - x2), (y3 - y2))
    wx = x3 - x2
    wy = y3 - y2

    denom = dx * wy - dy * wx
    if abs(denom) < 1e-6:
        return None  # Lines are parallel

    dx2 = x2 - x1
    dy2 = y2 - y1

    t = (dx2 * wy - dy2 * wx) / denom
    u = (dx2 * dy - dy2 * dx) / denom

    if t >= 0 and 0 <= u <= 1:
        # t >= 0 ensures the ray is forward
        return (x1 + t * dx, y1 + t * dy)
    return None

# Example test
origin = (0, 0)
direction = (1, 1)
wall = (2, 0, 2, 2)
print("Intersection:", ray_cast(origin, direction, wall))
```

## Output
```
Intersection: (2.0, 2.0)
```

## Explanation
- **Ray Casting**: Finds the intersection of a ray with a wall segment.
- **Logic**: Uses line-segment intersection formula to compute the hit point.
- **Complexity**: O(1) per ray.
- **Use Case**: Used in rendering, games, or robotics.
- **Best Practice**: Handle edge cases; optimize for multiple walls; validate inputs.