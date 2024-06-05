from flask import Blueprint, render_template, request, redirect, url_for
from models.forum import db, Post

forums = Blueprint('forums', __name__)

@forums.route('/forums', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('forums.forum'))

    posts = Post.query.all()
    return render_template('forum.html', posts=posts)