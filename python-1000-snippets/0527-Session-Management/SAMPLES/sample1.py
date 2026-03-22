# sample1.py
# Basic session dictionary management.


def add_session(sessions, user_id, data):
    sessions[user_id] = data


def get_session(sessions, user_id):
    return sessions.get(user_id)


if __name__ == '__main__':
    sessions = {}
    add_session(sessions, 'user1', {'auth': True})
    print('Session for user1:', get_session(sessions, 'user1'))
