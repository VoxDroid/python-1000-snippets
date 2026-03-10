# sample1.py
# number collection iterator (from README)

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_iterator(self):
        return NumberIterator(self.numbers)

if __name__ == '__main__':
    collection = NumberCollection([1, 2, 3])
    for num in collection.get_iterator():
        print(num, end=" ")
    print()
