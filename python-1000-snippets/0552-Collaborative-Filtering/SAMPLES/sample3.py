# sample3.py
# Save collaborative filtering correlation to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0552_collab_filtering.txt'))


def save_corr(corr):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(corr) + '\n')


if __name__ == '__main__':
    correlation = {0:{1:0.76,2:0.34}, 1:{0:0.76,2:0.12}, 2:{0:0.34,1:0.12}}
    save_corr(correlation)
    print('Saved correlation to', OUTPUT)
    with open(OUTPUT) as f:
        print(f.read().strip())
