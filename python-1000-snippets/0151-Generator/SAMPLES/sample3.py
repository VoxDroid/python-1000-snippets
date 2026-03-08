# sample3.py
# infinite generator with itertools

import itertools

def naturals():
    i = 1
    while True:
        yield i
        i += 1

if __name__ == '__main__':
    gen = naturals()
    for _ in range(5):
        print(next(gen))
    print('first five from itertools.count:')
    for n in itertools.count(1):
        print(n)
        if n >= 5:
            break
