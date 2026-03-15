# 0283 - Control System Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Step response of a critically damped second-order system: `y(t)=1-(1+ωt)e^{-ωt}`.
- PID controller formula: `u = Kp*e + Ki*∫e dt + Kd*de/dt`.
- Use small `dt` for stable discrete-time integration; adjust gains for desired dynamics.
