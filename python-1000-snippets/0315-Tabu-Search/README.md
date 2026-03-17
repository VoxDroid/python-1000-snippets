# Tabu Search

## Description
This snippet implements Tabu Search (TS), a local search metaheuristic that avoids revisiting recently explored solutions by maintaining a tabu list.

## Files
- `SAMPLES/sample1.py`: TS optimizing a 2D sphere function.
- `SAMPLES/sample2.py`: TS optimizing a shifted quadratic function.
- `SAMPLES/sample3.py`: TS optimizing a multimodal 1D function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best solution: [0.01 0.01], fitness: 0.0002
Best solution: [1.00 -2.00], fitness: 0.0000
Best solution: [1.27], fitness: -0.96
```

## Explanation
- **Tabu list**: Tracks recent moves to prevent cycling.
- **Neighborhood**: Generate candidate solutions near the current solution.
- **Aspiration**: Allow tabu moves if they yield a better solution.
- **Use Case**: Combinatorial and continuous optimization where local minima are common.
