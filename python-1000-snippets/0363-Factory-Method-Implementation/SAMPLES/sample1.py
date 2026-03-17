# sample1.py
# Simple factory method implementation

class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        if animal_type == "cat":
            return Cat()
        raise ValueError(f"Unknown animal type: {animal_type}")


def main():
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")
    print(dog.speak())
    print(cat.speak())


if __name__ == "__main__":
    main()
