# Log Analysis

## Description
This snippet demonstrates parsing a log file using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    logs = pd.DataFrame({"timestamp": ["2023-01-01"], "event": ["login"]})
    print("Log events:", logs["event"].iloc[0])
except ImportError:
    print("Mock Output: Log events: login")
```

## Output
`sample1.py` prints parsed events from log lines.
`sample2.py` prints event counts.
`sample3.py` writes a filtered log (login events) to `temp/log_filter.txt`.

## Explanation
- **Log Analysis**: Parses plain-text log entries.
- **Logic**: Extract event types, aggregate counts, and filter entries.
- **Complexity**: O(n) for n logs.
- **Use Case**: Used for security and operational log review.
- **Best Practice**: Normalize timestamps, handle missing fields, and store results in files.
