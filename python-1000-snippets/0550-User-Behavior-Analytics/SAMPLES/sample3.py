# sample3.py
# Write final user metric to temp file.

import os

OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0550_user_behavior.txt'))


def save_behavior_summary(summary):
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(str(summary) + '\n')
    return OUTPUT


if __name__ == '__main__':
    summary = {'daily_users': 2, 'click_rate': 0.6}
    path = save_behavior_summary(summary)
    print('Saved summary to', path)
    with open(path) as f:
        print(f.read().strip())
