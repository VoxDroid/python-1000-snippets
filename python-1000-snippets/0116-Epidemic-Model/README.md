# Epidemic Model

## Description
This snippet implements a basic SIR (Susceptible, Infected, Recovered) epidemic model using discrete time steps.

## Code
```python
def sir_model(S, I, R, beta, gamma, steps):
    history = [(S, I, R)]
    for _ in range(steps):
        new_infections = beta * S * I / (S + I + R)
        new_recoveries = gamma * I
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        history.append((S, I, R))
    return history

S, I, R = 1000, 10, 0
beta, gamma = 0.3, 0.1
print("SIR:", sir_model(S, I, R, beta, gamma, 5))
```

## Output
```
SIR: [(1000, 10, 0), (997.0, 12.0, 1.0), (993.844, 13.986, 2.17), (990.502, 16.156, 3.342), (987.003, 18.5, 4.497), (983.34, 20.994, 5.666)]
```

## Explanation
- **SIR Model**: Tracks Susceptible (S), Infected (I), and Recovered (R) populations; `beta` is infection rate, `gamma` is recovery rate.
- **Equations**: `dS = -beta * S * I / N`, `dI = beta * S * I / N - gamma * I`, `dR = gamma * I`.
- **Complexity**: O(steps) time.
- **Use Case**: Used in epidemiology or disease modeling.
- **Best Practice**: Use differential equations (e.g., with SciPy) for accuracy; validate parameters.