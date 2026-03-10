# sample1.py
# import utils module in same folder

import sys, os
# add parent directory so utils.py can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import utils

if __name__ == '__main__':
    print(utils.greet("Alice"))

