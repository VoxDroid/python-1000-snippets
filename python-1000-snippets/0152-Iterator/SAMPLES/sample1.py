# sample1.py
# custom StepRange iterator (matching README)

class StepRange:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

if __name__ == '__main__':
    for num in StepRange(1, 6, 2):
        print(num, end=' ')
    print()
