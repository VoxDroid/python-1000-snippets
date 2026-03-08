# 0115-Population-Growth Cheatsheet

- **Purpose**: model discrete population growth, either exponential or logistic.
- **Parameters**:
  * `initial_pop`: starting population
  * `growth_rate`: per-step fractional increase
  * `time_steps`: number of iterations
  * `carrying_capacity`: optional, switches to logistic growth

```python
from population_growth import population_growth

print(population_growth(50, 0.05, 10))             # exponential
print(population_growth(50, 0.05, 10, carrying_capacity=200))  # logistic
```

- Logistic formula: `P_{t+1}=P_t + r P_t (1 - P_t/K)`.
- Useful in ecology, finance, or any process with bounded growth.
- Plot the returned history with matplotlib for visualization.

