# sample1.py
# Print value of HOME or default

import os

if __name__ == '__main__':
    val = os.getenv('HOME', '/home/unknown')
    print('HOME =', val)
