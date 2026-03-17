# Hill Climbing

## Description
This snippet implements a simple hill climbing optimization algorithm. Hill climbing iteratively moves to better neighbors until no improvement is found.

## Files
- `SAMPLES/sample1.py`: Hill climbing on a 2D sphere function.
- `SAMPLES/sample2.py`: Hill climbing on a shifted quadratic function.
- `SAMPLES/sample3.py`: Hill climbing on a multimodal 1D function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best solution: [0.00 0.00], fitness: 0.0000
Best solution: [1.00 -2.00], fitness: 0.0000
Best solution: [0.78], fitness: -0.82
```

## Explanation
- **Neighborhood search**: Evaluates nearby candidate solutions to find improvements.
- **Greedy update**: Moves to the best neighbor if it improves the objective.
- **Termination**: Stops when no neighbor yields improvement.
- **Use Case**: Quick local optimization when global optima are not required.
