from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.forum import db, PostForm


forums = Blueprint('forums', __name__)

@forums.route('/forums')
def forum():
    return render_template('forum.html')

@forums.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = PostForm(title=form.title.data, content=form.content.data)
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('forums.create_post'))
    return render_template('create_post.html', form=form)
