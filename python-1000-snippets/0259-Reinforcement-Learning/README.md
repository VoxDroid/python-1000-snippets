# Reinforcement Learning

## Description
This snippet demonstrates a simple reinforcement learning setup using `gym`.

## Code
```python
# Note: Requires `gym`. Install with `pip install gym`
try:
    import gym
    env = gym.make("CartPole-v1")
    for _ in range(1):
        state = env.reset()
        done = False
        while not done:
            action = env.action_space.sample()
            state, reward, done, _ = env.step(action)
        print("Episode finished")
    env.close()
except ImportError:
    print("Mock Output: Episode finished")
```

## Output
```
Mock Output: Episode finished
```
*(Real output with `gym`: `Episode finished`)*

## Explanation
- **Reinforcement Learning**: Runs a random agent in the CartPole environment.
- **Logic**: Samples actions and steps through the environment until done.
- **Complexity**: O(T) for T timesteps per episode.
- **Use Case**: Used for training agents in games or robotics.
- **Best Practice**: Implement a policy; use Q-learning or DQN; tune exploration.