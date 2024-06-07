from flask import Blueprint, render_template, request, redirect, url_for
from models.forum import db, Post

forums = Blueprint('forums', __name__)

@forums.route('/forums')
def forum():
    return render_template('forum.html')


