# sample3.py
# Write ABAC policy decisions to temp log file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0526_abac_log.txt')


def policy_decision(user, resource):
    decision = (user.get('department') == resource.get('department') and
                user.get('clearance', 0) >= resource.get('required_clearance', 0))
    return decision


if __name__ == '__main__':
    user = {'department': 'IT', 'clearance': 3}
    resource = {'department': 'IT', 'required_clearance': 4}
    decision = policy_decision(user, resource)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(f'user: {user}; resource: {resource}; decision: {decision}\n')

    print('ABAC decision written to', OUTPUT_PATH)
