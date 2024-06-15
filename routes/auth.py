#!/usr/bin/python3

# Import necessary modules and classes
from app import db, bcrypt
from flask import Blueprint, render_template, flash, redirect, url_for, request
from models.user import RegistrationForm, LoginForm, User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

# Create a Blueprint named 'auth' to group authentication-related routes and views
auth = Blueprint('auth', __name__)

# Route for the dashboard, accessible only to logged-in users
@auth.route('/dashboard')
@login_required
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')

# Route for user login
@auth.route('/signin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # If the user is already logged in, redirect to the dashboard
        return redirect(url_for('auth.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        # If the login form is submitted and validated
        user = User.query.filter_by(email=form.email.data).first()
        # Check if the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Log the user in and remember them if the checkbox is checked
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            # Redirect to the dashboard after successful login
            return redirect(url_for('auth.dashboard'))
        else:
            # If login fails, show an error message
            flash('Login Unsuccessful. Please check email and password', 'danger')
    # Render the login template with the form
    return render_template('signin.html', form=form)

# Route for user registration
@auth.route('/signup', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        # If the user is already logged in, redirect to the dashboard
        return redirect(url_for('auth.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # If the registration form is submitted and validated
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create a new user with the form data
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
        # Add the new user to the database
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.firstname.data}!', 'success')
        # Redirect to the login page after successful registration
        return redirect(url_for('auth.login'))
    # Render the signup template with the form
    return render_template('signup.html', form=form)

# Route for user logout
@auth.route('/signout')
@login_required  # Ensure the user is logged in to log out
def signout():
    # Log the user out
    logout_user()
    # Redirect to the login page after logging out
    return redirect(url_for('auth.login'))
