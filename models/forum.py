#!/usr/bin/python3

# Import necessary modules and classes
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

# Create a Blueprint named 'forum' to group forum-related routes and views
forum = Blueprint('forum', __name__)

# Initialize SQLAlchemy for database operations
db = SQLAlchemy()

# Define the form for creating a new post
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])  # Title input field
    content = TextAreaField('Content', validators=[DataRequired()])  # Content input field
    submit = SubmitField('Post')  # Submit button

# Define the Post model to represent posts in the database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each post
    title = db.Column(db.String(100), nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Content of the post
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the post was created

# Define the form for adding a comment to a post
class CommentForm(FlaskForm):
    comment = TextAreaField('Content', validators=[DataRequired()])  # Comment input field
    submit = SubmitField('Comment')  # Submit button

    # Constructor to initialize the form with a post ID
    def __init__(self, post_id):
        super(CommentForm, self).__init__()
        self.post_id = post_id  # Store the post ID associated with the comment
