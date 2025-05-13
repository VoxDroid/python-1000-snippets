# Canary Release

## Description
This snippet demonstrates a canary release with weighted traffic.

## Code
```python
try:
    import random
    def route_request():
        return "canary" if random.random() < 0.1 else "stable"
    print("Route:", route_request())
except ImportError:
    print("Mock Output: Route: stable")
```

## Output
```
Mock Output: Route: stable
```
*(Real output: `Route: canary` or `Route: stable`)*

## Explanation
- **Canary Release**: Routes a small percentage of traffic to a new version.
- **Logic**: Sends 10% of requests to the canary version.
- **Complexity**: O(1) per route.
- **Use Case**: Used for testing new features safely.
- **Best Practice**: Monitor metrics; adjust weights; rollback if needed.