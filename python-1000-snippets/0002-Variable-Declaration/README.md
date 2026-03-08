# Variable Declaration

## Description
This snippet illustrates how to declare and initialize variables in Python. Variables are used to store data that can be referenced and manipulated throughout a program.

## Code
```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## Output
```
(No output, as this code only declares variables)
```

## Explanation
- **Variables**: In Python, variables are created by assigning a value using the `=` operator. No explicit type declaration is needed due to Python's dynamic typing.
- **Types**:
  - `name` is a string (`str`), storing text data.
  - `age` is an integer (`int`), storing whole numbers.
  - `height` is a float (`float`), storing decimal numbers.
  - `is_student` is a boolean (`bool`), storing `True` or `False`.
- **Naming Rules**: Variable names must start with a letter or underscore, can include numbers, and are case-sensitive (e.g., `Name` and `name` are different). Avoid Python keywords.
- **Dynamic Typing**: Python automatically determines the variable's type based on the assigned value, which allows reassigning different types to the same name.
- **Use Case**: Variables are fundamental for storing and manipulating data, such as user information or calculation results. They form the basis of functions, data structures, and control flow.

## Additional Files
- `CHEATSHEET.md` contains quick tips and examples for declaring and using variables.
- `SAMPLES/` directory includes three runnable programs demonstrating variable usage:
  1. `sample1.py` – declare, modify, and print variables.
  2. `sample2.py` – read input into variables and calculate a result.
  3. `sample3.py` – illustrate dynamic typing by reassigning different types.

Run these samples in a `.venv` to verify they execute correctly.