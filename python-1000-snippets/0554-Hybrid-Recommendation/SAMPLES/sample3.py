# sample3.py
# Save hybrid recommendation scores to temp.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0554_hybrid.txt'))


def save_hybrid(scores):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(scores) + '\n')
    return OUTPUT


if __name__ == '__main__':
    scores = [0.7, 0.55, 0.4]
    print('Saved to', save_hybrid(scores))
