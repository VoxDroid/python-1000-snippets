# sample3.py
# Use NumPy's polyval and polyder

import numpy as np

if __name__ == '__main__':
    coeffs = [1, -4, 3]
    x = 5
    print('numpy polyval', np.polyval(list(reversed(coeffs)), x))
    print('numpy derivative coeffs', np.polyder(list(reversed(coeffs))))
    print('numpy polyval derivative', np.polyval(np.polyder(list(reversed(coeffs))), x))
