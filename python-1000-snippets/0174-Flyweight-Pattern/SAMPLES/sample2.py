# sample2.py
# text character flyweight with shared font

class Char:
    def __init__(self, char, font):
        self.char = char
        self.font = font
    def display(self, size):
        return f"{self.char} in {self.font} size {size}"

class CharFactory:
    _chars = {}
    @classmethod
    def get_char(cls, char, font):
        key = (char, font)
        if key not in cls._chars:
            cls._chars[key] = Char(char, font)
        return cls._chars[key]

if __name__ == '__main__':
    a1 = CharFactory.get_char('a', 'Arial')
    a2 = CharFactory.get_char('a', 'Arial')
    b = CharFactory.get_char('b', 'Arial')
    print(a1 is a2)
    print(a1.display(12))
    print(b.display(14))
