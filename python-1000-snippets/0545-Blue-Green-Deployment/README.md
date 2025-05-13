# Blue-Green Deployment

## Description
This snippet demonstrates a simulated blue-green deployment switch.

## Code
```python
try:
    environments = {"blue": "v1", "green": "v2"}
    active = "blue"
    def switch_env():
        return "green" if active == "blue" else "blue"
    print("New active env:", switch_env())
except ImportError:
    print("Mock Output: New active env: green")
```

## Output
```
Mock Output: New active env: green
```
*(Real output: `New active env: green`)*

## Explanation
- **Blue-Green Deployment**: Switches between two environments.
- **Logic**: Toggles between blue and green environments.
- **Complexity**: O(1) per switch.
- **Use Case**: Used for zero-downtime deployments.
- **Best Practice**: Validate new env; automate rollback; monitor traffic.