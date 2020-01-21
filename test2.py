import ldap

dn = 'uid=amine,cn=admin,dc=chatroom,dc=com'
fullname = 'amine haj yahmed'
home_dir = '/home/users/amine'
gid = 500

entry = []
entry.extend([
    ('objectClass', ["person", "organizationalPerson", "inetOrgPerson", "posixAccount", "top", "shadowAccount", "hostObject"]),
    ('uid', 'amine'),
    ('cn', fullname),
    ('givenname', 'amine'),
    ('sn', 'haj yahmed'),
    ('mail', 'amine@gmail.com'),
    ('uidNumber', '2000'),
    ('gidNumber', str(gid)),
    ('loginShell', '/bin/sh'),
    ('homeDirectory', home_dir),
    ('shadowMax', "99999"),
    ('shadowWarning', "7"),
    ('userPassword', 'amine')
])

ldap_conn = ldap.initialize('ldap://192.168.1.55:389/')
ldap_conn.simple_bind_s('cn=admin,dc=chatroom,dc=com', 'root')


ldap_conn.add_s(dn, entry)

ldap_conn.unbind_s()