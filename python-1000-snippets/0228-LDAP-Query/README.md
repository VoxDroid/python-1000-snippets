# LDAP Query

## Description
This snippet demonstrates querying an LDAP directory using the `ldap3` library.

## Setup
These examples use `ldap3`'s `MOCK_SYNC` strategy to run an in-memory LDAP directory without requiring a real LDAP server.

## Code
In the `SAMPLES/` folder you'll find three runnable examples:

- `sample1.py` — query/mock LDAP directory search
- `sample2.py` — modify an LDAP entry
- `sample3.py` — delete an LDAP entry

Run any of them with:

```bash
python python-1000-snippets/0228-LDAP-Query/SAMPLES/sample1.py
```

## Output
The samples print LDAP entry DNs and attribute values found in the directory.

## Explanation
- **LDAP Query**: Searches an LDAP directory using standard filters (e.g., `(cn=John*)`).
- **Logic**: Bind to the directory, perform a search, and iterate over results.
- **Use Case**: Useful for querying user directories, authentication systems, or configuration stores.
- **Best Practice**: In production, use a real LDAP server and secure connections (LDAPS/STARTTLS).
