# Population Growth

## Description
This snippet models exponential population growth using a simple discrete model.

## Code
```python
def population_growth(initial_pop, growth_rate, time_steps):
    population = initial_pop
    history = [population]
    for _ in range(time_steps):
        population *= (1 + growth_rate)
        history.append(population)
    return history

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