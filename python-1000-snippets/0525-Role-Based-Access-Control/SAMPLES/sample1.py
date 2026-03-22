# sample1.py
# Role-based permission checks.

roles = {
    'admin': {'read', 'write', 'delete'},
    'user': {'read'},
    'guest': {'read'}
}


def has_access(role, action):
    return action in roles.get(role, set())


if __name__ == '__main__':
    tests = [('admin', 'write'), ('user', 'delete'), ('guest', 'read')]
    for role, action in tests:
        print(f'{role} can {action}:', has_access(role, action))
