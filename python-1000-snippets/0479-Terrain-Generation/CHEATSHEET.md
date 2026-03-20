# 0479-Terrain-Generation Cheatsheet

## Quick Tips
- Layer multiple noise scales (octaves) to create realistic terrain features.
- Use smoothing (e.g., box blur) to reduce high-frequency noise.
- Classify heights into categories (water/land/mountain) using thresholds.

## Running examples
- `python SAMPLES/sample1.py` — generate a heightmap using layered noise.
- `python SAMPLES/sample2.py` — classify heightmap regions into terrain types.
- `python SAMPLES/sample3.py` — compute contour points for specified elevation levels.
