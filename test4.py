from ldap3 import Server, Connection, ALL

server = Server('192.168.1.55',  get_info=ALL)
conn = Connection(server, 'cn=admin,dc=chatroom,dc=com', 'root', auto_bind=True)
print(conn.extend.standard.who_am_i())
conn.add('cn=bhajyahmed,ou=myusers,dc=chatroom,dc=com', 'inetOrgPerson', {'givenName': 'b',
                                                                          'sn': 'hajyahmed',
                                                                          'departmentNumber': 'DEV',
                                                                          'telephoneNumber': 1111,
                                                                          'userPassword': 'ahmed'
                                                                          })
print(conn.result['description'])

# close the connection

conn.unbind()