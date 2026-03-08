# sample3.py
# Use NumPy for efficient multiplication (requires numpy installed)

import numpy as np

if __name__ == '__main__':
    A = np.array([[1,2],[3,4]])
    B = np.array([[5,6],[7,8]])
    print('numpy product')
    print(np.dot(A, B))
