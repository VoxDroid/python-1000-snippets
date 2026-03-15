# Q-Learning

## Description
This snippet demonstrates Q-learning on a simple grid world using NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — Q-learning training loop and Q-table printout.
- `sample2.py` — Q-learning with epsilon decay and policy extraction.
- `sample3.py` — train Q-learning and run the resulting greedy policy.

Run a sample with:

```bash
python python-1000-snippets/0260-Q-Learning/SAMPLES/sample1.py
```

## Output
Each sample prints the learned Q-table and a derived policy to illustrate how Q-learning converges.

## Notes
- This is a toy example; real environments use more states and actions and often use function approximation (e.g., neural networks).
- The core update rule is:

```python
Q[s,a] += alpha * (reward + gamma * max(Q[next_state]) - Q[s,a])
```

- Use epsilon-greedy exploration to balance exploration and exploitation.
