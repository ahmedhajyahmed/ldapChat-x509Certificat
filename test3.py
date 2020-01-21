from ldap3 import Server, Connection, ALL

server = Server('192.168.1.55',  get_info=ALL)
# conn = Connection(server, auto_bind=True)
# print(server.info)
conn = Connection(server, 'cn=admin,dc=chatroom,dc=com', 'root', auto_bind=True)
print(conn.extend.standard.who_am_i())
# Create a container for new entries
conn.add('ou=myusers,dc=chatroom,dc=com', 'organizationalUnit')

# Add a new user
# conn.add('cn=b.young,ou=myusers,dc=chatroom,dc=com', 'inetOrgPerson', {'givenName': 'ahmed', 'sn': 'haj yahmed',
#                                                                      'departmentNumber': 'DEV', 'telephoneNumber': 1111,
#                                                                      'userCertificate': 'mycertif',
#                                                                      'email': 'ahmed@gmail.com'})
conn.add('cn=b.young,ou=myusers,dc=chatroom,dc=com', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
print(conn.entries)
# if (conn.search('ou=myusers,dc=chatroom,dc=com', '(cn=ahmed)', attributes=['cn', 'sn'])):
#     print('mawjoud')
#     print(conn.entries)
# else:
#     print('mech mawjoud')

# conn.search('dc=chatroom,dc=com', '(objectclass=inetOrgPerson)')
# print(conn.entries)

# conn.search('dc=chatroom,dc=com', '(objectclass=person)')
# print(conn.entries)

