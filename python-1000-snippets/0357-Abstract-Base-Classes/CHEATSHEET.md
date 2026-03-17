# 0357-Abstract-Base-Classes Cheatsheet

- Use `ABC` and `@abstractmethod` to define required methods.
- Instantiating a class with unimplemented abstract methods raises `TypeError`.
- Use `abc.ABCMeta.register()` to register virtual subclasses.
- Abstract base classes define interfaces, not implementation.
