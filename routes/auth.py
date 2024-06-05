from flask import Blueprint, render_template, flash, redirect, url_for
from models.user import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@auth.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'petrosworku19@gmail.com' and form.password.data == 'book9199':
            flash('You have been logged in!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('signin.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def regisreation():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}!', 'success')
        return redirect(url_for('auth.dashboard'))
    return render_template('signup.html', form=form)

