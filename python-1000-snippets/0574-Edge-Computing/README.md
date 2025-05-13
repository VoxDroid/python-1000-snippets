# Edge Computing

## Description
This snippet demonstrates local data processing for edge computing.

## Code
```python
try:
    def process_edge_data(data):
        return sum(data) / len(data)
    sensor_data = [25, 26, 24]
    print("Edge average:", process_edge_data(sensor_data))
except ImportError:
    print("Mock Output: Edge average: 25.0")
```

## Output
```
Mock Output: Edge average: 25.0
```
*(Real output: `Edge average: 25.0`)*

## Explanation
- **Edge Computing**: Processes data locally to reduce latency.
- **Logic**: Computes the average of sensor readings.
- **Complexity**: O(n) for n data points.
- **Use Case**: Used in IoT for real-time analytics.
- **Best Practice**: Optimize for low resources; secure data; sync with cloud.