# 0316 - Hill Climbing Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Define a neighborhood function that generates local candidate solutions.
- Evaluate all neighbors and move to the one with the best improvement.
- Stop when no neighbor improves the current solution (local optimum).
- For noisy or multimodal functions, repeat with random restarts.
