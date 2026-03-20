# 0483-Crowd-Simulation Cheatsheet

## Quick Start
Run a sample:
```bash
python3 python-1000-snippets/0483-Crowd-Simulation/SAMPLES/sample1.py
```

## Concepts
- Random-walk movement for agents.
- Grid-based crowd density histogram.
- Attraction/repulsion updates for group dynamics.

## Notes
- `sample1.py`: random walk update
- `sample2.py`: density cell counting
- `sample3.py`: simple social force step

## Tips
- Increase agent count for large-scale tests (be careful with performance). 
- Add a `max_force` cap and obstacle avoidance in `sample3` for real behavior.
