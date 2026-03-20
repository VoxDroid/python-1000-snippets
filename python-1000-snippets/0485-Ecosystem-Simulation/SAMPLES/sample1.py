# sample1.py
# Predator-prey model (Lotka-Volterra) with simple loop.


def simulate(prey=100, predator=10, steps=20):
    history = []
    for _ in range(steps):
        prey = prey * (1 + 0.1 - 0.01 * predator)
        predator = predator * (1 - 0.05 + 0.005 * prey)
        history.append((prey, predator))
    return history


def main() -> None:
    hist = simulate()
    print('Start: prey=100 predator=10')
    print('End:', tuple(round(v, 2) for v in hist[-1]))


if __name__ == '__main__':
    main()
