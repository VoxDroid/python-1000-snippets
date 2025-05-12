# Control System Simulation

## Description
This snippet demonstrates a PID control system simulation using `control`.

## Code
```python
# Note: Requires `control`. Install with `pip install control`
try:
    import control
    import numpy as np
    s = control.tf('s')
    plant = 1 / (s**2 + s + 1)
    Kp, Ki, Kd = 1.0, 0.1, 0.5
    controller = Kp + Ki/s + Kd*s
    sys = control.feedback(controller * plant)
    t, y = control.step_response(sys, T=np.linspace(0, 10, 100))
    print("Response shape:", y.shape)
except ImportError:
    print("Mock Output: Response shape: (100,)")
```

## Output
```
Mock Output: Response shape: (100,)
```
*(Real output with `control`: `Response shape: (100,)`)*

## Explanation
- **Control System Simulation**: Simulates a PID controller response.
- **Logic**: Defines a plant and PID controller, computes step response.
- **Complexity**: O(n) for n time points.
- **Use Case**: Used in robotics or process control.
- **Best Practice**: Tune PID parameters; validate stability; visualize response.