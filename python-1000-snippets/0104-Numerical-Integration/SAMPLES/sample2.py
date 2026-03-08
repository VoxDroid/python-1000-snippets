# sample2.py
# Simpson's rule for better accuracy

def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError('n must be even')
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        factor = 4 if i % 2 else 2
        s += factor * f(a + i * h)
    return s * h / 3

if __name__ == '__main__':
    f = lambda x: x**2
    print('simpson', simpson_rule(f, 0, 1, 100))
