# Time Handling

## Description
This snippet shows how to handle time in Python using the `datetime` module to get and format the current time.

## Code
```python
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
print("Current time:", formatted_time)
```

## Output
```
Current time: 14:30:45
```
*(Output varies based on current time)*

## Explanation
- **datetime.now()**: Returns the current date and time, including hours, minutes, and seconds.
- **strftime()**: Formats the time as a string (e.g., `"%H:%M:%S"` for `HH:MM:SS`).
- **Use Case**: Time handling is used in scheduling, logging, or user interfaces.
- **Format Codes**: `%H` (hour), `%M` (minute), `%S` (second), etc., allow custom formatting.
- **Best Practice**: Use `datetime` for reliable time handling; consider time zones for global applications.