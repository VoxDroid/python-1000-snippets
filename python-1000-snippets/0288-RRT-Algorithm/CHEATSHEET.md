# 0288-RRT-Algorithm Cheatsheet

## Quick Start
- Run a sample:
  - `python python-1000-snippets/0288-RRT-Algorithm/SAMPLES/sample1.py`
  - `python python-1000-snippets/0288-RRT-Algorithm/SAMPLES/sample2.py`
  - `python python-1000-snippets/0288-RRT-Algorithm/SAMPLES/sample3.py`

## Concepts
- **RRT**: Randomly sample space, connect to nearest node, and grow a tree.
- **Goal bias**: Occasionally sample the goal directly to improve success rate.
- **RRT***: Rewire nearby nodes to reduce path cost (as in sample3).

## Tips
- Increase `max_iterations` or `step_size` to influence how fast the tree grows.
- Add more obstacles to test collision handling.
- For visualization, export node positions and plot with matplotlib.
