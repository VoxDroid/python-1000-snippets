# Heatmap Generation

## Description
This snippet demonstrates generating heatmap data and rendering a simple ASCII heatmap without external plotting libraries.

## Code
The sample scripts show how to:
- Generate heatmap matrix data and save as CSV (`sample1.py`).
- Compute statistics (min/max/mean) for heatmap values (`sample2.py`).
- Render an ASCII heatmap view in the terminal (`sample3.py`).

## Output
`sample1.py` writes a CSV file with heatmap values:
```
temp/heatmap.csv
```

`sample2.py` prints summary statistics, e.g.:
```
Heatmap Summary
  min: 1
  max: 64
  mean: 17.50
```

`sample3.py` renders an ASCII heatmap to the console.

## Explanation
- **Heatmap Generation**: Visualizes a 2D array as a color-coded grid (ASCII in this snippet).
- **Logic**: Generates a numerical matrix, computes statistics, and maps values to characters for display.
- **Complexity**: O(n*m) for n x m data points.
- **Use Case**: Useful for quick visualization of 2D data in terminal environments.
- **Best Practice**: Normalize data before creating a heatmap and label axes for clarity.