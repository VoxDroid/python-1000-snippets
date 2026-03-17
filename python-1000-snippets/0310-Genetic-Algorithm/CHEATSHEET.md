# 0310 - Genetic Algorithm Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use **roulette wheel** or **tournament selection** to favor fitter individuals.
- Crossover (single-point, two-point, uniform) combines parents into children.
- Mutation prevents premature convergence; keep mutation rate low (e.g., 1-5%).
- Fitness functions should map to a scalar objective; higher is better.
