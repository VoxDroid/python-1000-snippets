# sample3.py
# returning lambdas (closures)

def make_multiplier(n):
    return lambda x: x * n

if __name__ == '__main__':
    times3 = make_multiplier(3)
    times5 = make_multiplier(5)
    print('5 * 3 =', times3(5))
    print('4 * 5 =', times5(4))
