# String Formatting Cheatsheet

## f-strings
```python
name = "Bob"
age = 30
print(f"{name} is {age} years old")
```

## format()
```python
"{0} + {1} = {2}".format(1, 2, 3)
"{name} is {age}".format(name="Bob", age=30)
```

## % operator
```python
"%s is %d" % ("Bob", 30)
```

## Numeric formatting
```python
pi = 3.14159
print(f"{pi:.2f}")          # two decimals
print("{:.3f}".format(pi))
```

## Alignment and width
```python
print(f"{"left":<10}")  # left align
print(f"{"right":>10}") # right align
```

## Tips
- Use f-strings for expressions: `f"{2+2}"`.
- For older versions of Python (<3.6), use `format()`.
- Avoid mixing different styles in one project.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

