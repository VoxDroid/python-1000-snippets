# Usage Analytics

## Description
This snippet demonstrates analyzing API usage for an e-commerce system, tracking request counts by endpoint.

## Code
```python
# Usage analytics for API endpoints
try:
    from collections import Counter

    # Simulated API logs
    logs = [
        {"endpoint": "/order", "timestamp": "2025-05-13"},
        {"endpoint": "/order", "timestamp": "2025-05-13"},
        {"endpoint": "/user", "timestamp": "2025-05-13"}
    ]

    # Analyze usage
    def analyze_usage(logs: list) -> dict:
        # Count requests per endpoint
        endpoint_counts = Counter(log["endpoint"] for log in logs)
        return dict(endpoint_counts)

    # Run analytics
    result = analyze_usage(logs)
    print("Usage analytics:", result)
except ImportError:
    print("Mock Output: Usage analytics: {'/order': 2, '/user': 1}")
```

## Output
```
Mock Output: Usage analytics: {'/order': 2, '/user': 1}
```
*(Real output: `Usage analytics: {'/order': 2, '/user': 1}`)*

## Explanation
- **Purpose**: Usage analytics tracks system activity, providing insights into resource usage and user behavior.
- **Real-World Use Case**: In an e-commerce system, analyzing API endpoint usage helps identify high-traffic endpoints for optimization or scaling.
- **Code Breakdown**:
  - Simulated logs record API requests.
  - The `analyze_usage` function counts requests per endpoint using `Counter`.
  - The output shows request counts.
- **Challenges**: Handling large log volumes, ensuring privacy, and integrating with analytics platforms.
- **Integration**: Works with Cost Optimization (Snippet 644) and Budget Monitoring (Snippet 646) for resource planning.
- **Complexity**: O(n) for analyzing n logs.
- **Best Practices**: Use log aggregation tools, anonymize data, automate analytics, and visualize results.