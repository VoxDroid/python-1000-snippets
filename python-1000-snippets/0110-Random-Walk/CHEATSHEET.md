# 0110-Random-Walk Cheatsheet

- A 1D random walk moves in steps of +1 or -1 with equal probability.
- Extend to 2D: step vectors chosen from [(1,0),(-1,0),(0,1),(0,-1)].
- Use `random.choice` or `numpy.random.choice` for vectorized sampling.
- Track positions list; compute displacement or average distance over trials.
- Useful analysis: mean squared displacement ~ steps, distribution approximates normal.
- For multiple walkers, simulate ensemble and compute statistics.
