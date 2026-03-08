# sample2.py
# static method used for validation

class Validator:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

if __name__ == '__main__':
    print('4 even?', Validator.is_even(4))
    print('5 even?', Validator.is_even(5))
