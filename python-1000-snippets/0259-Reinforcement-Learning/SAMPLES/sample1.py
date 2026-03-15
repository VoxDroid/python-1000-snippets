# sample1.py
# Random agent in a simple 1D grid environment.

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

    total_reward = 0
    state = env.reset()
    done = False
    while not done:
        action = random.choice([0, 1])
        state, reward, done = env.step(action)
        total_reward += reward

    print(f"Episode finished. Total reward: {total_reward}")
