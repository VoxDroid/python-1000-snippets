# sample2.py
# Simple Q-learning on the 1D grid environment.

import random


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


if __name__ == '__main__':
    env = SimpleGridEnv(size=5)
    num_states = env.size
    num_actions = 2

    Q = [[0.0 for _ in range(num_actions)] for _ in range(num_states)]

    epsilon = 0.1
    alpha = 0.5
    gamma = 0.9
    episodes = 200

    for ep in range(1, episodes + 1):
        state = env.reset()
        done = False
        steps = 0

        while not done and steps < 50:
            if random.random() < epsilon:
                action = random.choice([0, 1])
            else:
                action = int(Q[state].index(max(Q[state])))

            next_state, reward, done = env.step(action)
            best_next = max(Q[next_state])
            td_target = reward + gamma * best_next
            td_delta = td_target - Q[state][action]
            Q[state][action] += alpha * td_delta

            state = next_state
            steps += 1

        if ep % 50 == 0 or ep == 1:
            print(f"Episode {ep}, steps: {steps}")

    print("Learned Q-table:")
    for s in range(num_states):
        print(f"state {s}: {Q[s]}")
