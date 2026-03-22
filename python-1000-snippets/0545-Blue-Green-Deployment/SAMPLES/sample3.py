# sample3.py
# Save deployment transition to file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0545_blue_green.txt'))


def save_transition(active):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(f'active={active}\n')


if __name__ == '__main__':
    save_transition('green')
    print('Saved transition to', OUTPUT_PATH)
