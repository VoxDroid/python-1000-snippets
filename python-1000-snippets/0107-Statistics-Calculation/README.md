# Statistics Calculation

## Description
This snippet calculates basic statistics (mean, median, variance) for a dataset.

## Code
```python
def statistics(data):
    n = len(data)
    mean = sum(data) / n
    sorted_data = sorted(data)
    median = sorted_data[n//2] if n % 2 else (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    variance = sum((x - mean) ** 2 for x in data) / n
    return mean, median, variance

data = [1, 2, 3, 4, 5]
mean, median, variance = statistics(data)
print(f"Mean: {mean}, Median: {median}, Variance: {variance}")
```

## Output
```
Mean: 3.0, Median: 3, Variance: 2.0
```

## Explanation
- **Statistics**:
  - Mean: Average of all values.
  - Median: Middle value of sorted data.
  - Variance: Average of squared deviations from the mean.
- **Complexity**: O(n log n) time due to sorting for median.
- **Use Case**: Used in data analysis, reporting, or preprocessing.
- **Best Practice**: Use `statistics` module or NumPy; handle empty datasets.