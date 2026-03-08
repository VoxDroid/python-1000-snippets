# sample3.py
# Use itertools.accumulate to generate Fibonacci-like sequence.

import itertools

def main():
    # generate first 10 Fibonacci numbers
    fib = itertools.accumulate(itertools.repeat(1), lambda x, y: x + y)
    # the accumulate sequence starts at 1,1,2,3,... so prepend 0
    seq = [0] + list(itertools.islice(fib, 9))
    print(seq)

if __name__ == '__main__':
    main()

