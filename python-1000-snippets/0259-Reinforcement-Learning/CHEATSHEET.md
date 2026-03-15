# Reinforcement Learning Cheatsheet

## Key Concepts
- **Environment**: defined by states, actions, rewards, and transitions.
- **Q-learning**: a value-based RL algorithm that learns `Q(s, a)` values.
- **Epsilon-greedy**: explore random actions with probability epsilon, otherwise exploit best known action.

## Running Samples
```bash
python python-1000-snippets/0259-Reinforcement-Learning/SAMPLES/sample1.py
python python-1000-snippets/0259-Reinforcement-Learning/SAMPLES/sample2.py
python python-1000-snippets/0259-Reinforcement-Learning/SAMPLES/sample3.py
```

## Tips
- Decrease epsilon over time to shift from exploration to exploitation.
- Q-learning updates: `Q[s,a] += alpha * (reward + gamma * max(Q[next_state]) - Q[s,a])`.
- Use a simple environment to validate your RL implementation before moving to complex tasks.
