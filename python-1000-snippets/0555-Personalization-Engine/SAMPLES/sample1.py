# sample1.py
# Simple personalization lookup from user profile dictionary.

USER_PROFILES = {1: 'action', 2: 'comedy'}


def personalize(user_id):
    return USER_PROFILES.get(user_id, 'default')


if __name__ == '__main__':
    print('Preference for user 1:', personalize(1))
