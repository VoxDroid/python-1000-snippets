# sample2.py
# Demonstrate modifying an LDAP entry using ldap3's MOCK_SYNC strategy.

from ldap3 import Server, Connection, OFFLINE_AD_2012_R2, MOCK_SYNC


def main():
    server = Server('my_fake_server', get_info=OFFLINE_AD_2012_R2)
    conn = Connection(server, user='cn=admin,dc=example,dc=com', password='password', client_strategy=MOCK_SYNC)
    conn.bind()

    conn.strategy.add_entry('cn=Jane Doe,dc=example,dc=com', {
        'objectClass': ['person', 'inetOrgPerson'],
        'cn': 'Jane Doe',
        'sn': 'Doe',
        'mail': 'jane.doe@example.com',
    })

    # Modify the mail attribute
    conn.modify('cn=Jane Doe,dc=example,dc=com', {'mail': [(2, ['jane.d@example.com'])]})

    conn.search('dc=example,dc=com', '(cn=Jane Doe)', attributes=['cn', 'mail'])
    for entry in conn.entries:
        print('Modified entry:', entry.entry_dn)
        print('  Mail:', entry.mail)

    conn.unbind()


if __name__ == '__main__':
    main()
