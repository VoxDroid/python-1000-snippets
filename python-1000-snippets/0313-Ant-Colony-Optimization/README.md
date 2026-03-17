# Ant Colony Optimization

## Description
This snippet implements a simple Ant Colony Optimization (ACO) algorithm for the Traveling Salesman Problem (TSP). Ants build tours probabilistically based on pheromone levels and edge distances.

## Files
- `SAMPLES/sample1.py`: ACO on a small fixed 4-node graph.
- `SAMPLES/sample2.py`: ACO on a random 5-node distance matrix.
- `SAMPLES/sample3.py`: ACO with pheromone evaporation and reinforcement.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best tour: [0, 2, 1, 3, 0], length: 3.45
Best tour: [0, 3, 2, 1, 4, 0], length: 4.92
Best tour: [0, 2, 4, 1, 3, 0], length: 4.12
```

## Explanation
- **Pheromones**: Guide ants toward promising edges; updated based on tour quality.
- **Heuristic**: Often inverse of distance (shorter edges preferred).
- **Evaporation**: Prevents premature convergence by reducing pheromone on all edges.
- **Use Case**: Common for routing and scheduling problems.
