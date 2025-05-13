# CQRS Pattern

## Description
This snippet demonstrates Command Query Responsibility Segregation.

## Code
```python
try:
    class CQRS:
        def command(self, data):
            return {"stored": data}
        def query(self):
            return {"data": "mocked"}
    cqrs = CQRS()
    print("Command result:", cqrs.command("test")["stored"])
except ImportError:
    print("Mock Output: Command result: test")
```

## Output
```
Mock Output: Command result: test
```
*(Real output: `Command result: test`)*

## Explanation
- **CQRS Pattern**: Separates read and write operations.
- **Logic**: Simulates a command to store data and a query.
- **Complexity**: O(1) per operation.
- **Use Case**: Used in scalable systems for performance.
- **Best Practice**: Sync read/write models; optimize queries; handle consistency.