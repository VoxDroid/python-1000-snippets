# sample3.py
# Output stream stats to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0515_stream_stats.txt')


def compute_stats(values):
    return {
        'count': len(values),
        'sum': sum(values),
        'avg': sum(values) / len(values) if values else 0,
    }


if __name__ == '__main__':
    streamed = [i for i in range(1, 11)]
    stats = compute_stats(streamed)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for k, v in stats.items():
            f.write(f'{k}: {v}\n')
    print('Stat output written to', OUTPUT_PATH)
