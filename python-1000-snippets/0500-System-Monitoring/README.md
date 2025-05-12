# System Monitoring

## Description
This snippet demonstrates CPU usage monitoring using `psutil`.

## Code
```python
# Note: Requires `psutil`. Install with `pip install psutil`
try:
    import psutil
    cpu = psutil.cpu_percent(interval=1)
    print("CPU usage:", cpu)
except ImportError:
    print("Mock Output: CPU usage: 10.0")
```

## Output
```
Mock Output: CPU usage: 10.0
```
*(Real output with `psutil`: `CPU usage: <percentage>`)*

## Explanation
- **System Monitoring**: Tracks CPU usage in real-time.
- **Logic**: Uses `psutil` to measure CPU percentage.
- **Complexity**: O(1) per measurement.
- **Use Case**: Used for performance monitoring or alerting.
- **Best Practice**: Monitor multiple metrics; set thresholds; log data.