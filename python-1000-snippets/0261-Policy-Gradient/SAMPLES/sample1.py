# sample1.py
# Demonstrate a simple softmax policy that selects actions based on state features.

import numpy as np


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


if __name__ == '__main__':
    np.random.seed(0)

    # Policy parameters: state_dim x n_actions
    state_dim = 5  # one-hot encoding of 5 states
    n_actions = 2
    policy_weights = np.random.randn(state_dim, n_actions) * 0.1

    # Example state: one-hot for state 2
    state = np.zeros(state_dim)
    state[2] = 1.0

    logits = state @ policy_weights
    probs = softmax(logits)

    print("State:", state)
    print("Action logits:", logits)
    print("Action probabilities:", probs)
    print("Sampled action:", np.random.choice(n_actions, p=probs))
