# sample1.py
# Simulate temperature readings over a small time series.

import random


def generate_temperatures(count=12, base=20.0):
    temps = []
    for i in range(count):
        trend = 0.5 * i / count
        noise = random.uniform(-1.0, 1.0)
        temps.append(base + trend + noise)
    return temps


def main() -> None:
    temps = generate_temperatures()
    print('First 5 temperatures:', [round(t, 2) for t in temps[:5]])
    print('Min/Max:', round(min(temps), 2), round(max(temps), 2))


if __name__ == '__main__':
    main()
