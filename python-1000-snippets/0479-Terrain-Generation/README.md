# Terrain Generation

## Description
This snippet demonstrates terrain generation techniques using NumPy, including heightmap creation, terrain classification, and contour extraction.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Heightmap stats: min= 0.586 max= 1.357
Row sample: [0.798, 0.946, ...]
```

## Explanation
- **Heightmap Generation**: Layer smoothed random noise to create a terrain heightmap.
- **Terrain Classification**: Segment the heightmap into water, land, and mountain regions.
- **Contour Extraction**: Find points near specified elevation levels (contours).
- **Best Practice**: Normalize heightmaps, apply smoothing, and use meaningful thresholds for terrain categories.
