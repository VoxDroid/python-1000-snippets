# sample3.py
# Demonstrates modifying an LDAP entry (e.g., password) and verifying the change.

from ldap3 import Server, Connection, MOCK_SYNC


def main() -> None:
    server = Server('my_fake_server')
    conn = Connection(
        server,
        user='cn=admin,dc=example,dc=com',
        password='secret',
        client_strategy=MOCK_SYNC,
    )

    # Populate directory with a user entry.
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
            'userPassword': 'pass',
        },
    )

    conn.bind()

    # Modify the user's password attribute.
    conn.modify('cn=user,ou=users,dc=example,dc=com', {'userPassword': [(2, ['newpass'])]})
    print('Modify result:', conn.result)

    conn.unbind()

    # Verify the password change by binding as the user.
    conn2 = Connection(
        server,
        user='cn=user,ou=users,dc=example,dc=com',
        password='newpass',
        client_strategy=MOCK_SYNC,
    )
    print('User bind successful:', conn2.bind())
    conn2.unbind()


if __name__ == '__main__':
    main()
