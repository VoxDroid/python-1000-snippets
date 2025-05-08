# Palindrome Check

## Description
This snippet checks if a given string is a palindrome, meaning it reads the same forward and backward (ignoring case and non-alphanumeric characters).

## Code
```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

text = input("Enter a string: ")
print(f"'{text}' is {'a palindrome' if is_palindrome(text) else 'not a palindrome'}.")
```

## Output
```
Enter a string: Racecar
'Racecar' is a palindrome.
```
*(If input is `hello`):*
```
Enter a string: hello
'hello' is not a palindrome.
```

## Explanation
- **Palindrome Logic**: Compares the string with its reverse after cleaning (lowercase, remove non-alphanumeric characters).
- **Function**: `is_palindrome(s)` processes the string and checks if it equals its reverse (`s[::-1]`).
- **Cleaning**: Uses `isalnum()` to keep only letters and numbers, and `lower()` for case-insensitive comparison.
- **Use Case**: Palindrome checks are used in text processing, games, or coding challenges.
- **Best Practice**: Handle empty strings or special cases explicitly if required.