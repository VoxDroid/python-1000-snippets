# sample1.py
# simple lambdas for arithmetic operations

if __name__ == '__main__':
    square = lambda x: x*x
    add = lambda x, y: x+y
    print('square of 6 =', square(6))
    print('sum of 7 and 8 =', add(7, 8))
    # inline lambda call
    print('triple of 5 =', (lambda x: x*3)(5))
