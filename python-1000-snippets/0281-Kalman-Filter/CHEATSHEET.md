# 0281 - Kalman Filter Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Kalman filter consists of **predict** and **update** steps.
- Prediction: `x = F @ x`, `P = F @ P @ F.T + Q`
- Update: `K = P @ H.T @ inv(H @ P @ H.T + R); x = x + K @ (z - H @ x)`
- Use a larger process noise (`Q`) to trust measurements more, and larger measurement noise (`R`) to trust the model more.
