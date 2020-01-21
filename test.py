import ldap
import ldap.modlist as modlist

try:
    conn = ldap.initialize('ldap://192.168.1.55:389/')
    conn.simple_bind_s('cn=admin,dc=chatroom,dc=com', 'root')
    print('jawek behy')
    # The dn of our new entry/object

    attributes = {
        "objectClass": [b"inetOrgPerson"],
        "sn": ['username'.encode('utf-8')],
        "cn": ['amine'.encode('utf-8')],
        "userPassword": ['amine'.encode('utf-8')],
    }

    # Convert our dict to nice syntax for the add-function using modlist-module
    ldif = modlist.addModlist(attributes)
    res = conn.add_s(
        'cn=' + 'amine' + ',ou=users,dc=chatroom,dc=com', ldif
    )


    # Its nice to the server to disconnect and free resources when done
    conn.unbind_s()

except Exception as e:
    print('fama mochkel')
    print(e)


# dn = "uid=amine,cn=guest,ou=users,dc=chatroom,dc=com"
#     modlist = {
#         "objectClass": ["inetOrgPerson", "posixAccount", "shadowAccount"],
#         "uid": ["amine"],
#         "sn": ["haj yahmed"],
#         "givenName": ["amine"],
#         "cn": ["amine haj yahmed"],
#         "displayName": ["amine haj yahmed"],
#         "uidNumber": ["5000"],
#         "gidNumber": ["500"],
#         "loginShell": ["/bin/bash"],
#         "homeDirectory": ["/home/users/ahajyahmed"]}
#
#     # addModList transforms your dictionary into a list that is conform to ldap input.
#     result = conn.add_s(dn, ldap.modlist.addModlist(modlist))


