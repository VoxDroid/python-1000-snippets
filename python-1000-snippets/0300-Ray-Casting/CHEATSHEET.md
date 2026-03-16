# 0300-Ray-Casting Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py  # Ray cast in a grid using Bresenham line
python SAMPLES/sample2.py  # Visibility polygon via ray casting
python SAMPLES/sample3.py  # Ray-sphere intersection in 3D
```

## Tips
- Ray casting is the process of sending a ray from an origin in a direction and finding the first intersection.
- The slab method (ray vs AABB) and line-segment intersection are common primitives for 2D/3D collision.
- For performance in games, cast rays against simplified geometry (grid, bounding boxes) and avoid checking every object.
