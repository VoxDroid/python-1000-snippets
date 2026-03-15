# sample3.py
# Train a policy with policy-gradient and then evaluate it deterministically.

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


def train_policy(episodes=200, lr=0.1):
    env = GridEnv(size=5)
    num_states = env.size
    n_actions = 2

    weights = np.random.randn(num_states, n_actions) * 0.1

    for _ in range(episodes):
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

        # REINFORCE update
        returns = np.zeros_like(rewards, dtype=float)
        G = 0.0
        for t in reversed(range(len(rewards))):
            G = rewards[t] + 0.99 * G
            returns[t] = G
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)

        for s, a, G in zip(states, actions, returns):
            logits = s @ weights
            probs = softmax(logits)
            grad = -probs
            grad[a] += 1
            weights += lr * grad * G * s[:, None]

    return weights


def evaluate_policy(weights, episodes=10):
    env = GridEnv(size=5)
    total_rewards = []
    for _ in range(episodes):
        state = env.reset()
        done = False
        ep_reward = 0.0
        while not done:
            s_onehot = state_to_onehot(state, env.size)
            probs = softmax(s_onehot @ weights)
            action = int(np.argmax(probs))
            state, reward, done = env.step(action)
            ep_reward += reward
        total_rewards.append(ep_reward)
    return np.mean(total_rewards)


if __name__ == '__main__':
    np.random.seed(0)

    weights = train_policy(episodes=300, lr=0.1)
    avg_reward = evaluate_policy(weights, episodes=20)
    print(f"Average reward (greedy policy): {avg_reward:.3f}")
