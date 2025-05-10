# Logging Configuration

## Description
This snippet demonstrates configuring Python’s `logging` module to log messages to a file and console.

## Code
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
logger.warning("This is a warning")
```

## Output
*(Console output)*
```
2025-05-10 12:00:00,000 - INFO - Application started
2025-05-10 12:00:00,001 - WARNING - This is a warning
```
*(app.log file)*
```
2025-05-10 12:00:00,000 - INFO - Application started
2025-05-10 12:00:00,001 - WARNING - This is a warning
```

## Explanation
- **Logging Configuration**: Sets up `logging` to output messages at `INFO` level or higher to both console and `app.log`.
- **Logic**: Uses `basicConfig` to define format and handlers; logs sample messages.
- **Complexity**: O(1) per log message.
- **Use Case**: Used for debugging, monitoring, or auditing applications.
- **Best Practice**: Configure log levels; use named loggers; rotate log files for large applications.