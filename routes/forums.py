#!/usr/bin/python3

# Import necessary modules and classes
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.forum import db, PostForm, Post, 

# Create a Blueprint named 'forums' to group forum-related routes and views
forums = Blueprint('forums', __name__)

# Route for displaying the forum page
@forums.route('/forums')
def forum():
    return render_template('forum.html')  # Render the forum.html template

# Route for creating a new post
@forums.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()  # Create an instance of the PostForm
    if form.validate_on_submit():
        # If the form is submitted and validated
        new_post = Post(title=form.title.data, content=form.content.data)  # Create a new Post object
        db.session.add(new_post)  # Add the new post to the database session
        db.session.commit()  # Commit changes to the database
        flash('Your post has been created!', 'success')  # Flash a success message
        return redirect(url_for('forums.create_post'))  # Redirect to the create_post route (refresh the page)
    return render_template('create_post.html', form=form)  # Render the create_post.html template with the form
