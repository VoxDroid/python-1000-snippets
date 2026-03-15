# Particle Filter

## Description
This snippet demonstrates particle filter techniques for state estimation using a set of weighted particles.
It includes examples of resampling, effective sample size, and tracking in 1D and 2D.

## Dependencies
- `numpy`

Install with:
```bash
pip install numpy
```

## Samples
- `SAMPLES/sample1.py`: 1D particle filter estimating a constant state from noisy measurements.
- `SAMPLES/sample2.py`: Demonstrates resampling degeneracy and the effect on effective sample size.
- `SAMPLES/sample3.py`: 2D particle filter estimating position from noisy distance measurements.

## Running
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Particle filters are useful for non-linear, non-Gaussian state estimation.
- Common steps: prediction (propagate particles), weight update (likelihood), and resampling (avoid degeneracy).
- Monitor effective sample size (ESS) to decide when to resample.
