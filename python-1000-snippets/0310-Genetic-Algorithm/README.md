# Genetic Algorithm

## Description
This snippet implements a simple genetic algorithm (GA) in pure Python without external dependencies. The GA evolves a population of candidate solutions using selection, crossover, and mutation.

## Files
- `SAMPLES/sample1.py`: Binary-string optimization (maximize number of 1s).
- `SAMPLES/sample2.py`: Real-valued optimization of a quadratic function (minimize (x-3)^2).
- `SAMPLES/sample3.py`: Knapsack problem solver using a GA.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best individual: [1, 1, 1, 1, 1], fitness: 5.00
Best x: 2.97, fitness: 0.0009
Best value: 7, weight: 8
```

## Explanation
- **Population**: A list of candidate solutions (chromosomes).
- **Selection**: Picks fitter individuals for reproduction.
- **Crossover**: Combines parents to create children.
- **Mutation**: Introduces random changes to maintain diversity.
