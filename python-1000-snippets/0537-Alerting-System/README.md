# Alerting System

## Description
This snippet demonstrates a simple alerting mechanism.

## Code
```python
try:
    def alert(condition, message):
        if condition:
            print("Alert:", message)
    alert(True, "CPU usage high")
except ImportError:
    print("Mock Output: Alert: CPU usage high")
```

## Output
```
Mock Output: Alert: CPU usage high
```
*(Real output: `Alert: CPU usage high`)*

## Explanation
- **Alerting System**: Triggers alerts based on conditions.
- **Logic**: Prints an alert if a condition is met.
- **Complexity**: O(1) per alert.
- **Use Case**: Used for notifying system issues.
- **Best Practice**: Integrate with email/SMS; set thresholds; suppress duplicates.