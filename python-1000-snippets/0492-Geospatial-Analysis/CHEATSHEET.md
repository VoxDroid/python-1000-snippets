# 0492-Geospatial Analysis Cheatsheet

## Quick Start
Run a sample:
```bash
python3 python-1000-snippets/0492-Geospatial-Analysis/SAMPLES/sample1.py
```

## Notes
- `sample1.py` computes centroid of latitude/longitude points.
- `sample2.py` calculates great-circle distance with the haversine formula.
- `sample3.py` checks whether coordinates are inside a bounding box.

## Tips
- For better accuracy, use geospatial libraries (`geopandas`, `shapely`, `pyproj`) in production.
- Keep lat/lon in degrees and convert to radians for trigonometric formulas.
