# sample1.py
# Create a single directory if it does not exist

import os

if __name__ == '__main__':
    dirname = 'folder1'
    try:
        os.mkdir(dirname)
        print('created', dirname)
    except FileExistsError:
        print(dirname, 'already exists')
