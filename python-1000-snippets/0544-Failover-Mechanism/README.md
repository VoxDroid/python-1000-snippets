# Failover Mechanism

## Description
This snippet demonstrates a simple failover to a backup server.

## Code
```python
try:
    servers = ["primary:8080", "backup:8080"]
    def failover():
        return servers[1] if True else servers[0]  # Simulated failure
    print("Active server:", failover())
except ImportError:
    print("Mock Output: Active server: backup:8080")
```

## Output
```
Mock Output: Active server: backup:8080
```
*(Real output: `Active server: backup:8080`)*

## Explanation
- **Failover Mechanism**: Switches to a backup server on failure.
- **Logic**: Selects backup server in a simulated failure.
- **Complexity**: O(1) per failover.
- **Use Case**: Used for maintaining service uptime.
- **Best Practice**: Test failover; minimize downtime; log switches.