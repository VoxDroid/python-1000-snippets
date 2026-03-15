# Q-Learning Cheatsheet

## Key Concepts
- **Q-table**: stores the expected return for each state-action pair.
- **Update rule**: `Q[s,a] += alpha * (reward + gamma * max(Q[next_s]) - Q[s,a])`.
- **Epsilon-greedy**: choose a random action with probability epsilon; otherwise choose the best action.

## Running Samples
```bash
python python-1000-snippets/0260-Q-Learning/SAMPLES/sample1.py
python python-1000-snippets/0260-Q-Learning/SAMPLES/sample2.py
python python-1000-snippets/0260-Q-Learning/SAMPLES/sample3.py
```

## Tips
- Decay epsilon over time to shift from exploration to exploitation.
- Smaller alpha values lead to smoother but slower learning.
- Q-learning works well for small discrete state/action spaces.
