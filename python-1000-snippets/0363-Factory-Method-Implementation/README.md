# Factory Method Implementation

## Description
This snippet demonstrates the factory method pattern.

## Code
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        return None

dog = AnimalFactory.create_animal("dog")
print(dog.speak())
```

## Output
```
Woof
```

## Explanation
- **Factory Method Implementation**: Creates objects based on input type.
- **Logic**: Factory method returns a `Dog` instance for "dog" input.
- **Complexity**: O(1) per creation.
- **Use Case**: Used for object creation with varying types.
- **Best Practice**: Extend for new types; handle invalid inputs; document factory logic.