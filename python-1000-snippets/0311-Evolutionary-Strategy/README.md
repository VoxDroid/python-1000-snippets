# Evolutionary Strategy

## Description
This snippet implements a simple evolutionary strategy (ES) optimizer in pure Python. ES evolves a population of candidate solutions using Gaussian mutations and selection.

## Files
- `SAMPLES/sample1.py`: Minimize a sphere function (sum of squares) in 2D.
- `SAMPLES/sample2.py`: Optimize a shifted quadratic function (minimum at [1, -2]).
- `SAMPLES/sample3.py`: Optimize a one-dimensional multimodal function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best solution: [0.01 0.02], fitness: 0.0003
Best solution: [0.99 -2.01], fitness: 0.0004
Best solution: [0.79], fitness: -0.82
```

## Explanation
- **Population**: A set of candidate solutions in continuous space.
- **Mutation**: Add Gaussian noise to generate offspring.
- **Selection**: Keep the best individuals (mu+lambda strategy).
- **Use Case**: Continuous optimization, hyperparameter tuning, non-convex search.
