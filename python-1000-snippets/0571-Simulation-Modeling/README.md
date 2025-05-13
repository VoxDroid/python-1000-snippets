# Simulation Modeling

## Description
This snippet demonstrates a simple queue simulation using `simpy`.

## Code
```python
# Note: Requires `simpy`. Install with `pip install simpy`
try:
    import simpy
    def customer(env):
        yield env.timeout(1)
        return "Customer served"
    env = simpy.Environment()
    process = env.process(customer(env))
    env.run()
    print("Simulation completed")
except ImportError:
    print("Mock Output: Simulation completed")
```

## Output
```
Mock Output: Simulation completed
```
*(Real output with `simpy`: `Simulation completed`)*

## Explanation
- **Simulation Modeling**: Simulates a customer service process.
- **Logic**: Uses `simpy` to model a customer with a 1-unit time delay.
- **Complexity**: O(n) for n events in the simulation.
- **Use Case**: Used for modeling queues, networks, or processes.
- **Best Practice**: Define realistic events; validate model; analyze results.