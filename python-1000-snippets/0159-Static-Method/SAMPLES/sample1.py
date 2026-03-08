# sample1.py
# basic static method for addition

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    print('Sum:', MathUtils.add(5, 3))
    m = MathUtils()
    print('Sum via instance:', m.add(2,4))
