# 0311 - Evolutionary Strategy Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- In (µ+λ)-ES, generate λ offspring from µ parents, then select the best µ individuals.
- Mutation strength (step size) is critical: too large = random search, too small = slow convergence.
- Use recombination (averaging parents) to mix solutions.
- Evaluate fitness on the full solution vector (minimize or maximize as needed).
