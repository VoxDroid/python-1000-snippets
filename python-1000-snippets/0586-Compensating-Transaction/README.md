# Compensating Transaction

## Description
This snippet demonstrates a compensating transaction for rollback.

## Code
```python
try:
    def transaction():
        return {"status": "committed"}
    def compensate():
        return {"status": "rolled back"}
    tx = transaction()
    print("Compensated:", compensate()["status"] if tx["status"] == "committed" else "no action")
except ImportError:
    print("Mock Output: Compensated: rolled back")
```

## Output
```
Mock Output: Compensated: rolled back
```
*(Real output: `Compensated: rolled back`)*

## Explanation
- **Compensating Transaction**: Reverses a transaction on failure.
- **Logic**: Simulates a rollback if a transaction commits.
- **Complexity**: O(1) per compensation.
- **Use Case**: Used in sagas for error recovery.
- **Best Practice**: Ensure idempotency; log compensations; test rollbacks.