# sample2.py
# Q-learning with epsilon decay and policy extraction.

import numpy as np


def run_q_learning(episodes=300, alpha=0.1, gamma=0.9, epsilon=1.0, min_epsilon=0.05):
    q_table = np.zeros((5, 2))
    rewards = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 10]])
    step_reward = -0.1

    for ep in range(1, episodes + 1):
        state = 0
        done = False
        while not done:
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
            done = state == 4

        # Decay exploration
        epsilon = max(min_epsilon, epsilon * 0.99)

        if ep % 50 == 0 or ep == 1:
            print(f"Episode {ep}, epsilon={epsilon:.3f}")

    return q_table


if __name__ == '__main__':
    q_table = run_q_learning()
    policy = np.argmax(q_table, axis=1)

    print("Learned policy (0=left,1=right):")
    print(policy)
    print("Q-table:")
    print(q_table)
