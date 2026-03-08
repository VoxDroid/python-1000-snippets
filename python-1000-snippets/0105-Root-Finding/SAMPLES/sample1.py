# sample1.py
# Bisection to find square root of 2

def bisection(f,a,b,tol=1e-6):
    if f(a)*f(b) >= 0:
        return None
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2

if __name__ == '__main__':
    f = lambda x: x**2 - 2
    print('root', bisection(f, 0, 2))
