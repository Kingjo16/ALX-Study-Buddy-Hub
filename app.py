from flask import Flask, render_template
from routes.auth import auth
from routes.groups import group
from models.user import user
from models.group import groups
from models.forum import forums
from models.forum import Post

app = Flask(__name__)

app.config['SECRET_KEY'] = 'micku101820'


# Register the auth routes
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(group)
app.register_blueprint(groups)
app.register_blueprint(forums)



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)