# User Input Cheatsheet

Quick tips for reading input from users in Python.

## Basic Usage
```python
name = input("Enter your name: ")
age = input("Enter your age: ")  # returns string
```

## Conversion
```python
age = int(input("Age: "))
x = float(input("Number: "))
```

## Validation
```python
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid, try again.")
```

## Hidden Input
```python
import getpass
password = getpass.getpass("Password: ")
```

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

