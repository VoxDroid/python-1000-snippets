# sample2.py
# import specific name from module

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import greet

if __name__ == '__main__':
    print(greet('Bob'))

