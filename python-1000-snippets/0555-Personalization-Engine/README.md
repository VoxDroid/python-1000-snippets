# Personalization Engine

## Description
This snippet demonstrates a simple personalization engine using user profiles.

## Code
```python
# Note: Requires `pandas`. Install with `pip install pandas`
try:
    import pandas as pd
    user_profiles = pd.DataFrame({"user": [1, 2], "pref": ["action", "comedy"]})
    def personalize(user_id):
        return user_profiles[user_profiles["user"] == user_id]["pref"].iloc[0]
    print("Preference for user 1:", personalize(1))
except ImportError:
    print("Mock Output: Preference for user 1: action")
```

## Output
```
Mock Output: Preference for user 1: action
```
*(Real output with `pandas`: `Preference for user 1: action`)*

## Explanation
- **Personalization Engine**: Delivers user-specific content.
- **Logic**: Retrieves user preferences from a DataFrame.
- **Complexity**: O(n) for n users.
- **Use Case**: Used in tailored content delivery.
- **Best Practice**: Update profiles dynamically; handle missing data; ensure privacy.