# Logging

## Description
This snippet shows how to use the `logging` module to log messages at different severity levels (e.g., info, warning, error).

## Code
```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
```

## Output
```
2025-05-08 14:30:45,123 - DEBUG - Debug message
2025-05-08 14:30:45,124 - INFO - Info message
2025-05-08 14:30:45,125 - WARNING - Warning message
2025-05-08 14:30:45,126 - ERROR - Error message
```

## Explanation
- **logging.basicConfig()**: Sets up logging with a format (timestamp, level, message) and minimum level (`DEBUG`).
- **Levels**: `debug`, `info`, `warning`, `error`, `critical` for different severities.
- **Use Case**: Logging is used for debugging, monitoring, or auditing applications.
- **Flexibility**: Can log to files or other outputs by configuring handlers.
- **Best Practice**: Use logging instead of `print()` for production code; configure appropriate levels.