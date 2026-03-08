# sample2.py
# Polar form and division using cmath

import cmath

if __name__ == '__main__':
    z = 1 + 1j
    r, phi = cmath.polar(z)
    print('polar', r, phi)
    print('back to rect', cmath.rect(r, phi))
    a = 2+3j
    b = 1-1j
    print('division', a / b)
