# User Behavior Analytics

## Description
This snippet demonstrates analyzing user events using `pandas`.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    events = pd.DataFrame({"user": [1, 1, 2], "action": ["click", "view", "click"]})
    clicks = events[events["action"] == "click"].groupby("user").size()
    print("Click counts:", clicks.to_dict())
except ImportError:
    print("Mock Output: Click counts: {1: 1, 2: 1}")
```

## Output
```
Mock Output: Click counts: {1: 1, 2: 1}
```
*(Real output with `pandas`: `Click counts: {1: 1, 2: 1}`)*

## Explanation
- **User Behavior Analytics**: Aggregates user actions.
- **Logic**: Counts clicks per user in a DataFrame.
- **Complexity**: O(n) for n events.
- **Use Case**: Used for understanding user engagement.
- **Best Practice**: Clean data; visualize trends; protect privacy.