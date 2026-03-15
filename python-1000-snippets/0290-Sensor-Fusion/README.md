# Sensor Fusion

## Description
This snippet demonstrates several sensor fusion techniques using `numpy`.

## Samples
- `SAMPLES/sample1.py`: Kalman filter fusing accelerometer and GPS for 1D position.
- `SAMPLES/sample2.py`: Complementary filter fusing gyro and accelerometer for roll estimation.
- `SAMPLES/sample3.py`: Covariance-weighted fusion of two noisy sensor estimates.

## Running
```bash
python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample1.py
python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample2.py
python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample3.py
```

## Notes
- All scripts are seeded for deterministic output.
- In real systems, replace simulated sensor readings with live data streams.
