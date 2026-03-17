# Simulated Annealing

## Description
This snippet implements simulated annealing (SA) for continuous optimization. SA probabilistically accepts worse solutions to escape local minima, with acceptance probability decreasing over time.

## Files
- `SAMPLES/sample1.py`: Minimize a 2D sphere function using SA.
- `SAMPLES/sample2.py`: Optimize a shifted quadratic function.
- `SAMPLES/sample3.py`: Minimize a multimodal 1D function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best solution: [0.01 0.02], fitness: 0.0004
Best solution: [0.99 -2.01], fitness: 0.0001
Best solution: [1.27], fitness: -0.96
```

## Explanation
- **Temperature**: Controls probability of accepting worse solutions; decreases over time.
- **Neighbor generation**: Propose new candidate by perturbing current solution.
- **Acceptance**: Accept if better, or with probability `exp(-(delta)/T)` if worse.
- **Use Case**: Non-convex optimization, combinatorial search.
