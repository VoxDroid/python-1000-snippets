# Control System Simulation

## Description
This snippet demonstrates PID control for a simple second-order plant using a discrete-time simulation (no external control library needed).

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Final value (approx): 0.995
First 5 output values: [0.0, 0.005, 0.018, 0.041, 0.075]
```

## Explanation
- **Control System Simulation**: Models a plant and a PID controller in discrete time.
- **sample1.py**: Simulates a step response with PID control.
- **sample2.py**: Shows how changing PID gains affects response.
- **sample3.py**: Demonstrates disturbance rejection with a step disturbance.
- **Best Practice**: Tune PID gains carefully, and validate stability and overshoot for your plant.
