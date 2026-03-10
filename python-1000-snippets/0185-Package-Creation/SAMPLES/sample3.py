# sample3.py
# modify package by adding new function and reload

import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import my_package.utilities as util

if __name__ == '__main__':
    print(util.add(1,2))
    # dynamically add function
    def mul(a,b):
        return a*b
    util.mul = mul
    importlib.reload(util)
    print(util.mul(3,4))
