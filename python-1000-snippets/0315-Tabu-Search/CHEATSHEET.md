# 0315 - Tabu Search Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Keep a fixed-size tabu list (recent moves) to avoid cycles.
- Allow tabu moves if they produce a new best solution (aspiration criterion).
- Explore neighborhood by perturbing the current solution.
- Use a scoring function to compare neighbors and track the best solution found.
