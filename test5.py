from ldap3 import Server, Connection, ALL

server = Server('192.168.1.55',  get_info=ALL)
conn = Connection(server, 'cn=admin,dc=chatroom,dc=com', 'root', auto_bind=True)
print(conn.extend.standard.who_am_i())
username = 'amhajyahmed'
password = 'ahmed'
conn.search('dc=chatroom,dc=com', '(&(cn=%s)(userPassword=%s))' % (username, password))
print(conn.entries)
