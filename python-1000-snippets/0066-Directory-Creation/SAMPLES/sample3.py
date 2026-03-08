# sample3.py
# Prompt user for directory name and create it if absent

import os

if __name__ == '__main__':
    name = input('Directory name: ')
    if not os.path.exists(name):
        os.mkdir(name)
        print('created', name)
    else:
        print(name, 'already exists')
