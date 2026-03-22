# sample2.py
# Evaluate request and return auth result.


def authorize(user_role, action):
    if user_role == 'admin':
        return True
    if action == 'read' and user_role in ('user', 'guest'):
        return True
    return False


if __name__ == '__main__':
    print('Authorize admin-delete:', authorize('admin', 'delete'))
    print('Authorize user-write:', authorize('user', 'write'))
