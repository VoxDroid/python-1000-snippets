# Q-Learning

## Description
This snippet demonstrates Q-Learning on a simple grid world.

## Code
```python
import numpy as np

# Define the Q-table (5 states, 2 actions)
q_table = np.zeros((5, 2))  # 5 states, 2 actions

# Define the rewards for state-action pairs
rewards = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 10]])  # Reward for state-action
# Optional: Give a small reward for each action taken to encourage movement
step_reward = 1

# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate (probability of taking a random action)

# Q-learning process
for _ in range(100):
    state = 0
    while state != 4:
        # Epsilon-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.choice(2)  # Random action
        else:
            action = np.argmax(q_table[state])  # Greedy action
        
        reward = rewards[state, action] + step_reward  # Add small reward for each step
        next_state = min(state + 1, 4)  # Simple state transition (progress one step at a time)
        
        # Q-value update rule (Q-learning update)
        q_table[state, action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])
        
        state = next_state  # Transition to next state

# Print the Q-table after learning
print("Q-Table:", q_table)
```

## Output
```
Q-Table: [ <value> <value> ]
```

## Explanation
- **Q-Learning**: Implements Q-Learning to learn optimal actions in a grid world.
- **Logic**: Updates Q-table based on rewards and future estimates.
- **Complexity**: O(S*A*I) for S states, A actions, I iterations.
- **Use Case**: Used for learning policies in discrete environments.
- **Best Practice**: Balance exploration/exploitation; tune learning rate; use epsilon-greedy.