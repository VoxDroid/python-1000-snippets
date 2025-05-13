# High Availability Setup

## Description
This snippet demonstrates a simulated HA setup with multiple nodes.

## Code
```python
try:
    nodes = ["node1:8080", "node2:8080"]
    def is_available(node):
        return True  # Simulated check
    print("Available nodes:", [node for node in nodes if is_available(node)])
except ImportError:
    print("Mock Output: Available nodes: ['node1:8080', 'node2:8080']")
```

## Output
```
Mock Output: Available nodes: ['node1:8080', 'node2:8080']
```
*(Real output: `Available nodes: ['node1:8080', 'node2:8080']`)*

## Explanation
- **High Availability Setup**: Checks node availability.
- **Logic**: Simulates checking if nodes are online.
- **Complexity**: O(n) for n nodes.
- **Use Case**: Used in distributed systems for uptime.
- **Best Practice**: Automate checks; balance load; failover gracefully.