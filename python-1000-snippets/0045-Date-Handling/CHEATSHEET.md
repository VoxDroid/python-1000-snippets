# Date Handling Cheatsheet

## Getting current date/time
```python
from datetime import datetime
now = datetime.now()
```

## Formatting
- `now.strftime("%Y-%m-%d")` -> `2026-03-08`
- Common codes: `%Y` year, `%m` month, `%d` day, `%H` hour, `%M` minute.

## Parsing
```python
datetime.strptime("2026-03-08", "%Y-%m-%d")
```

## Differences
- Subtract two `datetime` objects to get a `timedelta`.

## Tips
- For timezones use `pytz` or `zoneinfo` (Python 3.9+).
- `date()` method drops time portion.

## Running samples
Activate virtual env then run `SAMPLES/sample*.py`.
