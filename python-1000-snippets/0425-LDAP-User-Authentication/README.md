# LDAP User Authentication

## Description
This snippet demonstrates LDAP authentication using `ldap3`.

## Code
```python
# Note: Requires `ldap3`. Install with `pip install ldap3`
try:
    from ldap3 import Server, Connection
    server = Server("ldap://localhost")
    conn = Connection(server, user="cn=user,dc=example,dc=com", password="pass")
    conn.bind()
    print("Authenticated" if conn.bound else "Failed")
    conn.unbind()
except ImportError:
    print("Mock Output: Authenticated")
```

## Output
```
Mock Output: Authenticated
```
*(Real output with `ldap3` and LDAP server: `Authenticated` or `Failed`)*

## Explanation
- **LDAP User Authentication**: Authenticates a user against an LDAP server.
- **Logic**: Connects and binds to LDAP with credentials.
- **Complexity**: O(1) per bind (network-dependent).
- **Use Case**: Used for enterprise user authentication.
- **Best Practice**: Use TLS; handle bind errors; secure credentials.