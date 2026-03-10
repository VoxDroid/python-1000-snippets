# sample3.py
# numeric flyweight using Python's small int cache

# Python automatically reuses small ints, but we can illustrate manually

class NumberFactory:
    _cache = {}
    @classmethod
    def get_number(cls, value):
        if value not in cls._cache:
            cls._cache[value] = value
        return cls._cache[value]

if __name__ == '__main__':
    n1 = NumberFactory.get_number(100)
    n2 = NumberFactory.get_number(100)
    print('same object?', n1 is n2)
    # should print True even for larger ints because cache holds one instance
    print('cached value', n1)
