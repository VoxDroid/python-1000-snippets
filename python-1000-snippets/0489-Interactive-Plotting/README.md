# Interactive Plotting

## Description
This snippet demonstrates preparing data and configuration for interactive plotting without requiring `plotly`.
It writes CSV data and a JSON plot configuration that can be loaded into a plotting tool.

## Code
The sample scripts demonstrate:
- `sample1.py`: Generates CSV data suitable for plotting.
- `sample2.py`: Prints a simple dataset that can be plotted interactively.
- `sample3.py`: Writes a JSON plot configuration to `temp/interactive_plot_config.json`.

## Output
`sample1.py` writes data to:
```
temp/interactive_plot_data.csv
```

`sample2.py` prints point data to the console.

`sample3.py` writes a JSON plot configuration to:
```
temp/interactive_plot_config.json
```

## Explanation
- **Interactive Plotting (Data Prep)**: Generates data and configuration that can be consumed by interactive plotting tools.
- **Logic**: Create sample datasets and export them in common formats (CSV/JSON).
- **Complexity**: O(n) for n data points.
- **Use Case**: Useful when exporting data for visualization in web or GUI tools.
