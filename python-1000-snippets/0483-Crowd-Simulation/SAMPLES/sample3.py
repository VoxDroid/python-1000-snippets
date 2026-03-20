# sample3.py
# Model simple attraction/repulsion behavior among agents.

import math


def step_swarm(agents, attraction=0.01, repulsion=0.05, bounds=10):
    new_agents = []
    for i, (x, y) in enumerate(agents):
        dx = dy = 0.0
        for j, (x2, y2) in enumerate(agents):
            if i == j:
                continue
            dist = math.hypot(x2 - x, y2 - y) + 1e-5
            dx += (x2 - x) / dist * attraction
            dy += (y2 - y) / dist * attraction
            if dist < 1.0:
                dx -= (x2 - x) / dist * repulsion
                dy -= (y2 - y) / dist * repulsion
        x = max(0, min(bounds, x + dx))
        y = max(0, min(bounds, y + dy))
        new_agents.append([x, y])
    return new_agents


def main() -> None:
    import random
    agents = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(15)]
    for _ in range(10):
        agents = step_swarm(agents)
    print('Final positions (first 5):', agents[:5])


if __name__ == '__main__':
    main()
