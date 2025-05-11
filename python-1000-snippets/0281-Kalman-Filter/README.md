# Kalman Filter

## Description
This snippet demonstrates a simple Kalman Filter using `numpy`.

## Code
```python
import numpy as np
x = np.array([0.0])  # Initial state
P = np.array([1.0])  # Initial uncertainty
Q = 0.01  # Process noise
R = 0.1   # Measurement noise
z = 1.0   # Measurement
F = 1.0   # State transition
H = 1.0   # Measurement function
x = F * x
P = F * P * F + Q
K = P * H / (H * P * H + R)
x = x + K * (z - H * x)
P = (1 - K * H) * P
print("Estimated State:", x)
```

## Output
```
Estimated State: 0.90990991
```

## Explanation
- **Kalman Filter**: Estimates state from noisy measurements.
- **Logic**: Applies predict and update steps for a 1D system.
- **Complexity**: O(1) for scalar state.
- **Use Case**: Used for sensor fusion or tracking.
- **Best Practice**: Tune noise parameters; validate model; extend to multi-dimensional states.