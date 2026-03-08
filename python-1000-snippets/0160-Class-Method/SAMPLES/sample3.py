# sample3.py
# class method modifying class-wide state

class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

if __name__ == '__main__':
    print('count', Counter.increment())
    print('count', Counter.increment())
    c = Counter()
    print('count via instance', c.increment())
