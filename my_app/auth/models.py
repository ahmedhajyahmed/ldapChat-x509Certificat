import ldap
from ldap3 import Server, Connection, ALL
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired
from my_app import db, app
from flask_login._compat import unicode


def get_ldap_connection():
    # conn = ldap.initialize(app.config['LDAP_PROVIDER_URL'])
    server = Server('192.168.1.55', get_info=ALL)
    conn = Connection(server, 'cn=admin,dc=chatroom,dc=com', 'root', auto_bind=True)
    return conn


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username

    @staticmethod
    def try_login(username, password):
        # conn = get_ldap_connection()
        # conn.simple_bind_s(
        #     'cn=%s,cn=guest,ou=users,dc=chatroom,dc=com' % username,
        #     password
        # )
        conn = get_ldap_connection()
        conn.search('dc=chatroom,dc=com', '(&(cn=%s)(userPassword=%s))' % (username, password))
        return conn.entries

    @staticmethod
    def try_signup(cn, givenName, sn, departmentNumber, telephoneNumber, userPassword):
        conn = get_ldap_connection()
        conn.add('cn=%s,ou=myusers,dc=chatroom,dc=com' % cn, 'inetOrgPerson', {'givenName': givenName,
                                                                               'sn': sn,
                                                                               'departmentNumber': departmentNumber,
                                                                               'telephoneNumber': telephoneNumber,
                                                                               'userPassword': userPassword
                                                                               })
        return conn.result['description']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class LoginForm(Form):
    username = TextField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])


class SignupForm(Form):
    cn = TextField('cn', [InputRequired()])
    givenName = TextField('givenName', [InputRequired()])
    sn = TextField('sn', [InputRequired()])
    departmentNumber = TextField('departmentNumber', [InputRequired()])
    telephoneNumber = TextField('telephoneNumber', [InputRequired()])
    userPassword = PasswordField('userPassword', [InputRequired()])
