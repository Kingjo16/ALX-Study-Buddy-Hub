from flask import Blueprint, render_template, flash, redirect, url_for
from models.group import Group, GroupForm, db

# Create a Blueprint named 'group' to manage group-related routes and views
group = Blueprint('group', __name__)

# Route to display all groups
@group.route('/groups')
def groups():
    # Fetch all groups from the database (commented out for now)
    # groups = Group.query.all()
    # Initialize an empty GroupForm instance (commented out for now)
    # form = GroupForm()
    return render_template('groups.html')

# Route to create a new group
@group.route('/create_groups', methods=['GET', 'POST'])
def create_group():
    form = GroupForm()  # Initialize GroupForm for handling group creation

    if form.validate_on_submit():
        # Create a new Group object with data from the form
        new_group = Group(name=form.title.data, description=form.description.data)
        db.session.add(new_group)  # Add the new group to the database session
        db.session.commit()  # Commit the transaction to the database
        flash('Your group has been created!', 'success')  # Flash success message
        return redirect(url_for('group.create_group'))  # Redirect to the create_group route

    # If form validation fails or if it's a GET request, render the create_group template with the form
    return render_template('create_group.html', form=form)
