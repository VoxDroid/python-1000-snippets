# Time Handling Cheatsheet

## Current time
```python
from datetime import datetime
now = datetime.now()
now.strftime('%H:%M:%S')
```

## Formatting codes
- `%H` hour (24h), `%I` hour (12h), `%p` AM/PM.
- `%M` minute, `%S` second, `%f` microseconds.

## Parsing
```python
datetime.strptime('14:30:00', '%H:%M:%S')
```

## Tips
- For timezones, use `datetime.now(tz=timezone.utc)` or `zoneinfo`.
- Use `time.sleep()` for delays.

## Running samples
Activate virtual env and run `SAMPLES/sample*.py`.
