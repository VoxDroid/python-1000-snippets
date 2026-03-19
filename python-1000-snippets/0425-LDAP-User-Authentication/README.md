# LDAP User Authentication

## Description
This snippet demonstrates LDAP authentication and directory operations using the `ldap3` library.

The examples use an in-memory mock LDAP server (`MOCK_SYNC`) so they run without requiring an external LDAP service.

## Requirements
- Python 3.8+
- `ldap3` (`pip install ldap3`)

## Samples
- `SAMPLES/sample1.py`: Bind to the LDAP server as an admin user.
- `SAMPLES/sample2.py`: Search for a user entry by attribute.
- `SAMPLES/sample3.py`: Modify a user entry (change password) and re-authenticate.

## Running
```bash
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample1.py
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample2.py
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample3.py
```

## Notes
- These examples do not connect to a real LDAP server; they demonstrate LDAP operations in a mocked environment.
- For production, connect to a real LDAP server and use secure connections (LDAPS) as needed.
