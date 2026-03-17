# 0361-Metaclass-Customization Cheatsheet

- A metaclass is a class of a class; default is `type`.
- Override `__new__` or `__init__` to customize class creation.
- Use metaclasses to enforce naming, register subclasses, or modify attributes.
- Keep metaclasses small; avoid surprising behavior.
