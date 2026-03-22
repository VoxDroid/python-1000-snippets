# sample3.py
# Persist credit score output to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0560_credit.txt'))


def save_credit(status):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(status) + '\n')
    return OUTPUT


if __name__ == '__main__':
    status = {'score': 750, 'category': 'excellent'}
    path = save_credit(status)
    print('Saved to', path)
    with open(path) as f:
        print(f.read().strip())
