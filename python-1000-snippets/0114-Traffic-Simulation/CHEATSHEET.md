# 0114-Traffic-Simulation Cheatsheet

- **Purpose**: simulate a single‑light intersection with random arrivals.
- **Key arguments**:
  * `cycles`: time steps to run
  * `arrival_rate`: probability of a car arriving each step (0–1)
  * `green_duration`: how often the light toggles
  * `cars_per_green`: throughput when light turns green
  * `seed`: reproducible random behaviour

```python
from traffic_simulation import traffic_simulation

# deterministic run
print(traffic_simulation(100, 0.4, green_duration=5, seed=1))

# compare different arrival rates
for r in (0.1, 0.3, 0.5):
    print(r, traffic_simulation(100, r, seed=42))
```

- Use loops or Monte Carlo trials to estimate average wait times under different policies.
- Seed the RNG for unit tests.

