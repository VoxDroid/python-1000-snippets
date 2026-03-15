# Kalman Filter

## Description
This snippet demonstrates simple Kalman filters for estimating a system state from noisy measurements.
The examples include a scalar constant-state filter, a 2D constant velocity tracker, and handling missing measurements.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: Scalar Kalman filter estimating a constant value from noisy measurements.
- `SAMPLES/sample2.py`: 2D Kalman filter tracking position and velocity from noisy position observations.
- `SAMPLES/sample3.py`: Kalman filter with missing measurements (prediction-only steps).

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Kalman filters alternate predict and update steps.
- Tune process noise and measurement noise to match your system behavior.
- Extend to higher-dimensional states by using matrices for state, covariance, and transition models.
