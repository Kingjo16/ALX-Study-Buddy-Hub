#!/usr/bin/python3

# Import necessary modules and classes
from datetime import datetime
from flask import Blueprint
from app import db, login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import UserMixin
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# Create a Blueprint named 'user' to group user-related routes and views
user = Blueprint('user', __name__)

# Define the user loader function for Flask-Login to load a user from the database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the User model to represent users in the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    firstname = db.Column(db.String(20), nullable=False)  # User's first name
    lastname = db.Column(db.String(20), nullable=False)  # User's last name
    email = db.Column(db.String(120), unique=True, nullable=False)  # User's email, must be unique
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')  # Profile image filename
    password = db.Column(db.String(60), nullable=False)  # User's password (hashed)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date and time the user joined

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.image_file}')"

# Define the registration form for new users to sign up
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])  # First name input field
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])  # Last name input field
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email input field
    password = PasswordField('Password', validators=[DataRequired()])  # Password input field
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  # Confirm password input field
    submit = SubmitField('Sign Up')  # Submit button

    # Custom validator to check if the email already exists in the database
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

# Define the login form for users to log in
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Email input field
    password = PasswordField('Password', validators=[DataRequired()])  # Password input field
    remember = BooleanField('Remember Me')  # Remember me checkbox
    submit = SubmitField('Log In')  # Submit button
