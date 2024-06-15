#!/usr/bin/python3

# Import necessary modules and classes
from flask import Blueprint
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired

# Initialize SQLAlchemy for database operations
db = SQLAlchemy()

# Create a Blueprint named 'groups' to group group-related routes and views
groups = Blueprint('groups', __name__)

# Define association table for many-to-many relationship between groups and users
group_members = db.Table(
    'group_members',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

# Define the Group model to represent groups in the database
class Group(db.Model):
    __tablename__ = 'groups'  # Table name

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each group
    name = db.Column(db.String(100), nullable=False)  # Name of the group
    description = db.Column(db.Text, nullable=False)  # Description of the group
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the group was created
    members = db.relationship('User', secondary='group_members', backref='groups')  # Many-to-many relationship with users

# Define the form for adding a member to a group
class MemberForm(FlaskForm):
    name = StringField('Member Name', validators=[DataRequired()])  # Member name input field
    email = StringField('Member Email', validators=[DataRequired()])  # Member email input field

# Define the form for creating a new group
class GroupForm(FlaskForm):
    title = StringField('Group Name', validators=[DataRequired()])  # Group name input field
    description = TextAreaField('Group Description', validators=[DataRequired()])  # Group description input field
    members = FieldList(FormField(MemberForm), min_entries=1)  # List of members using MemberForm as subform
    submit = SubmitField('Create Group')  # Submit button for form submission


