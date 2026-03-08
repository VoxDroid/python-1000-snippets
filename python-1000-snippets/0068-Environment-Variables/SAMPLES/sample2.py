# sample2.py
# Set an environment variable temporarily then read it

import os

if __name__ == '__main__':
    os.environ['MYVAR'] = '123'
    print('MYVAR set to:', os.getenv('MYVAR'))
