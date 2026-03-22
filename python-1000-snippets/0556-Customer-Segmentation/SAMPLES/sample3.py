# sample3.py
# Save segmentation results to a temp file for downstream tasks.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0556_segmentation.txt'))


def save_segments(segments):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(segments) + '\n')
    return OUTPUT


if __name__ == '__main__':
    segments = {'high_value': [1, 3], 'low_value': [2]}
    path = save_segments(segments)
    print('Saved to', path)
    with open(path) as f:
        print(f.read().strip())
