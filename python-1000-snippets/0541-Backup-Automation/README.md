# Backup Automation

## Description
This snippet demonstrates automating a backup using `shutil`.

## Code
```python
# Note: Requires `shutil`. Built-in module.
try:
    import shutil
    shutil.copy("data.txt", "data_backup.txt")
    print("Backup created")
except ImportError:
    print("Mock Output: Backup created")
```

## Output
```
Mock Output: Backup created
```
*(Real output with `shutil`: `Backup created` (if `data.txt` exists))*

## Explanation
- **Backup Automation**: Copies a file as a backup.
- **Logic**: Uses `shutil` to copy a file.
- **Complexity**: O(n) for file size n.
- **Use Case**: Used for periodic data backups.
- **Best Practice**: Schedule backups; verify integrity; store offsite.