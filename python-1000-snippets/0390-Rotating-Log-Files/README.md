# Rotating Log Files

## Description
This snippet demonstrates rotating log files using `logging`.

## Code
```python
# Note: Requires `logging`
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("example")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("example.log", maxBytes=100, backupCount=2)
logger.addHandler(handler)
logger.info("Log message")
print("Log written")
```

## Output
```
Log written
```
*(Real output: Writes to `example.log`, rotates if size exceeds 100 bytes)*

## Explanation
- **Rotating Log Files**: Logs messages with automatic file rotation.
- **Logic**: Configures a `RotatingFileHandler` to manage log file size.
- **Complexity**: O(1) per log.
- **Use Case**: Used for long-running applications to manage log storage.
- **Best Practice**: Set appropriate size limits; handle permissions; test rotation.