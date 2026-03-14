# 0228-LDAP-Query Cheatsheet

## Run
```bash
python python-1000-snippets/0228-LDAP-Query/SAMPLES/sample1.py
python python-1000-snippets/0228-LDAP-Query/SAMPLES/sample2.py
python python-1000-snippets/0228-LDAP-Query/SAMPLES/sample3.py
```

## Key points
* Use `ldap3` to connect to an LDAP directory and perform searches.
* Create a `Server` and `Connection` object; bind with credentials.
* Use `connection.search(base_dn, search_filter, attributes=[...])`.
* Access results via `connection.entries`.
* For testing, use `client_strategy=MOCK_SYNC` to run an in-memory directory.
* In production, use secure LDAP (LDAPS/STARTTLS) and proper access controls.
