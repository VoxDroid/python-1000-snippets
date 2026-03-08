# sample1.py
# simple duck-typed polymorphism (matches README)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

if __name__ == '__main__':
    for animal in (Dog(), Cat()):
        print(animal.speak())
