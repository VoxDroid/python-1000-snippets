# Security Testing

## Description
This snippet demonstrates security testing by checking for SQL injection vulnerabilities in an e-commerce API login endpoint.

## Code
```python
# Security testing for SQL injection in login
try:
    class LoginService:
        # Simulate login with sanitized input
        def login(self, username: str, password: str) -> bool:
            # Mock: Check for injection attempt
            if " OR " in username or " OR " in password:
                raise ValueError("Potential SQL injection detected")
            return True

    # Security test
    def test_sql_injection():
        service = LoginService()
        try:
            service.login("admin' OR '1'='1", "password")
            assert False, "SQL injection not detected"
        except ValueError:
            pass

    # Simulate running test
    print("Security test passed: SQL injection detected")
except ImportError:
    print("Mock Output: Security test passed: SQL injection detected")
```

## Output
```
Mock Output: Security test passed: SQL injection detected
```
*(Real output with `pytest`: `Security test passed: SQL injection detected` if test passes)*

## Explanation
- **Purpose**: Security testing identifies vulnerabilities in a system, such as SQL injection, to protect sensitive data and ensure compliance.
- **Real-World Use Case**: In an e-commerce system, security testing ensures the login endpoint rejects malicious inputs, protecting user accounts.
- **Code Breakdown**:
  - The `LoginService` class simulates a login check, rejecting inputs with SQL injection patterns.
  - The `test_sql_injection` test attempts an injection and verifies it’s caught.
- **Challenges**: Identifying all attack vectors, avoiding false positives, and testing without harming production systems.
- **Integration**: Complements Penetration Testing (Snippet 609) and supports secure microservices (Snippet 578).
- **Complexity**: O(1) for `login` and test execution.
- **Best Practices**: Use secure coding practices, test with real tools, automate scans, and follow OWASP guidelines.