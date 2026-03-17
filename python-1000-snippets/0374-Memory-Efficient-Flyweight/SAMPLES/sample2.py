# sample2.py
# Use flyweights to represent characters in a document

class CharacterFlyweight:
    def __init__(self, char):
        self.char = char

    def render(self, font):
        return f"{self.char} in {font}"


class CharacterFactory:
    def __init__(self):
        self._flyweights = {}

    def get_character(self, char):
        if char not in self._flyweights:
            self._flyweights[char] = CharacterFlyweight(char)
        return self._flyweights[char]


def main():
    factory = CharacterFactory()
    text = "hello"
    for ch in text:
        f = factory.get_character(ch)
        print(f.render("Arial"))


if __name__ == "__main__":
    main()
