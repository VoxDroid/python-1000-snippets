# sample3.py
# Persist user personalization output to temp.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0555_personalization.txt'))


def save_personalization(user_id, recs):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'a') as f:
        f.write(f'user:{user_id} recs:{recs}\n')
    return OUTPUT


if __name__ == '__main__':
    out = save_personalization(1, ['movie1', 'movie2'])
    print('Saved to', out)
    with open(out) as f:
        print('Current file lines:', f.read().strip())
