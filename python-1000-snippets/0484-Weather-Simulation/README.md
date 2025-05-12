# Weather Simulation

## Description
This snippet demonstrates a simple weather simulation using `numpy`.

## Code
```python
try:
    import numpy as np
    temperature = 20 + np.random.randn(10) * 2
    print("Temperatures:", temperature[:3])
except ImportError:
    print("Mock Output: Temperatures: [20.1 19.8 21.2]")
```

## Output
```
Mock Output: Temperatures: [20.1 19.8 21.2]
```
*(Real output with `numpy`: `Temperatures: <random temperatures>`)*

## Explanation
- **Weather Simulation**: Simulates temperature fluctuations.
- **Logic**: Generates temperatures with Gaussian noise.
- **Complexity**: O(n) for n time points.
- **Use Case**: Used in climate modeling or game environments.
- **Best Practice**: Model multiple variables; validate ranges; add trends.