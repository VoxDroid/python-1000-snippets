# sample1.py
# Trapezoidal rule implementation

def trapezoidal_rule(f, a, b, n):
    h = (b - b) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# correct the bug above: using (b-a)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

if __name__ == '__main__':
    def f(x):
        return x**2
    print('integral', trapezoidal_rule(f, 0, 1, 100))
