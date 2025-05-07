# String Formatting

## Description
This snippet explores different methods of string formatting in Python, including f-strings, `.format()`, and `%` operator, to create dynamic strings.

## Code
```python
name = "Alice"
age = 25
f_string = f"My name is {name} and I'm {age}."
format_string = "My name is {} and I'm {}.".format(name, age)
percent_string = "My name is %s and I'm %d." % (name, age)
print(f_string)
print(format_string)
print(percent_string)
```

## Output
```
My name is Alice and I'm 25.
My name is Alice and I'm 25.
My name is Alice and I'm 25.
```

## Explanation
- **f-strings**: Introduced in Python 3.6, `f"..."` embeds variables directly in strings (e.g., `{name}`).
- **`.format()`**: Uses placeholders `{}` filled by `.format()` arguments in order.
- ** `%` Operator**: Older method using `%s` for strings and `%d` for integers, with values provided in a tuple.
- **Use Case**: String formatting is used for user messages, logging, or generating dynamic content.
- **Best Practice**: Prefer f-strings for readability and performance; avoid `%` operator in modern Python.