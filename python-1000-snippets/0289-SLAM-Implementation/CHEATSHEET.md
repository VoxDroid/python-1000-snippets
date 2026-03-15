# 0289-SLAM-Implementation Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample1.py`
  - `python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample2.py`
  - `python python-1000-snippets/0289-SLAM-Implementation/SAMPLES/sample3.py`

## Concepts
- **EKF-SLAM**: Use Extended Kalman Filter to estimate robot pose and landmark positions simultaneously.
- **Particle Filter SLAM**: Maintain multiple hypotheses (particles) for pose and map, resample based on observation likelihood.
- **Occupancy Grid Mapping**: Update grid cells with log-odds counts from simulated rays.

## Tips
- For real SLAM, connect to odometry and sensor sources rather than simulated data.
- Tune motion and measurement noise covariances for stability.
- Visualize trajectories and maps with matplotlib for debugging.
