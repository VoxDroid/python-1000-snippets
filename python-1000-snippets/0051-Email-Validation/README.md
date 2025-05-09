# Email Validation

## Description
This snippet validates an email address using a regular expression to check if it follows a standard email format (e.g., `user@domain.com`).

## Code
```python
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")
print(f"'{email}' is {'valid' if is_valid_email(email) else 'invalid'}.")
```

## Output
```
Enter an email address: user@example.com
'user@example.com' is valid.
```
*(If input is `invalid.email`):*
```
Enter an email address: invalid.email
'invalid.email' is invalid.
```

## Explanation
- **Regular Expression**: The pattern `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` checks for:
  - Username: Letters, numbers, and some symbols (e.g., `.`, `_`).
  - `@` symbol.
  - Domain: Letters, numbers, hyphens, and dots.
  - Top-level domain: At least 2 letters (e.g., `.com`).
- **re.match()**: Checks if the entire string matches the pattern.
- **Use Case**: Email validation is used in forms, user registration, or data cleaning.
- **Limitations**: This checks format, not if the email exists. Advanced validation may require DNS checks.
- **Best Practice**: Use robust regex patterns and consider libraries like `email-validator` for production.