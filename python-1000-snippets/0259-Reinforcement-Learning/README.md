# Reinforcement Learning

## Description
This snippet demonstrates simple reinforcement learning concepts using a minimal custom environment implemented in plain Python.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — runs a random policy in a simple 1D grid environment.
- `sample2.py` — trains a Q-learning agent to reach a goal in the grid.
- `sample3.py` — trains Q-learning and then runs the learned greedy policy.

Run a sample with:

```bash
python python-1000-snippets/0259-Reinforcement-Learning/SAMPLES/sample2.py
```

## Output
Each sample prints progress or learned Q-values to show how an agent improves over time.

## Notes
- This is a toy environment to illustrate core RL concepts without external dependencies.
- For real RL, use environments like OpenAI Gym and deep Q-networks or policy gradients.
