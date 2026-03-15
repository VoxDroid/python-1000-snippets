# SLAM Implementation

## Description
This snippet demonstrates basic Simultaneous Localization and Mapping (SLAM) techniques using `numpy`.

## Samples
- `SAMPLES/sample1.py`: 2D EKF-SLAM with two landmarks and pose estimation.
- `SAMPLES/sample2.py`: Particle filter SLAM (Monte Carlo localization + landmark estimation).
- `SAMPLES/sample3.py`: Occupancy grid mapping using simulated range scans.

## Running
```bash
python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample1.py
python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample2.py
python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample3.py
```

## Notes
- These examples are deterministic (seeded) and do not require user input.
- For real-world SLAM, replace simulated controls and observations with actual sensor data.
