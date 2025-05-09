# Environment Variables

## Description
This snippet demonstrates accessing environment variables using the `os` module, which store system or user-defined settings.

## Code
```python
import os

variable = "HOME"
value = os.getenv(variable, "Not found")
print(f"Environment variable {variable}: {value}")
```

## Output
*(On a Unix-like system):*
```
Environment variable HOME: /home/user
```
*(If variable doesn't exist):*
```
Environment variable HOME: Not found
```

## Explanation
- **os.getenv()**: Retrieves the value of an environment variable, with an optional default if not found.
- **Use Case**: Environment variables are used for configuration, like paths, API keys, or system settings.
- **Common Variables**: `HOME`, `PATH`, `USER` on Unix; `USERPROFILE` on Windows.
- **Best Practice**: Use defaults for missing variables and avoid exposing sensitive data.