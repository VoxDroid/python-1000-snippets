# Feature Toggling

## Description
This snippet demonstrates enabling/disabling a feature.

## Code
```python
try:
    features = {"new_ui": False}
    def is_enabled(feature):
        return features.get(feature, False)
    print("Feature new_ui:", "enabled" if is_enabled("new_ui") else "disabled")
except ImportError:
    print("Mock Output: Feature new_ui: disabled")
```

## Output
```
Mock Output: Feature new_ui: disabled
```
*(Real output: `Feature new_ui: disabled`)*

## Explanation
- **Feature Toggling**: Controls feature availability.
- **Logic**: Checks if a feature is enabled in a dictionary.
- **Complexity**: O(1) per check.
- **Use Case**: Used for rolling out features gradually.
- **Best Practice**: Centralize toggles; log usage; test both states.