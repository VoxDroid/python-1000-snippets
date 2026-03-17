# 0313 - Ant Colony Optimization Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use pheromone evaporation to avoid getting stuck in local optima.
- Choose heuristic desirability (e.g., 1/distance) to bias short paths.
- Maintain a pheromone matrix and update it based on best tours each iteration.
- For small graphs, brute-force is possible; ACO scales to larger TSP instances.
