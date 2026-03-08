# sample3.py
# Read email addresses from stdin and indicate validity

import re
import sys

def is_valid(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

if __name__ == '__main__':
    for line in sys.stdin:
        email = line.strip()
        if email:
            print(email, 'valid' if is_valid(email) else 'invalid')
