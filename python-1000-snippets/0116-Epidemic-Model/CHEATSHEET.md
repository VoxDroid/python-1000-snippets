# 0116-Epidemic-Model Cheatsheet

- **Purpose**: compute the SIR epidemic trajectory using simple discrete steps.
- **Parameters**:
  * `S, I, R`: initial counts (can be floats for proportions).
  * `beta`: infection rate constant.
  * `gamma`: recovery rate constant.
  * `steps`: number of iterations to simulate.
  * `seed`: reserved for reproducibility if stochastic extension added.

```python
from epidemic_model import sir_model

print(sir_model(990, 10, 0, 0.3, 0.1, 10))
```

- The model assumes homogeneous mixing; extensions include SEIR or network structure.
- Plot results with matplotlib: extract columns for S, I, R.

