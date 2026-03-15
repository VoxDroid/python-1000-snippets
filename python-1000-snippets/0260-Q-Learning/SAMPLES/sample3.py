# sample3.py
# Run a learned Q-learning policy in the grid environment.

import numpy as np


class SimpleGridEnv:
    def __init__(self, size=5):
        self.size = size
        self.reset()

    def reset(self):
        self.pos = 0
        return self.pos

    def step(self, action):
        # action: 0=left, 1=right
        if action == 0:
            self.pos = max(0, self.pos - 1)
        else:
            self.pos = min(self.size - 1, self.pos + 1)

        done = self.pos == (self.size - 1)
        reward = 1 if done else 0
        return self.pos, reward, done


def train_q_learning(episodes=300, alpha=0.1, gamma=0.9, epsilon=0.2):
    q_table = np.zeros((5, 2))
    rewards = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 10]])
    step_reward = -0.1

    for _ in range(episodes):
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

    return q_table


def run_policy(env, policy, episodes=5):
    for ep in range(1, episodes + 1):
        state = env.reset()
        done = False
        steps = 0
        while not done and steps < 20:
            action = int(policy[state])
            state, reward, done = env.step(action)
            steps += 1
        print(f"Episode {ep} finished in {steps} steps")


if __name__ == '__main__':
    env = SimpleGridEnv(size=5)
    q_table = train_q_learning()
    policy = np.argmax(q_table, axis=1)

    print("Learned policy (0=left,1=right):", policy)
    run_policy(env, policy)
