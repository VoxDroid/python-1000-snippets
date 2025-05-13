# Disaster Recovery

## Description
This snippet demonstrates a simulated data restore process.

## Code
```python
try:
    backup = {"data": [1, 2, 3]}
    def restore():
        return backup["data"]
    print("Restored data:", restore())
except ImportError:
    print("Mock Output: Restored data: [1, 2, 3]")
```

## Output
```
Mock Output: Restored data: [1, 2, 3]
```
*(Real output: `Restored data: [1, 2, 3]`)*

## Explanation
- **Disaster Recovery**: Restores data from a backup.
- **Logic**: Returns data from a simulated backup.
- **Complexity**: O(1) for restore.
- **Use Case**: Used for recovering from data loss.
- **Best Practice**: Test restores; secure backups; automate recovery.