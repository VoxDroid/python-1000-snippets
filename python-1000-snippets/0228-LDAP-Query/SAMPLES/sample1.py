# sample1.py
# Demonstrate an LDAP query using ldap3 with an in-memory mock server.

from ldap3 import Server, Connection, OFFLINE_AD_2012_R2, MOCK_SYNC


def main():
    # Create a mock LDAP server and populate it with one entry.
    server = Server('my_fake_server', get_info=OFFLINE_AD_2012_R2)
    conn = Connection(server, user='cn=admin,dc=example,dc=com', password='password', client_strategy=MOCK_SYNC)
    conn.bind()

    # Add a base entry and a test user entry.
    conn.strategy.add_entry('dc=example,dc=com', {'objectClass': 'domain', 'dc': 'example'})
    conn.strategy.add_entry(
        'cn=John Doe,dc=example,dc=com',
        {
            'objectClass': ['person', 'inetOrgPerson'],
            'cn': 'John Doe',
            'sn': 'Doe',
            'mail': 'john.doe@example.com',
        },
    )

    # Perform a search and print results.
    conn.search('dc=example,dc=com', '(cn=John*)', attributes=['cn', 'mail'])
    for entry in conn.entries:
        print('Found entry:', entry.entry_dn)
        print('  CN:', entry.cn)
        print('  Mail:', entry.mail)

    conn.unbind()


if __name__ == '__main__':
    main()
