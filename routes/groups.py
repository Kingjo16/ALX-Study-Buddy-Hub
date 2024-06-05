from flask import Blueprint, render_template, flash, redirect, url_for
from models.group import Group, GroupForm, db

group = Blueprint('group', __name__)

@group.route('/groups')
def groups():
    groups = Group.query.all()
    form = GroupForm()
    return render_template('groups.html', groups=groups, form=form)

@group.route('/create_groups', methods=['GET', 'POST'])
def create_group():
    form = GroupForm()
    if form.validate_on_submit():
        new_group = Group(name=form.title.data, description=form.description.data)
        db.session.add(new_group)
        db.session.commit()
        flash('Your group has been created!', 'success')
        return redirect(url_for('group.create_group'))
    
    else:                   
        return render_template('create_group.html', form=form)


"""@group_bp.route('/group/<int:group_id>')
def view_group(group_id):
    group = Group.query.get(group_id)
    return render_template('view_group.html', group=group)"""