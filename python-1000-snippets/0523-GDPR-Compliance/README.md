# GDPR Compliance

## Description
This snippet demonstrates a simulated GDPR data deletion process.

## Code
```python
try:
    import pandas as pd
    df = pd.DataFrame({"user_id": [1, 2], "data": ["info", "info"]})
    df = df[df["user_id"] != 1]
    print("User data deleted")
except ImportError:
    print("Mock Output: User data deleted")
```

## Output
```
Mock Output: User data deleted
```
*(Real output: `User data deleted`)*

## Explanation
- **GDPR Compliance**: Removes user data to comply with deletion requests.
- **Logic**: Filters out a specific user’s data.
- **Complexity**: O(n) for n rows.
- **Use Case**: Used for regulatory compliance in data systems.
- **Best Practice**: Log deletions; ensure backups; validate compliance.