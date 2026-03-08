# sample3.py
# NumPy vectorized statistics

import numpy as np

if __name__ == '__main__':
    data = np.array([1,2,3,4,5])
    print('np mean', np.mean(data))
    print('np median', np.median(data))
    print('np var', np.var(data))
    print('np std', np.std(data))
