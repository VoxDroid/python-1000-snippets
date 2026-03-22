# sample3.py
# Write frequent items analysis into temp.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0563_market_basket.txt'))


def save_frequent(items):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(items) + '\n')
    return OUTPUT


if __name__ == '__main__':
    items = ['milk', 'bread']
    path = save_frequent(items)
    print('Saved to', path)
    with open(path) as f:
        print(f.read().strip())
