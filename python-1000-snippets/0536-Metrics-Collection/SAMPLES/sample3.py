# sample3.py
# Save collected metrics to a temp file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0536_metrics.txt'))


def save_metrics(metrics):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(metrics) + '\n')


if __name__ == '__main__':
    metrics = {'requests': 500, 'errors': 15}
    save_metrics(metrics)
    print('Saved metrics to', OUTPUT_PATH)
