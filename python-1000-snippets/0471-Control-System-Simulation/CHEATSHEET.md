# 0471-Control-System-Simulation Cheatsheet

## Quick Tips
- PID control uses proportional, integral, and derivative terms to reduce error, eliminate steady-state error, and dampen overshoot.
- Use a small time step for stable simulation of continuous dynamics.
- Compare response curves to choose good gains (fast settle, low overshoot).

## Running examples
- `python SAMPLES/sample1.py` — step response with PID control.
- `python SAMPLES/sample2.py` — explore different PID gains.
- `python SAMPLES/sample3.py` — observe disturbance rejection behavior.
