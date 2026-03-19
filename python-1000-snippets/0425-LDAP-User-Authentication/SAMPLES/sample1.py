# sample1.py
# Demonstrates binding to an LDAP server using ldap3 with a mock in-memory server.

from ldap3 import Server, Connection, MOCK_SYNC


def main() -> None:
    # Create a mock LDAP server and populate it with a user entry.
    server = Server('my_fake_server')
    conn = Connection(
        server,
        user='cn=admin,dc=example,dc=com',
        password='secret',
        client_strategy=MOCK_SYNC,
    )

    # Define a simple directory tree and a user entry.
    conn.strategy.add_entry('dc=example,dc=com', {'objectClass': ['domain']})
    conn.strategy.add_entry(
        'cn=admin,dc=example,dc=com',
        {
            'objectClass': ['simpleSecurityObject', 'organizationalRole'],
            'cn': 'admin',
            'userPassword': 'secret',
        },
    )
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
            'userPassword': 'pass',
        },
    )

    # Perform a bind (authentication) using the supplied credentials.
    if conn.bind():
        print('Bind successful')
    else:
        print('Bind failed:', conn.result)

    conn.unbind()


if __name__ == '__main__':
    main()
