# sample2.py
# Train a policy using REINFORCE (policy gradient) on a simple 1D grid environment.

import numpy as np


class GridEnv:
    def __init__(self, size=5):
        self.size = size

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        # action: 0=left, 1=right
        if action == 0:
            self.state = max(0, self.state - 1)
        else:
            self.state = min(self.size - 1, self.state + 1)

        reward = 1.0 if self.state == self.size - 1 else 0.0
        done = self.state == self.size - 1
        return self.state, reward, done


def softmax(logits):
    e = np.exp(logits - np.max(logits))
    return e / e.sum()


def state_to_onehot(state, num_states):
    vec = np.zeros(num_states)
    vec[state] = 1.0
    return vec


if __name__ == '__main__':
    np.random.seed(0)

    env = GridEnv(size=5)
    num_states = env.size
    n_actions = 2

    # Policy parameters: weight matrix (state_dim, n_actions)
    weights = np.random.randn(num_states, n_actions) * 0.1

    lr = 0.1
    episodes = 200

    for ep in range(1, episodes + 1):
        state = env.reset()
        states, actions, rewards = [], [], []

        done = False
        while not done:
            s_onehot = state_to_onehot(state, num_states)
            logits = s_onehot @ weights
            probs = softmax(logits)
            action = np.random.choice(n_actions, p=probs)

            next_state, reward, done = env.step(action)

            states.append(s_onehot)
            actions.append(action)
            rewards.append(reward)

            state = next_state

        # Compute returns
        returns = np.zeros_like(rewards, dtype=float)
        G = 0.0
        for t in reversed(range(len(rewards))):
            G = rewards[t] + 0.99 * G
            returns[t] = G

        # Normalize returns
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)

        # Policy gradient update (REINFORCE)
        for s, a, G in zip(states, actions, returns):
            logits = s @ weights
            probs = softmax(logits)
            grad = -probs
            grad[a] += 1
            weights += lr * grad * G * s[:, None]

        if ep % 50 == 0 or ep == 1:
            total_reward = sum(rewards)
            print(f"Episode {ep}: total reward={total_reward}")

    # Print learned policy
    print("Learned policy (state -> action probabilities):")
    for s in range(num_states):
        probs = softmax(np.eye(num_states)[s] @ weights)
        print(f" state {s}: {probs}")
