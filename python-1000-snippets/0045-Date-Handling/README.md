# Date Handling

## Description
This snippet demonstrates handling dates in Python using the `datetime` module to get and format the current date.

## Code
```python
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")
print("Current date:", formatted_date)
```

## Output
```
Current date: 2025-05-08
```

## Explanation
- **datetime.now()**: Returns the current date and time.
- **strftime()**: Formats the date as a string (e.g., `"%Y-%m-%d"` for `YYYY-MM-DD`).
- **Use Case**: Date handling is used in logging, scheduling, or data timestamping.
- **Format Codes**: `%Y` (year), `%m` (month), `%d` (day), etc., allow custom formatting.
- **Best Practice**: Use `datetime` for robust date handling; validate formats for user inputs.