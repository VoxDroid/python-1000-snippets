# sample2.py
# Generate a CSV time series for prey/predator populations (no external libraries).

import csv
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/ecosystem.csv')


def generate_series(steps=30):
    prey, predator = 100.0, 10.0
    out = []
    for t in range(steps):
        out.append((t, prey, predator))
        prey = prey * (1 + 0.1 - 0.01 * predator)
        predator = predator * (1 - 0.05 + 0.005 * prey)
    return out


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    series = generate_series()
    with open(OUTPUT_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'prey', 'predator'])
        for row in series:
            writer.writerow([row[0], round(row[1], 3), round(row[2], 3)])
    print('Saved', OUTPUT_PATH)


if __name__ == '__main__':
    main()
