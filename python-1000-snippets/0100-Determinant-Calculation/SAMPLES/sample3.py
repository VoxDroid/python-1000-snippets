# sample3.py
# Use NumPy's linear algebra to compute determinant

import numpy as np

if __name__ == '__main__':
    a = np.array([[1,2],[3,4]])
    print('numpy det', np.linalg.det(a))
    b = np.array([[1,2,3],[0,1,4],[5,6,0]])
    print('numpy det2', np.linalg.det(b))
