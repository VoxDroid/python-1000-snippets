# sample1.py
# Simple Q-learning example on a small grid world using NumPy.

import numpy as np


def run_q_learning(episodes=100, alpha=0.1, gamma=0.9, epsilon=0.2):
    q_table = np.zeros((5, 2))  # 5 states, 2 actions
    rewards = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 10]])
    step_reward = -0.1

    for _ in range(episodes):
        state = 0
        while state != 4:
            if np.random.rand() < epsilon:
                action = np.random.choice(2)
            else:
                action = int(np.argmax(q_table[state]))

            reward = rewards[state, action] + step_reward
            next_state = min(state + 1, 4)

            td_target = reward + gamma * np.max(q_table[next_state])
            td_error = td_target - q_table[state, action]
            q_table[state, action] += alpha * td_error

            state = next_state

    return q_table


if __name__ == '__main__':
    q_table = run_q_learning(episodes=200)
    print("Learned Q-table:")
    print(q_table)
