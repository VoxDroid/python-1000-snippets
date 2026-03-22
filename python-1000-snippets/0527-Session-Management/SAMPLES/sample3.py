# sample3.py
# Save active session list to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0527_sessions.txt')


def write_sessions(sessions):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for u, v in sessions.items():
            f.write(f'{u}: {v}\n')


if __name__ == '__main__':
    sessions = {'user1': {'auth': True}, 'user2': {'auth': False}}
    write_sessions(sessions)
    print('Sessions written to', OUTPUT_PATH)
