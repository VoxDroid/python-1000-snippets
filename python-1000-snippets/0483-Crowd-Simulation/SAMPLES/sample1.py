# sample1.py
# Simulate a small crowd with random walk positions (pure Python).

import random


def initialize_agents(count=10, bounds=10.0):
    return [[random.uniform(0, bounds), random.uniform(0, bounds)] for _ in range(count)]


def step_agents(agents, step_size=0.5, bounds=10.0):
    for agent in agents:
        agent[0] = max(0, min(bounds, agent[0] + random.uniform(-step_size, step_size)))
        agent[1] = max(0, min(bounds, agent[1] + random.uniform(-step_size, step_size)))


def main() -> None:
    agents = initialize_agents(10)
    print('Initial (first 3):', agents[:3])
    for t in range(5):
        step_agents(agents)
    print('After 5 steps (first 3):', agents[:3])


if __name__ == '__main__':
    main()
