# sample3.py
# demonstrate import alias and module reload

import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import utils as u

if __name__ == '__main__':
    print(u.greet('Carol'))
    # reload for demonstration
    importlib.reload(u)
