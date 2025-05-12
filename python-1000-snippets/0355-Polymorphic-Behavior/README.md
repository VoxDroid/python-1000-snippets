# Polymorphic Behavior

## Description
This snippet demonstrates polymorphism with a common interface.

## Code
```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

## Output
```
Woof
Meow
```

## Explanation
- **Polymorphic Behavior**: Calls the same method on different classes.
- **Logic**: Defines `speak` in each class, called uniformly in a loop.
- **Complexity**: O(n) for n objects.
- **Use Case**: Used in object-oriented systems for flexible behavior.
- **Best Practice**: Define clear interfaces; use ABCs; ensure method consistency.