# sample2.py
# Demonstrate failure when sign does not change

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
    f = lambda x: x**2 + 1
    print('no root', bisection(f, -1, 1))
