# Ray Casting

## Description
This snippet demonstrates simple 2D/3D ray casting techniques used in games and simulations.

## Samples
- `SAMPLES/sample1.py`: Cast a ray through a 2D grid using Bresenham to find the first obstacle.
- `SAMPLES/sample2.py`: Compute a visibility polygon from a point by casting rays in multiple directions.
- `SAMPLES/sample3.py`: Perform ray-sphere intersection in 3D using a quadratic solution.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Ray casting is useful for visibility, line-of-sight, and collision detection.
- Use the slab method or line-segment intersection for robust 2D ray hits.
- In 3D, solving the quadratic equation gives the intersection distance along the ray.
