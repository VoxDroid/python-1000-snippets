# sample2.py
# generator expression for squares

if __name__ == '__main__':
    squares = (x*x for x in range(5))
    for s in squares:
        print('square', s)
    # generator is now exhausted
    print('converted to list', list(x*x for x in range(5)))
