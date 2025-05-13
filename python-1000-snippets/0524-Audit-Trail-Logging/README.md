# Audit Trail Logging

## Description
This snippet demonstrates logging actions using `logging`.

## Code
```python
try:
    import logging
    logging.basicConfig(filename="audit.log", level=logging.INFO)
    logging.info("User action: login")
    print("Audit log created")
except ImportError:
    print("Mock Output: Audit log created")
```

## Output
```
Mock Output: Audit log created
```
*(Real output: `Audit log created`)*

## Explanation
- **Audit Trail Logging**: Logs user actions to a file.
- **Logic**: Records a login event using `logging`.
- **Complexity**: O(1) per log entry.
- **Use Case**: Used for tracking system activity.
- **Best Practice**: Rotate logs; secure files; include timestamps.