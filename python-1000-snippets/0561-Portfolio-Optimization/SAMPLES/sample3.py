# sample3.py
# Save portfolio optimization results to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0561_portfolio.txt'))


def save_portfolio(result):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(result) + '\n')
    return OUTPUT


if __name__ == '__main__':
    result = {'optimal_weight': 0.5, 'variance': 0.19}
    path = save_portfolio(result)
    print('Saved to', path)
    with open(path) as f:
        print(f.read().strip())
