# sample3.py
# Compute complex exponentials and Euler's formula

import cmath

if __name__ == '__main__':
    for k in range(4):
        z = cmath.exp(1j * k * cmath.pi/2)
        print(f'exp(i*{k}*pi/2) =', z)
    z = 5*cmath.exp(1j*cmath.pi/4)
    print('magnitude-phase', abs(z), cmath.phase(z))
