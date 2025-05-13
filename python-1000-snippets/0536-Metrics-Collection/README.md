# Metrics Collection

## Description
This snippet demonstrates collecting metrics using `prometheus_client`.

## Code
```python
# Note: Requires `prometheus_client`. Install with `pip install prometheus_client`
try:
    from prometheus_client import Counter
    requests_total = Counter("requests_total", "Total requests")
    requests_total.inc()
    print("Metric incremented")
except ImportError:
    print("Mock Output: Metric incremented")
```

## Output
```
Mock Output: Metric incremented
```
*(Real output with `prometheus_client`: `Metric incremented`)*

## Explanation
- **Metrics Collection**: Tracks request counts.
- **Logic**: Increments a Prometheus counter.
- **Complexity**: O(1) per increment.
- **Use Case**: Used for system performance monitoring.
- **Best Practice**: Expose metrics endpoint; define clear metrics; integrate with Grafana.