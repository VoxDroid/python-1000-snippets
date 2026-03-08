# sample3.py
# Bisection with cosine function, handle tolerance

def bisection(f,a,b,tol=1e-8):
    if f(a)*f(b) >= 0:
        return None
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b=c
        else:
            a=c
    return (a+b)/2

if __name__ == '__main__':
    import math
    # avoid endpoint exactly zero by using slightly larger b
    root = bisection(math.cos, 0, 2, tol=1e-10)
    print('root cos approx', root)
