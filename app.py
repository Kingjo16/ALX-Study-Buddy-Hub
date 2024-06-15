#!/usr/bin/python3

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import Blueprints and models
from routes.auth import auth
from routes.groups import group
from routes.forums import forums
from models import db
from models.user import user
from models.group import groups
from models.forum import forum

# Initialize Flask application
app = Flask(__name__)

# Configure application
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://study_user:new_password@localhost/study_buddy_hub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints for different routes
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(group)
app.register_blueprint(groups)
app.register_blueprint(forums)
app.register_blueprint(forum)

# Default route
@app.route('/')
def index():
    return render_template('index.html')

# Error handling for 404 Not Found errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handling for 500 Internal Server errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all database tables defined in models
    app.run(debug=True)  # Run the Flask app in debug mode
