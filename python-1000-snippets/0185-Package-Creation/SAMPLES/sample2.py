# sample2.py
# import add directly from package

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from my_package.utilities import add

if __name__ == '__main__':
    print(add(5, 7))
