# PID Controller

## Description
This snippet demonstrates PID control in simulation using a simple discrete-time model.
The examples cover a basic PID controller, integral windup mitigation, and response to changing setpoints.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Basic PID controller controlling a first-order plant.
- `SAMPLES/sample2.py`: Shows integral windup and an anti-windup mechanism.
- `SAMPLES/sample3.py`: Demonstrates PID response to a changing setpoint.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- PID control output: `u = Kp*e + Ki*∫e dt + Kd*de/dt`.
- Integral windup occurs when the integral term grows too large; anti-windup limits the integral.
- Use small time steps for stability in discrete simulation.
