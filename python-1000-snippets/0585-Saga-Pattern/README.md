# Saga Pattern

## Description
This snippet demonstrates a distributed transaction using the Saga pattern.

## Code
```python
try:
    def saga_step(step, success=True):
        return {"step": step, "status": "success" if success else "failed"}
    steps = [saga_step(i) for i in range(2)]
    print("Saga status:", all(step["status"] == "success" for step in steps))
except ImportError:
    print("Mock Output: Saga status: True")
```

## Output
```
Mock Output: Saga status: True
```
*(Real output: `Saga status: True`)*

## Explanation
- **Saga Pattern**: Manages distributed transactions as a series of steps.
- **Logic**: Simulates two successful saga steps.
- **Complexity**: O(n) for n steps.
- **Use Case**: Used in microservices for transactions.
- **Best Practice**: Implement compensating actions; log steps; handle failures.