# sample3.py
# Generate multiple passwords and check uniqueness

import random
import string

def gen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    n = int(input('How many passwords? '))
    length = int(input('Length each: '))
    pwds = [gen(length) for _ in range(n)]
    print('Generated', n, 'passwords')
    print('Any duplicates?', len(set(pwds)) != len(pwds))
    for p in pwds:
        print(p)
