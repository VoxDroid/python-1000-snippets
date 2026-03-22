# sample3.py
# Write content-based recommendation output into temp.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0553_content_based.txt'))


def save_scores(scores):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(scores) + '\n')
    return OUTPUT


if __name__ == '__main__':
    users_pref = [1, 0]
    items = [[1, 0], [0, 1], [1, 1]]
    scores = [sum(i * p for i, p in zip(item, users_pref)) for item in items]
    path = save_scores(scores)
    print('Saved scores at', path)
    print(scores)
