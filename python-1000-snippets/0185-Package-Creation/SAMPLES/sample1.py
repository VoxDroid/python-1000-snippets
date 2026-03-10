# sample1.py
# import add from my_package utilities

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from my_package import utilities

if __name__ == '__main__':
    print(utilities.add(2, 3))
