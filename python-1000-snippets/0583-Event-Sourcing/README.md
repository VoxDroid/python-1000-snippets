# Event Sourcing

## Description
This snippet demonstrates event sourcing for state reconstruction.

## Code
```python
try:
    events = [{"type": "add", "value": 5}, {"type": "add", "value": 3}]
    def reconstruct_state(events):
        state = 0
        for event in events:
            if event["type"] == "add":
                state += event["value"]
        return state
    print("Reconstructed state:", reconstruct_state(events))
except ImportError:
    print("Mock Output: Reconstructed state: 8")
```

## Output
```
Mock Output: Reconstructed state: 8
```
*(Real output: `Reconstructed state: 8`)*

## Explanation
- **Event Sourcing**: Rebuilds state from stored events.
- **Logic**: Sums values from "add" events.
- **Complexity**: O(n) for n events.
- **Use Case**: Used in systems requiring auditability.
- **Best Practice**: Store events reliably; validate events; handle replays.