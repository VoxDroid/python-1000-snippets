# sample2.py
# Create nested directories using makedirs

import os

if __name__ == '__main__':
    path = 'parent/child/grandchild'
    os.makedirs(path, exist_ok=True)
    print('ensured path', path)
