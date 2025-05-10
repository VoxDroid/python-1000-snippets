# Property Decorator

## Description
This snippet uses the `@property` decorator to create a getter and setter for a class attribute.

## Code
```python
class Employee:
    def __init__(self, name, salary):
        self._salary = salary
        self.name = name
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee("Bob", 50000)
print("Salary:", emp.salary)
emp.salary = 60000
print("Updated Salary:", emp.salary)
```

## Output
```
Salary: 50000
Updated Salary: 60000
```

## Explanation
- **Property Decorator**: Makes `salary` a property, allowing getter (`@property`) and setter (`@salary.setter`) methods.
- **Logic**: Validates `salary` in the setter to prevent negative values.
- **Complexity**: O(1) for get/set operations.
- **Use Case**: Used to control attribute access and validation.
- **Best Practice**: Use `_` for protected attributes; document validation rules.