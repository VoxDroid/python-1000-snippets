# Polymorphism

## Description
This snippet demonstrates polymorphism by defining classes with a common method called differently.

## Code
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

## Output
```
Woof!
Meow!
```

## Explanation
- **Polymorphism**: Different classes (`Dog`, `Cat`) implement the same method (`speak`) with unique behavior.
- **Logic**: Iterates over a list of objects, calling `speak` without knowing the exact type.
- **Complexity**: O(n) for n objects.
- **Use Case**: Used for flexible code handling multiple types with a common interface.
- **Best Practice**: Ensure consistent method signatures; use interfaces or abstract classes for clarity.