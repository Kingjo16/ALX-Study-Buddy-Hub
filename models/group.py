from flask import Blueprint
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired


db = SQLAlchemy()

groups = Blueprint('groups', __name__)

group_members = db.Table(
    'group_members',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('User', secondary='group_members', backref='groups')


class MemberForm(FlaskForm):
    name = StringField('Member Name', validators=[DataRequired()])
    email = StringField('Member Email', validators=[DataRequired()])


class GroupForm(FlaskForm):
    title = StringField('Group Name', validators=[DataRequired()])
    description = TextAreaField('Group Description', validators=[DataRequired()])
    members = FieldList(FormField(MemberForm), min_entries=1)
    submit = SubmitField('Create Group')


