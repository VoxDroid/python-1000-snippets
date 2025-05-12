# Abstract Base Classes

## Description
This snippet demonstrates abstract base classes using `abc`.

## Code
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak())
```

## Output
```
Woof
```

## Explanation
- **Abstract Base Classes**: Enforces a contract for subclasses.
- **Logic**: Defines an abstract `speak` method, implemented by `Dog`.
- **Complexity**: O(1) for method calls.
- **Use Case**: Used to define interfaces in object-oriented design.
- **Best Practice**: Use `abc` module; ensure all abstract methods are implemented; document interfaces.