# Data Dashboard

## Description
This snippet demonstrates a simple data dashboard using console output and file-based reports.

## Code
The sample scripts showcase different dashboard outputs:
- `sample1.py`: Prints a table of data to the console.
- `sample2.py`: Computes summary statistics and prints a report.
- `sample3.py`: Writes a short dashboard report to `temp/dashboard.txt` in a loop.

## Output
`sample1.py` prints a table to the console, e.g.:
```
Simple Data Dashboard
item | value | score
-----+-------+------
A    | 10.0  | 0.75
B    | 22.5  | 0.52
C    | 15.1  | 0.95
D    | 7.3   | 0.33
```

`sample2.py` prints summary statistics:
```
Dashboard Summary
value: min=7.30, max=22.50, mean=13.72
score: min=0.33, max=0.95, mean=0.64
```

`sample3.py` writes a dashboard report to `temp/dashboard.txt` in a loop.

## Explanation
- **Data Dashboard**: This snippet outputs data to the console and to a text file, simulating a dashboard.
- **Logic**: Build a dataset, compute summary metrics, and format output in tables or reports.
- **Complexity**: O(n) proportional to the number of data points.
- **Use Case**: Useful for lightweight reporting and monitoring in CLI environments.
