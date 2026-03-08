# sample2.py
# use lambdas with map/filter/sorted

if __name__ == '__main__':
    numbers = list(range(10))
    evens = list(filter(lambda x: x%2==0, numbers))
    print('evens:', evens)
    doubled = list(map(lambda x: x*2, numbers))
    print('doubled:', doubled)
    pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
    print('sorted by letter:', sorted(pairs, key=lambda t: t[1]))
