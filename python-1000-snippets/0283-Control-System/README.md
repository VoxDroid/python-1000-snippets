# Control System

## Description
This snippet demonstrates a simple control system simulation using `control`.

## Code
```python
# Note: Requires `control`. Install with `pip install control`
try:
    from control import tf, step_response
    import numpy as np
    sys = tf([1], [1, 2, 1])  # Transfer function: 1/(s^2 + 2s + 1)
    t, y = step_response(sys, T=np.linspace(0, 5, 100))
    print("Final Output:", y[-1])
except ImportError:
    print("Mock Output: Final Output: 1.0")
```

## Output
```
Mock Output: Final Output: 1.0
```
*(Real output with `control`: `Final Output: <value around 1.0>`)*

## Explanation
- **Control System**: Simulates a second-order system’s step response.
- **Logic**: Defines a transfer function and computes the response.
- **Complexity**: O(n) for n time points.
- **Use Case**: Used for analyzing system dynamics.
- **Best Practice**: Validate model; tune parameters; check stability.