# Geospatial Analysis

## Description
This snippet demonstrates plotting geospatial data using `geopandas`.

## Code
```python
# Note: Requires `geopandas`. Install with `pip install geopandas`
try:
    import geopandas as gpd
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot()
    print("Geospatial map plotted")
except ImportError:
    print("Mock Output: Geospatial map plotted")
```

## Output
```
Mock Output: Geospatial map plotted
```
*(Real output with `geopandas`: `Geospatial map plotted` (displays map))*

## Explanation
- **Geospatial Analysis**: Visualizes country boundaries.
- **Logic**: Loads and plots a built-in world dataset.
- **Complexity**: O(n) for n geometries.
- **Use Case**: Used for GIS or location-based analysis.
- **Best Practice**: Validate geometries; add annotations; use projections.