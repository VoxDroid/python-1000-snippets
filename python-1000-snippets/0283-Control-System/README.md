# Control System

## Description
This snippet demonstrates basic control system concepts using simple numerical simulation.
It includes step response of a second-order system, PID control of a first-order plant, and PD control of a second-order plant.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Compute a step response of a critically damped second-order system analytically.
- `SAMPLES/sample2.py`: Simulate a PID controller acting on a first-order plant.
- `SAMPLES/sample3.py`: Simulate a PD controller acting on a second-order plant.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Control systems often use differential equations; these examples use simple discrete-time integration.
- PID controllers adjust control output based on error, integral, and derivative terms.
- Tuning gains (Kp, Ki, Kd) affects response speed and stability.
