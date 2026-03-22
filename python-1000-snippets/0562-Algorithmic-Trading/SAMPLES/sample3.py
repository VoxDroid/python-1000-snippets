# sample3.py
# Write trading signals to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0562_algo_trading.txt'))


def save_signals(signals):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        for s in signals:
            f.write(str(s) + '\n')
    return OUTPUT


if __name__ == '__main__':
    signals = [{'index':3,'price':103,'signal':True}, {'index':4,'price':104,'signal':True}]
    path = save_signals(signals)
    print('Saved signals to', path)
    with open(path) as f:
        print(f.read().strip())
