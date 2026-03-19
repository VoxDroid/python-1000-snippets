# 0425 - LDAP User Authentication Cheatsheet

## Quick Facts
- Uses `ldap3` with the `MOCK_SYNC` client strategy to simulate an LDAP server in-memory.
- Demonstrates bind (authentication), search, and modify operations.

## Run Samples
```bash
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample1.py
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample2.py
python python-1000-snippets/0425-LDAP-User-Authentication/SAMPLES/sample3.py
```

## Key ldap3 APIs
- `Server(...)` and `Connection(..., client_strategy=MOCK_SYNC)` to setup a mock server.
- `connection.bind()` to authenticate.
- `connection.search(base_dn, search_filter, attributes=[...])` to find entries.
- `connection.modify(dn, changes)` to update attributes.

## Notes
- The mock server does not require network connectivity and stores entries only in memory.
- Replace `MOCK_SYNC` with `SYNC` or `ASYNC` and provide a real server URI to connect to an actual LDAP service.
