# LDAP Query

## Description
This snippet demonstrates querying an LDAP server using `python-ldap`.

## Code
```python
# Note: Requires `python-ldap`. Install with `pip install python-ldap`
try:
    import ldap
    conn = ldap.initialize("ldap://localhost:389")
    conn.simple_bind_s("cn=admin,dc=example,dc=com", "password")
    result = conn.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=alice)")
    print("Found:", result[0][1]["uid"][0].decode())
    conn.unbind_s()
except ImportError:
    print("Mock Output: Found: alice")
```

## Output
```
Mock Output: Found: alice
```
*(Real output with LDAP: `Found: alice`)*

## Explanation
- **LDAP Query**: Searches for a user in an LDAP directory using `python-ldap`.
- **Logic**: Binds to the server and searches for a user by `uid`.
- **Complexity**: O(n) for n entries in the search scope.
- **Use Case**: Used for authentication or directory services.
- **Best Practice**: Use LDAPS for security; handle bind errors; ensure server is running.