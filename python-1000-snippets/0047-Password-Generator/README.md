# Password Generator

## Description
This snippet generates a random password of a specified length using letters, digits, and special characters with the `random` module.

## Code
```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated password:", password)
```

## Output
```
Enter password length: 12
Generated password: kX#9mP$2nJ@5
```
*(Output varies each run)*

## Explanation
- **Password Logic**: Uses `string.ascii_letters`, `string.digits`, and `string.punctuation` for a diverse character set.
- **random.choice()**: Selects a random character from the set for each position.
- **List Comprehension**: Builds the password by joining random characters.
- **Use Case**: Password generation is used in security applications or user account setup.
- **Best Practice**: Use `secrets` module for cryptographic security; validate length input.