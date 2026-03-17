# 0382-Object-Cloning-Prototype Cheatsheet

- Use `copy.copy` for shallow copies and `copy.deepcopy` for deep cloning.
- Provide a `clone()` method on prototypes to encapsulate copying logic.
- Be cautious with mutable nested structures; deep copy can be expensive.
- Use prototypes when creating new objects from a template is cheaper than constructing from scratch.
