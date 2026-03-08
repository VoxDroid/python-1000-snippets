# sample2.py
# Validate a list of predefined email addresses

import re

def is_valid(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

if __name__ == '__main__':
    emails = ['user@example.com', 'invalid.email', 'bob@site', 'alice@domain.co']
    valids = [e for e in emails if is_valid(e)]
    print('valid addresses:', valids)
