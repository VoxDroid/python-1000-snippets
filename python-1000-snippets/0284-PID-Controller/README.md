# PID Controller

## Description
This snippet demonstrates a PID controller simulation using `numpy`.

## Code
```python
import numpy as np
setpoint = 1.0
Kp, Ki, Kd = 1.0, 0.1, 0.01
error, integral, prev_error = 0.0, 0.0, 0.0
y = 0.0
dt = 0.1
error = setpoint - y
integral += error * dt
derivative = (error - prev_error) / dt
u = Kp * error + Ki * integral + Kd * derivative
y += u * dt
print("Control Output:", u)
```

## Output
```
Control Output: 1.11
```

## Explanation
- **PID Controller**: Computes control output for a single step.
- **Logic**: Uses proportional, integral, and derivative terms to adjust output.
- **Complexity**: O(1) per step.
- **Use Case**: Used for stabilizing systems like drones or heaters.
- **Best Practice**: Tune PID gains; handle integral windup; test in simulation.