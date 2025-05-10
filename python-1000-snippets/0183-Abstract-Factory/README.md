# Abstract Factory

## Description
This snippet implements the Abstract Factory pattern to create families of related objects.

## Code
```python
class Button:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Windows Button"

class MacButton(Button):
    def render(self):
        return "Mac Button"

class Factory:
    def create_button(self):
        pass

class WindowsFactory(Factory):
    def create_button(self):
        return WindowsButton()

class MacFactory(Factory):
    def create_button(self):
        return MacButton()

factory = WindowsFactory()
button = factory.create_button()
print(button.render())
```

## Output
```
Windows Button
```

## Explanation
- **Abstract Factory**: `Factory` defines an interface; `WindowsFactory` and `MacFactory` create platform-specific objects.
- **Logic**: `create_button` returns a `Button` subclass based on the factory.
- **Complexity**: O(1) for object creation.
- **Use Case**: Used for platform-specific UI components or configurations.
- **Best Practice**: Ensure factory methods are consistent; avoid overcomplicating families.