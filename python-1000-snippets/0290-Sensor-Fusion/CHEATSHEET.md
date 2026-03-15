# 0290-Sensor-Fusion Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample1.py`
  - `python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample2.py`
  - `python python-1000-snippets/0290-Sensor-Fusion/SAMPLES/sample3.py`

## Concepts
- **Kalman Filter**: Optimal fusion for linear systems with Gaussian noise.
- **Complementary Filter**: Blends high-frequency gyro with low-frequency accelerometer.
- **Covariance-weighted Fusion**: Combine multiple estimates using inverse-variance weighting.

## Tips
- Tune noise covariance values to match your sensor noise characteristics.
- For dynamic motion, include a proper process model (e.g., constant velocity).
- Visualize estimates over time using matplotlib for debugging.
