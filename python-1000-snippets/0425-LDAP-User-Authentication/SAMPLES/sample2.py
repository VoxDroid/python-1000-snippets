# sample2.py
# Demonstrates searching an LDAP directory for a user entry using ldap3 (mock server).

from ldap3 import Server, Connection, MOCK_SYNC, ALL


def main() -> None:
    server = Server('my_fake_server', get_info=ALL)
    conn = Connection(
        server,
        user='cn=admin,dc=example,dc=com',
        password='secret',
        client_strategy=MOCK_SYNC,
    )

    # Populate the mock directory.
    conn.strategy.add_entry('dc=example,dc=com', {'objectClass': ['domain']})
    conn.strategy.add_entry(
        'ou=users,dc=example,dc=com',
        {'objectClass': ['organizationalUnit'], 'ou': 'users'},
    )
    conn.strategy.add_entry(
        'cn=user,ou=users,dc=example,dc=com',
        {
            'objectClass': ['person', 'inetOrgPerson'],
            'cn': 'user',
            'sn': 'User',
            'mail': 'user@example.com',
            'userPassword': 'pass',
        },
    )

    conn.bind()

    # Search for the user by mail attribute.
    conn.search(
        'dc=example,dc=com',
        '(mail=user@example.com)',
        attributes=['cn', 'mail'],
    )

    print('Search result entries:')
    for entry in conn.entries:
        print(entry)

    conn.unbind()


if __name__ == '__main__':
    main()
