# 0299-Collision-Detection Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0299-Collision-Detection/SAMPLES/sample1.py`
  - `python python-1000-snippets/0299-Collision-Detection/SAMPLES/sample2.py`
  - `python python-1000-snippets/0299-Collision-Detection/SAMPLES/sample3.py`

## Concepts
- **AABB Collision**: Fast check for overlap between axis-aligned rectangles.
- **Circle Collision**: Distance check between centers compared to sum of radii.
- **Ray Casting**: Compute intersection of a ray with a bounding volume (e.g., AABB).

## Tips
- Use spatial indexing (grids, quadtrees) when checking many objects to avoid O(n^2) checks.
- Use bounding volumes (AABB, spheres) for hierarchical collision detection.
- For continuous collision detection, use ray/segment intersection to prevent tunneling.
