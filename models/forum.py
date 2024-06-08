from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

forum = Blueprint('forum', __name__)

db = SQLAlchemy()

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CommentForm(FlaskForm):
    comment = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Comment')
    def __init__(self, post_id):
        self.post_id = post_id
        