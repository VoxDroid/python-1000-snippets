# sample3.py
# Use NumPy's polyfit for regression

import numpy as np

if __name__ == '__main__':
    x = np.array([1,2,3,4])
    y = np.array([2,4,5,4])
    m, b = np.polyfit(x, y, 1)
    print('numpy m,b', m, b)
    # compute R2
    ypred = m*x + b
    ss_res = np.sum((y-ypred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    print('r2', 1 - ss_res/ss_tot)
