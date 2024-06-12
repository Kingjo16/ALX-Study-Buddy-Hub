#!/usr/bin/python3

import os
from flask import Flask, render_template
from routes.auth import auth
from routes.groups import group
from models.user import user
from models.group import groups
from models.forum import forum
from routes.forums import forums

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')


# Register the auth routes
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(group)
app.register_blueprint(groups)
app.register_blueprint(forums)
app.register_blueprint(forum)

@app.route('/')
def index():
    return render_template('index.html')

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
