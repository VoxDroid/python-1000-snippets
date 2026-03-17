# sample1.py
# Basic polymorphism using a shared method name

class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())


if __name__ == "__main__":
    main()
