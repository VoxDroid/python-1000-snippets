# sample3.py
# Log recommendation results to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0551_recommendation.txt'))


def save_recommendations(recs):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(recs) + '\n')
    return OUTPUT


if __name__ == '__main__':
    recs = {'user0': [2], 'user1': [], 'user2': []}
    path = save_recommendations(recs)
    print('Saved to', path)
    print(recs)
