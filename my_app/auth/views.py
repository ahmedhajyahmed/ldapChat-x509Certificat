import ldap
from flask import request, render_template, flash, redirect, \
    url_for, Blueprint, g
from flask_login import current_user, login_user, \
    logout_user, login_required
from my_app import login_manager, db
from my_app.auth.models import User, LoginForm, SignupForm

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@auth.before_request
def get_current_user():
    g.user = current_user


@auth.route('/')
@auth.route('/home')
def home():
    return render_template('home.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('auth.home'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        password = request.form.get('password')

        if User.try_login(username, password).__len__() == 0:
            flash(
                'Invalid username or password. Please try again.',
                'danger')
            return render_template('login.html', form=form)

        user = User.query.filter_by(username=username).first()

        if not user:
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('auth.home'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))


@auth.route('/signup',  methods=['GET', 'POST'])
def signup():

    form = SignupForm(request.form)

    if request.method == 'POST' and form.validate():
        cn = request.form.get('cn')
        givenName = request.form.get('givenName')
        sn = request.form.get('sn')
        departmentNumber = request.form.get('departmentNumber')
        telephoneNumber = request.form.get('telephoneNumber')
        userPassword = request.form.get('userPassword')

        result = User.try_signup(cn, givenName, sn, departmentNumber, telephoneNumber, userPassword)
        if result == 'success':
            flash('You have successfully sign un.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(result, 'danger')
            return render_template('signup.html', form=form)
    if form.errors:
        flash(form.errors, 'danger')

    return render_template('signup.html', form=form)

