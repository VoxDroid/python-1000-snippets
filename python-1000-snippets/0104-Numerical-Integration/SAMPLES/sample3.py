# sample3.py
# Vectorized integration using NumPy

import numpy as np

def trapezoidal_vec(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (y[0]/2 + y[-1]/2 + y[1:-1].sum())

if __name__ == '__main__':
    f = lambda x: x**2
    print('np trap', trapezoidal_vec(f, 0, 1, 100000))
