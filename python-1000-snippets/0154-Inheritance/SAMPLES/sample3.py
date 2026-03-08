# sample3.py
# polymorphism: list of animals

class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return 'woof'

class Cat(Animal):
    def speak(self):
        return 'meow'

if __name__ == '__main__':
    for a in (Dog(), Cat()):
        print(a.speak())
