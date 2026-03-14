# sample3.py
# Demonstrate deleting an LDAP entry using ldap3's MOCK_SYNC strategy.

from ldap3 import Server, Connection, OFFLINE_AD_2012_R2, MOCK_SYNC


def main():
    server = Server('my_fake_server', get_info=OFFLINE_AD_2012_R2)
    conn = Connection(server, user='cn=admin,dc=example,dc=com', password='password', client_strategy=MOCK_SYNC)
    conn.bind()

    conn.strategy.add_entry('cn=Temp User,dc=example,dc=com', {
        'objectClass': ['person', 'inetOrgPerson'],
        'cn': 'Temp User',
        'sn': 'User',
        'mail': 'temp.user@example.com',
    })

    # Verify entry exists
    conn.search('dc=example,dc=com', '(cn=Temp User)', attributes=['cn', 'mail'])
    print('Before delete:', [e.entry_dn for e in conn.entries])

    # Delete the entry
    conn.delete('cn=Temp User,dc=example,dc=com')

    conn.search('dc=example,dc=com', '(cn=Temp User)', attributes=['cn', 'mail'])
    print('After delete:', [e.entry_dn for e in conn.entries])

    conn.unbind()


if __name__ == '__main__':
    main()
