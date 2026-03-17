# 0314 - Simulated Annealing Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use a temperature schedule (e.g., `T *= 0.99`) to gradually reduce acceptance of worse solutions.
- Generate neighbors by adding small random perturbations to the current solution.
- Accept worse solutions with probability `exp(-(delta)/T)` to escape local minima.
- Monitor best found solution over time.
