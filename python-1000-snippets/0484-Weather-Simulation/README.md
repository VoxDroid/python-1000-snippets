# Weather Simulation

## Description
This snippet demonstrates weather simulation using pure Python time series computations.

## Code
The sample scripts show:
- `sample1.py`: Temperature series with trend and noise.
- `sample2.py`: Pressure/humidity evolution over steps.
- `sample3.py`: Wind chill index calculation.

## Output
`sample1.py` prints a simulated temperature time series with min/max.

`sample2.py` prints first/last values from a pressure/humidity trajectory.

`sample3.py` prints wind chill values for sample pairs.

## Explanation
- **Weather Simulation**: Simulates weather variables with simple rules.
- **Logic**: Uses series generation and formulaic calculations.
- **Complexity**: O(n) for n time points.
- **Use Case**: Useful for teaching or prototyping environmental systems.
- **Best Practice**: Include seasonality, hysteresis, and constraints in realistic models.
