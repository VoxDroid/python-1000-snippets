# Geospatial Analysis

## Description
This snippet demonstrates geospatial analysis using basic coordinate operations without requiring geospatial libraries.

## Code
The sample scripts show:
- `sample1.py`: Compute centroid of sample locations.
- `sample2.py`: Compute haversine distance between two cities.
- `sample3.py`: Point-in-bounding-box checks.

## Output
`sample1.py` prints sample points and centroid.

`sample2.py` prints distance between New York and Los Angeles.

`sample3.py` prints whether points are inside a US bounding box.

## Explanation
- **Geospatial Analysis**: Demonstrates coordinate-based spatial queries.
- **Logic**: Computes centroid, haversine distances, and bbox membership.
- **Complexity**: O(n) for n points.
- **Use Case**: Useful for lightweight spatial reasoning when GIS libraries are unavailable.
- **Best Practice**: Use proper projection handling in production code.
