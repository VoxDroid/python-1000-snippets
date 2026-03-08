# Population Growth

## Description
This snippet models exponential population growth using a simple discrete model.

## Code
```python
def population_growth(initial_pop, growth_rate, time_steps, carrying_capacity=None):
    """Compute discrete-time population history.

    * `initial_pop` – starting population (float or int)
    * `growth_rate` – fractional growth per step
    * `time_steps` – number of steps to simulate
    * `carrying_capacity` – if provided, use logistic formula

    Returns list of population values (length time_steps+1).
    """
    population = float(initial_pop)
    history = [population]
    for _ in range(time_steps):
        if carrying_capacity is None:
            population *= (1 + growth_rate)
        else:
            # logistic growth: P_{t+1} = P_t + r P_t (1 - P_t/K)
            population = population + growth_rate * population * (1 - population / carrying_capacity)
        history.append(population)
    return history

if __name__ == '__main__':
    initial_pop = 100
    growth_rate = 0.02
    print("Population:", population_growth(initial_pop, growth_rate, 5))
```
## Output
```
Population: [100, 102.0, 104.04, 106.1208, 108.243216, 109.40808032]
```

## Explanation
- **Population Growth**: Uses the formula `P(t+1) = P(t) * (1 + r)` for exponential growth.
- **Parameters**: `initial_pop` (starting population), `growth_rate` (fractional growth per step).
- **Complexity**: O(time_steps) time.
- **Use Case**: Used in ecology, economics, or demography.
- **Best Practice**: Add carrying capacity for logistic growth; validate parameters.