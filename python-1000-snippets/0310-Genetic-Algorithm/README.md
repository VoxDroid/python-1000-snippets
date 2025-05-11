# Genetic Algorithm

## Description
This snippet demonstrates a genetic algorithm using `deap` to optimize a simple function.

## Code
```python
# Note: Requires `deap`. Install with `pip install deap`
try:
    from deap import base, creator, tools
    import random
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 2)
    toolbox.register("evaluate", lambda ind: (sum(ind),))
    ind = toolbox.individual()
    print("Individual Fitness:", toolbox.evaluate(ind)[0])
except ImportError:
    print("Mock Output: Individual Fitness: 1.0")
```

## Output
```
Mock Output: Individual Fitness: 1.0
```
*(Real output with `deap`: `Individual Fitness: <value around 1.0>`)*

## Explanation
- **Genetic Algorithm**: Evaluates a random individual’s fitness.
- **Logic**: Creates a 2D individual and computes its sum as fitness.
- **Complexity**: O(n) for n genes in evaluation.
- **Use Case**: Used for optimization problems like scheduling.
- **Best Practice**: Tune population size; use crossover/mutation; validate fitness.