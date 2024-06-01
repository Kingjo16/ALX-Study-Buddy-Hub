from app import db
from flask_login import UserMixin
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), nullable=False)
  last_name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
    
def __repr__(self):
  return f'<User {self.email}>'